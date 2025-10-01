import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from scapy.all import sniff, IP, TCP, UDP, ICMP, AsyncSniffer
import psutil
import os
import warnings
from pathlib import Path
from collections import deque

# Suppress minor warnings for a cleaner interface
warnings.filterwarnings('ignore')

# --- CONFIGURATION & SETUP ---
st.set_page_config(
    page_title="Sentinel-Net: AI-Powered NIDS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Relative Directory Structure for your files
MODELS_BASE_DIR = Path("models")
SCALERS_DIR = Path("scalers")
CICIDS_BINARY_DIR = MODELS_BASE_DIR / 'cicids_binary'
CICIDS_MULTICLASS_DIR = MODELS_BASE_DIR / 'cicids_multiclass'
CICIDS_PREPROCESSOR_FILE = SCALERS_DIR / 'cicids_preprocessor.pkl'

# Global state setup
if 'is_monitoring' not in st.session_state:
    st.session_state.is_monitoring = False
if 'detector' not in st.session_state:
    st.session_state.detector = None

# --- UTILITY CLASS: INTRUSION DETECTOR ---
class NetworkIntrusionDetector:
    def __init__(self, preprocessor_data, binary_models, multiclass_models):
        """Initializes detector with loaded resources."""
        self.scaler = preprocessor_data.get('scaler')
        # Note: CICIDS feature names contain leading spaces
        self.feature_names = preprocessor_data.get('feature_names', [])
        
        self.binary_models = binary_models
        self.multiclass_models = multiclass_models
        self.dataset_type = "CICIDS2017" # Fixed for your context
        
        self.selected_model_type = None
        self.selected_model_name = None
        self.model = None
        self.is_monitoring = st.session_state.is_monitoring
        self.sniffer = None
        self.packets_captured = 0
        self.intrusion_count = 0
        self.normal_count = 0
        self.detection_history = deque(maxlen=200)

    def load_selected_model(self, model_name, model_type):
        """Swaps the active model for live monitoring/CSV analysis."""
        self.selected_model_name = model_name
        self.selected_model_type = model_type
        
        if model_type == 'binary':
            self.model = self.binary_models.get(model_name)
        else: # 'multiclass'
            self.model = self.multiclass_models.get(model_name)
        
        if self.model is None:
            st.error(f"❌ Error: Could not find model for '{model_name}' ({model_type}).")
            return False
        
        st.success(f"✅ Active Model Loaded: **{model_name}** ({model_type.capitalize()})")
        return True

    def get_model_classes(self):
        """Returns the class names/labels for the currently selected model."""
        if self.selected_model_type == 'binary':
            return {0: 'BENIGN', 1: 'Attack'}
        elif self.selected_model_type == 'multiclass' and self.model and hasattr(self.model, 'classes_'):
            return {i: c for i, c in enumerate(self.model.classes_)}
        return {0: 'Unknown (0)', 1: 'Unknown (1)'}
        
    def extract_features(self, pkt):
        """
        A simplified feature extraction for live packets to match a subset 
        of CICIDS features.
        """
        features = {}
        
        # Initialize all required features to 0.0
        for f in self.feature_names:
            features[f] = 0.0 
            
        # --- Populate a few essential features from the packet ---
        
        # 1. Destination Port
        dport = 0
        if TCP in pkt:
            dport = pkt[TCP].dport
        elif UDP in pkt:
            dport = pkt[UDP].dport
        features[' Destination Port'] = dport

        # 2. Total Length of Fwd Packets (Approximation)
        features[' Total Length of Fwd Packets'] = len(pkt)
        
        # 3. Fwd Header Length (Approximation)
        fwd_header_len = 0
        if IP in pkt:
            fwd_header_len += pkt[IP].ihl * 4 
            if TCP in pkt:
                 fwd_header_len += pkt[TCP].dataofs * 4 
            elif UDP in pkt:
                fwd_header_len += 8
        features[' Fwd Header Length'] = fwd_header_len
        features[' Fwd Header Length.1'] = fwd_header_len # CICIDS has this duplicate
        
        # 4. Total Fwd Packets (Simplified, as real feature tracks flow)
        features[' Total Fwd Packets'] = 1
        
        # Create DataFrame from the dictionary
        df = pd.DataFrame([features])[self.feature_names]
        
        # Clean infinite values before scaling (RobustScaler practice)
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.fillna(0, inplace=True) 
        
        return df

    def get_protocol_name_live(self, pkt):
        """Gets a human-readable protocol name for live sniffed packet."""
        if TCP in pkt: return "TCP"
        if UDP in pkt: return "UDP"
        if ICMP in pkt: return "ICMP"
        if IP in pkt: 
            try:
                # Use Scapy's definition of protocol number to name
                return IP.fields["proto"].i2s[pkt[IP].proto]
            except:
                return "IP"
        return "Other"

    def get_risk_level(self, confidence):
        """Maps confidence score to a risk level."""
        if confidence > 0.95: return 'High'
        if confidence > 0.8: return 'Medium'
        return 'Low'

    def packet_handler(self, pkt):
        """Handle captured packets and perform intrusion detection."""
        if not self.is_monitoring or self.model is None or not (IP in pkt):
            return
        
        try:
            self.packets_captured += 1
            
            # 1. Feature Extraction and Scaling
            feature_df = self.extract_features(pkt)
            
            if self.scaler is not None:
                scaled_features = self.scaler.transform(feature_df)
            else:
                scaled_features = feature_df.values

            # 2. Prediction
            prediction_label = "Error"
            confidence = 0.0
            
            if hasattr(self.model, 'predict'):
                raw_pred = self.model.predict(scaled_features)[0]
                
                class_map = self.get_model_classes()
                prediction_label = class_map.get(raw_pred, str(raw_pred))
                
                if hasattr(self.model, 'predict_proba'):
                    probabilities = self.model.predict_proba(scaled_features)[0]
                    confidence = np.max(probabilities)
                    
            # 3. Store Detection
            is_intrusion = prediction_label != 'Normal' and prediction_label != 'BENIGN'
            risk_level = self.get_risk_level(confidence)

            detection = {
                'Timestamp': datetime.now().strftime("%H:%M:%S"),
                'Src_IP': pkt[IP].src,
                'Dst_IP': pkt[IP].dst,
                'Dst_Port': feature_df[' Destination Port'].iloc[0],
                'Protocol': self.get_protocol_name_live(pkt),
                'Prediction': prediction_label,
                'Confidence': f"{confidence:.4f}",
                'Risk': risk_level
            }
            
            self.detection_history.append(detection)
            
            if is_intrusion:
                self.intrusion_count += 1
            else:
                self.normal_count += 1
                
        except Exception as e:
            pass

    def start_monitoring(self, interface=None):
        """Starts the sniffing process in a non-blocking way."""
        if st.session_state.is_monitoring:
            return

        if self.model is None:
            st.error("Please load a model first!")
            return False

        self.is_monitoring = True
        st.session_state.is_monitoring = True
        
        try:
            self.sniffer = AsyncSniffer(prn=self.packet_handler, store=False, iface=interface, count=0)
            self.sniffer.start()
            return True
        except Exception as e:
            st.error(f"Monitoring error: Could not start sniffer. Check permissions (run with sudo) or interface name. Error: {str(e)}")
            self.is_monitoring = False
            st.session_state.is_monitoring = False
            return False

    def stop_monitoring(self):
        """Stops the sniffing process."""
        if self.sniffer and self.sniffer.running:
            self.sniffer.stop()
            self.sniffer = None
        self.is_monitoring = False
        st.session_state.is_monitoring = False
        
    def predict_csv(self, df_input):
        """Perform batch prediction on CSV data."""
        if self.model is None or self.scaler is None:
            st.error("Please load a model and scaler first!")
            return pd.DataFrame()

        try:
            X = df_input.copy()
            
            # 1. Align Features (Essential for successful scaling)
            for feature in self.feature_names:
                if feature not in X.columns:
                    X[feature] = 0.0
            
            X = X[self.feature_names]
            
            # 2. Data Cleaning & Scaling
            X.replace([np.inf, -np.inf], np.nan, inplace=True)
            X.fillna(X.mean(), inplace=True) 
            X.fillna(0, inplace=True)
            
            features_scaled = self.scaler.transform(X)
            
            # 3. Predict
            predictions = self.model.predict(features_scaled)
            probabilities = self.model.predict_proba(features_scaled)
            confidences = np.max(probabilities, axis=1)
            
            # 4. Format Results
            class_map = self.get_model_classes()
            results = []
            
            for i, (pred_code, conf) in enumerate(zip(predictions, confidences)):
                pred_label = class_map.get(pred_code, str(pred_code))
                
                is_intrusion = pred_label != 'Normal' and pred_label != 'BENIGN'
                
                results.append({
                    'Row_ID': i + 1,
                    'Prediction_Label': pred_label,
                    'Intrusion': 'YES' if is_intrusion else 'NO',
                    'Confidence': f"{conf:.4f}",
                    'Risk': self.get_risk_level(conf) if is_intrusion else 'None'
                })
            
            return pd.DataFrame(results)
            
        except Exception as e:
            st.error(f"CSV prediction execution error: {str(e)}")
            st.warning("Ensure your CSV features match the expected 78 CICIDS 2017 features.")
            return pd.DataFrame()


# --- RESOURCE LOADING ---
@st.cache_resource
def load_resources():
    """Loads all models and the preprocessor from the file system."""
    
    # 1. Load Preprocessor/Scaler
    if not CICIDS_PREPROCESSOR_FILE.exists():
        return None, None, None
        
    try:
        preprocessor_data = joblib.load(CICIDS_PREPROCESSOR_FILE)
    except Exception as e:
        st.error(f"❌ Error loading preprocessor: {e}")
        return None, None, None
    
    # 2. Load Binary Models
    binary_models = {}
    for filename in os.listdir(CICIDS_BINARY_DIR):
        if filename.endswith(".pkl"):
            model_path = CICIDS_BINARY_DIR / filename
            try:
                model = joblib.load(model_path)
                model_name = filename.replace('.pkl', '').replace('_', ' ').title()
                binary_models[model_name] = model
            except Exception as e:
                st.warning(f"⚠️ Failed to load binary model {filename}: {e}")
                
    # 3. Load Multi-Class Models
    multiclass_models = {}
    for filename in os.listdir(CICIDS_MULTICLASS_DIR):
        if filename.endswith(".pkl"):
            model_path = CICIDS_MULTICLASS_DIR / filename
            try:
                model = joblib.load(model_path)
                model_name = filename.replace('.pkl', '').replace('_', ' ').title()
                multiclass_models[model_name] = model
            except Exception as e:
                st.warning(f"⚠️ Failed to load multi-class model {filename}: {e}")

    return preprocessor_data, binary_models, multiclass_models

# --- MAIN APP FUNCTION ---
def main():
    
    st.title("🛡️ Sentinel-Net: AI-Powered Network Intrusion Detection System")
    # Credit Mohan Raaj C clearly
    st.markdown("Developed by Mohan Raaj C for the CICIDS 2017 Dataset.")
    st.markdown("---")
    
    # Check setup and load resources
    if not (CICIDS_BINARY_DIR.exists() and SCALERS_DIR.exists()):
        st.warning("⚠️ **Model folders not found.** Please ensure the required file structure exists in your current directory.")
        st.stop()
        
    preprocessor_data, binary_models, multiclass_models = load_resources()

    if preprocessor_data is None:
        st.error("❌ Critical: Failed to load preprocessor data. Stopping app.")
        st.stop()
    
    # Initialize Detector in session state
    if st.session_state.detector is None:
        st.session_state.detector = NetworkIntrusionDetector(
            preprocessor_data, binary_models, multiclass_models
        )
    
    detector = st.session_state.detector
    
    # --- SIDEBAR CONFIGURATION ---
    with st.sidebar:
        st.header("Configuration")
        
        # 1. Detection Mode Selection (Matches friend's UI)
        detection_mode = st.radio(
            "Select Detection Mode",
            ["Live Network Monitoring", "CSV File Analysis"],
            key='detection_mode'
        )
        
        # --- Dataset Selection (Fixed to CICIDS2017 for your files) ---
        st.selectbox("Select Dataset", ["CICIDS2017"], index=0)
        st.success("✅ Scaler available for CICIDS2017")
        
        # 2. Model Type Selection
        model_options = {}
        if detector.binary_models:
            model_options['Binary Classification (BENIGN/Attack)'] = detector.binary_models
        if detector.multiclass_models:
            model_options['Multi-class Classification (Specific Attacks)'] = detector.multiclass_models

        if not model_options:
            st.error("❌ No models could be loaded. Check file paths and contents.")
            st.stop()

        model_type_selection = st.selectbox(
            "Select Classification Type",
            list(model_options.keys()),
            key='model_type_select'
        )
        
        selected_model_type_key = 'binary' if 'Binary' in model_type_selection else 'multiclass'
        
        # 3. Model Algorithm Selection
        available_algos = list(model_options[model_type_selection].keys())
        model_option = st.selectbox(
            f"Select {model_type_selection} Algorithm",
            available_algos,
            key='model_select'
        )

        # 4. Load Model Button
        if st.button("Load/Change Model", type="primary"):
            with st.spinner(f"Loading {model_option}..."):
                detector.load_selected_model(model_option, selected_model_type_key)
        
        # --- Live Statistics Section (Moved to match the image layout) ---
        st.markdown("---")
        st.subheader("Live Statistics")
        st.metric("Packets Captured", detector.packets_captured)
        st.metric("Intrusions Detected", detector.intrusion_count)
        st.metric("Normal Traffic", detector.normal_count)
        
        if detector.packets_captured > 0:
            intrusion_rate = (detector.intrusion_count / detector.packets_captured) * 100
            st.metric("Intrusion Rate", f"{intrusion_rate:.2f}%")
        
        # --- Live Monitoring Controls (Placed after stats in the image's context) ---
        st.markdown("---")
        if detection_mode == "Live Network Monitoring":
            
            interfaces = list(psutil.net_if_addrs().keys())
            selected_interface = st.selectbox(
                "Network Interface (Requires sudo/admin)",
                interfaces,
                index=0
            )
            
            col1, col2 = st.columns(2)
            with col1:
                start_disabled = detector.model is None or st.session_state.is_monitoring
                if st.button("Start Monitoring 🚀", disabled=start_disabled, key="start_live"):
                    if detector.start_monitoring(selected_interface):
                        st.session_state.is_monitoring = True
                        st.experimental_rerun()
            
            with col2:
                stop_disabled = not st.session_state.is_monitoring
                if st.button("Stop Monitoring 🛑", disabled=stop_disabled, key="stop_live"):
                    detector.stop_monitoring()
                    st.session_state.is_monitoring = False
                    st.experimental_rerun()
            
            if st.session_state.is_monitoring:
                st.info(f"🔴 Live monitoring active on **{detector.selected_model_name}**.")

    # --- MAIN CONTENT AREA ---
    
    # --- CSV Analysis UI ---
    if detection_mode == "CSV File Analysis":
        st.subheader("📁 CSV File Analysis")
        
        if detector.model is None:
             st.warning("⚠️ Please load a model first to analyze CSV files.")
        
        uploaded_file = st.file_uploader(
            "Upload network traffic CSV file for batch analysis",
            type=['csv'],
            help=f"The CSV should contain features matching the **{detector.dataset_type}** format."
        )
        
        if uploaded_file is not None and detector.model is not None:
            try:
                df_upload = pd.read_csv(uploaded_file)
                st.success(f"✅ CSV file loaded successfully! Shape: {df_upload.shape}")
                
                with st.expander("Preview uploaded data"):
                    st.dataframe(df_upload.head(5), use_container_width=True)
                
                if st.button("Analyze CSV File", type="primary"):
                    with st.spinner("Analyzing CSV file..."):
                        results_df = detector.predict_csv(df_upload)
                        detector.csv_results = results_df
                        
                        if not results_df.empty:
                            st.subheader("Analysis Results")
                            # Style the output
                            def color_intrusion(val):
                                color = 'red' if val == 'YES' else 'green'
                                return f'color: {color}'
                            
                            styled_results_df = results_df.style.applymap(color_intrusion, subset=['Intrusion'])
                            st.dataframe(styled_results_df, use_container_width=True)
                            
                            # Download results
                            csv = results_df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label="Download Results as CSV",
                                data=csv,
                                file_name="intrusion_detection_results.csv",
                                mime="text/csv"
                            )
                        else:
                            st.warning("No results to display. Check for prediction errors.")
                            
            except Exception as e:
                st.error(f"Error processing CSV file: {str(e)}")

        # --- CSV Analysis Visualization ---
        if detector.csv_results is not None and not detector.csv_results.empty:
            st.markdown("---")
            st.subheader("📈 Batch Analysis Visualization")
            results_df = detector.csv_results
            
            col1, col2 = st.columns(2)
            
            with col1:
                pred_counts = results_df['Prediction_Label'].value_counts()
                fig, ax = plt.subplots(figsize=(6, 6))
                
                color_map = {'BENIGN': '#51cf66', 'Attack': '#ff6b6b'}
                
                if detector.selected_model_type == 'multiclass':
                    unique_labels = pred_counts.index.tolist()
                    colors = [color_map.get(label, sns.color_palette("Set2")[i % len(sns.color_palette("Set2"))]) 
                              for i, label in enumerate(unique_labels)]
                else:
                    colors = [color_map.get(label, '#ff6b6b') for label in pred_counts.index]
                
                ax.pie(pred_counts.values, labels=pred_counts.index, autopct='%1.1f%%', 
                       startangle=90, colors=colors)
                ax.set_title('Prediction Distribution')
                st.pyplot(fig)
            
            with col2:
                intrusion_counts = results_df['Intrusion'].value_counts()
                fig, ax = plt.subplots(figsize=(6, 6))
                sns.barplot(x=intrusion_counts.index, y=intrusion_counts.values, ax=ax, 
                            palette=['#ff6b6b', '#51cf66'], order=['YES', 'NO'])
                ax.set_title('Intrusion vs. Normal Traffic')
                ax.set_ylabel('Count')
                st.pyplot(fig)
        
    # --- Live Monitoring UI ---
    elif detection_mode == "Live Network Monitoring":
        
        if detector.model is not None:
             st.success(f"🔍 Active Model: **{detector.selected_model_name}**")
        else:
            st.warning("⚠️ No model loaded. Please select and load a model from the sidebar.")

        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("📊 Real-time Detection Dashboard")
            
            if detector.detection_history:
                recent_detections = list(detector.detection_history)[::-1]
                df_detections = pd.DataFrame(recent_detections)
                
                def color_risk_level(val):
                    if val == 'High': return 'color: red; font-weight: bold'
                    if val == 'Medium': return 'color: orange'
                    if val == 'Low': return 'color: green'
                    return ''
                
                styled_df = df_detections.style.applymap(color_risk_level, subset=['Risk'])
                st.dataframe(styled_df, use_container_width=True)
            else:
                st.info("No detections yet. Start monitoring to see live analysis.")
        
        with col2:
            st.subheader("🚨 Threat Overview")
            
            if detector.detection_history:
                recent_intrusions = [d for d in list(detector.detection_history) if d['Prediction'] != 'Normal' and d['Prediction'] != 'BENIGN']
                
                if recent_intrusions:
                    st.error(f"🚨 {len(recent_intrusions)} recent intrusions detected!")
                    
                    high_threats = [d for d in recent_intrusions if d['Risk'] == 'High']
                    if high_threats:
                        st.warning(f"⚠️ {len(high_threats)} high-confidence threats!")
                        
                    threat_protocols = pd.Series([d['Protocol'] for d in recent_intrusions]).value_counts()
                    for protocol, count in threat_protocols.items():
                        st.write(f"• {protocol}: {count} threats")
                else:
                    st.success("✅ No recent intrusions detected")
            else:
                st.info("Waiting for network traffic...")
            
        # Rerun logic to keep live updates flowing
        if st.session_state.is_monitoring:
            time.sleep(1)
            st.experimental_rerun()

    # --- ABOUT MOHAN RAAJ C ---
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; padding: 20px; font-family: Arial, sans-serif;'>
        <h4 style='margin-bottom: 5px;'>Project Sentinel-Net by Mohan Raaj C</h4>
        <p style='margin: 5px 0;'>
            This application utilizes machine learning models (**Random Forest, Decision Tree, Logistic Regression, Gradient Boosting**) 
            trained specifically on the **CICIDS 2017** dataset for intrusion detection.
        </p>
        <p style='margin: 5px 0;'>
            Thank you for using the Sentinel-Net system.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()