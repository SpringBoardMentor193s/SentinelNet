import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
import time
import threading
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from scapy.all import sniff, IP, TCP, UDP, ICMP
import psutil
import os
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Sentinel-Net: AI-Powered NIDS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

class NetworkIntrusionDetector:
    def __init__(self):
        self.selected_model = None
        self.selected_dataset = None
        self.model = None
        self.scaler = None
        self.feature_names = None
        self.is_monitoring = False
        self.packets_captured = 0
        self.intrusion_count = 0
        self.normal_count = 0
        self.packet_data = []
        self.detection_history = []
        self.csv_results = []
        
    def inspect_model(self, model_path):
        """Inspect the structure of the model file"""
        try:
            model_data = joblib.load(model_path)
            st.info(f"Model structure: {type(model_data)}")
            if isinstance(model_data, dict):
                st.info(f"Model keys: {list(model_data.keys())}")
            elif hasattr(model_data, '__class__'):
                st.info(f"Model type: {model_data.__class__.__name__}")
            return model_data
        except Exception as e:
            st.error(f"Inspection error: {str(e)}")
            return None
    
    def load_scaler(self, dataset):
        """Load the scaler for the specific dataset"""
        try:
            if dataset == "NSL-KDD":
                scaler_path = r"C:\Users\amity\SentinelNet\models\nslkdd\scaler.pkl"
            elif dataset == "CICIDS2017":
                scaler_path = r"C:\Users\amity\SentinelNet\models\cicids2017\scaler.pkl"
            else:
                st.warning(f"No scaler defined for dataset: {dataset}")
                return None
            
            if os.path.exists(scaler_path):
                self.scaler = joblib.load(scaler_path)
                st.success(f"✅ Scaler loaded successfully for {dataset}!")
                return True
            else:
                st.warning(f"Scaler file not found at: {scaler_path}")
                return False
        except Exception as e:
            st.error(f"Error loading scaler: {str(e)}")
            return False
        
    def load_model(self, model_path, dataset):
        """Load the trained model with flexible structure handling"""
        try:
            model_data = joblib.load(model_path)
            
            # Case 1: Model is a dictionary with expected keys
            if isinstance(model_data, dict):
                if 'model' in model_data:
                    self.model = model_data['model']
                    # Try to get scaler from model data, otherwise load separately
                    if 'scaler' in model_data:
                        self.scaler = model_data['scaler']
                    else:
                        self.load_scaler(dataset)
                    self.feature_names = model_data.get('feature_names', None)
                else:
                    # Try to find the model in the dictionary
                    for key, value in model_data.items():
                        if hasattr(value, 'predict') or hasattr(value, 'predict_proba'):
                            self.model = value
                            break
                    # Load scaler separately
                    self.load_scaler(dataset)
                    
            # Case 2: Model is directly the trained model
            elif hasattr(model_data, 'predict') or hasattr(model_data, 'predict_proba'):
                self.model = model_data
                # Load scaler separately
                self.load_scaler(dataset)
                self.feature_names = self.get_default_feature_names()
                
            # Case 3: Model is a tuple or list (common in some training scripts)
            elif isinstance(model_data, (tuple, list)):
                for item in model_data:
                    if hasattr(item, 'predict') or hasattr(item, 'predict_proba'):
                        self.model = item
                        break
                # Load scaler separately
                self.load_scaler(dataset)
                self.feature_names = self.get_default_feature_names()
            
            else:
                st.error(f"Unknown model structure: {type(model_data)}")
                return False
            
            # Validate that model was loaded
            if self.model is None:
                st.error("Could not find a valid model in the file")
                return False
                
            st.success(f"✅ Model loaded successfully! Type: {self.model.__class__.__name__}")
            
            # Set default feature names if none provided
            if self.feature_names is None:
                self.feature_names = self.get_default_feature_names()
                st.warning("Using default feature names")
                
            return True
            
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return False
    
    def get_default_feature_names(self):
        """Get default feature names for network intrusion detection"""
        return [
            'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
            'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
            'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
            'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
            'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate',
            'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
            'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
            'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
            'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
            'dst_host_rerror_rate', 'dst_host_srv_rerror_rate'
        ]
    
    def extract_features(self, packet):
        """Extract features from network packet for intrusion detection"""
        try:
            features = {}
            
            # Basic packet information
            features['duration'] = 0  # Placeholder for connection duration
            features['protocol_type'] = self.get_protocol_type(packet)
            features['service'] = self.get_service_type(packet)
            features['flag'] = self.get_connection_flag(packet)
            features['src_bytes'] = len(packet) if hasattr(packet, 'len') else 0
            features['dst_bytes'] = 0  # Would need bidirectional traffic
            
            # TCP specific features
            if TCP in packet:
                features['land'] = 1 if packet[IP].src == packet[IP].dst else 0
                features['wrong_fragment'] = 0  # Simplified
                features['urgent'] = packet[TCP].flags.U if hasattr(packet[TCP].flags, 'U') else 0
            else:
                features['land'] = 0
                features['wrong_fragment'] = 0
                features['urgent'] = 0
            
            # Connection features
            features['hot'] = self.calculate_hot_indicator(packet)
            features['num_failed_logins'] = 0  # Would need authentication data
            features['logged_in'] = 0  # Simplified
            features['num_compromised'] = 0
            features['root_shell'] = 0
            features['su_attempted'] = 0
            features['num_root'] = 0
            features['num_file_creations'] = 0
            features['num_shells'] = 0
            features['num_access_files'] = 0
            features['num_outbound_cmds'] = 0
            features['is_host_login'] = 0
            features['is_guest_login'] = 0
            
            # Count-based features (simplified)
            features['count'] = self.packets_captured % 100  # Simplified count
            features['srv_count'] = self.packets_captured % 50  # Simplified service count
            features['serror_rate'] = 0.0
            features['srv_serror_rate'] = 0.0
            features['rerror_rate'] = 0.0
            features['srv_rerror_rate'] = 0.0
            features['same_srv_rate'] = 1.0  # Simplified
            features['diff_srv_rate'] = 0.0
            features['srv_diff_host_rate'] = 0.0
            
            # Additional features for better detection
            features['dst_host_count'] = self.packets_captured % 100
            features['dst_host_srv_count'] = self.packets_captured % 50
            features['dst_host_same_srv_rate'] = 1.0
            features['dst_host_diff_srv_rate'] = 0.0
            features['dst_host_same_src_port_rate'] = 1.0
            features['dst_host_srv_diff_host_rate'] = 0.0
            features['dst_host_serror_rate'] = 0.0
            features['dst_host_srv_serror_rate'] = 0.0
            features['dst_host_rerror_rate'] = 0.0
            features['dst_host_srv_rerror_rate'] = 0.0
            
            return features
            
        except Exception as e:
            st.warning(f"Feature extraction error: {str(e)}")
            return None
    
    def get_protocol_type(self, packet):
        """Convert protocol to numerical value"""
        if TCP in packet:
            return 0  # TCP
        elif UDP in packet:
            return 1  # UDP
        elif ICMP in packet:
            return 2  # ICMP
        else:
            return 3  # Other
    
    def get_service_type(self, packet):
        """Get service type from port number"""
        try:
            if TCP in packet:
                port = packet[TCP].dport
            elif UDP in packet:
                port = packet[UDP].dport
            else:
                return 0  # Other service
            
            # Common service ports
            service_map = {
                80: 1,   # HTTP
                443: 2,  # HTTPS
                21: 3,   # FTP
                22: 4,   # SSH
                23: 5,   # Telnet
                25: 6,   # SMTP
                53: 7,   # DNS
                110: 8,  # POP3
                143: 9   # IMAP
            }
            return service_map.get(port, 0)  # 0 for other services
        except:
            return 0
    
    def get_connection_flag(self, packet):
        """Get connection flag"""
        try:
            if TCP in packet:
                flags = packet[TCP].flags
                if flags.S and not flags.A:  # SYN
                    return 0
                elif flags.S and flags.A:   # SYN-ACK
                    return 1
                elif flags.A and not flags.S: # ACK
                    return 2
                elif flags.F and flags.A:   # FIN-ACK
                    return 3
                elif flags.R:               # RST
                    return 4
            return 5  # Other
        except:
            return 5
    
    def calculate_hot_indicator(self, packet):
        """Calculate hot indicator based on packet characteristics"""
        # Simplified hot indicator calculation
        hot_score = 0
        if TCP in packet:
            if packet[TCP].flags.S:  # SYN flood potential
                hot_score += 1
            if packet[TCP].flags.R:  # RST attack potential
                hot_score += 1
        if len(packet) > 1000:  # Large packet
            hot_score += 1
        return min(hot_score, 10)  # Cap at 10
    
    def packet_handler(self, packet):
        """Handle captured packets and perform intrusion detection"""
        if not self.is_monitoring:
            return
        
        self.packets_captured += 1
        
        # Extract features from packet
        features = self.extract_features(packet)
        if features is None:
            return
        
        # Convert to DataFrame for model prediction
        feature_df = pd.DataFrame([features])
        
        try:
            # Ensure feature order matches training
            if self.feature_names:
                feature_df = feature_df.reindex(columns=self.feature_names, fill_value=0)
            
            # Scale features if scaler is available
            if self.scaler is not None:
                scaled_features = self.scaler.transform(feature_df)
            else:
                scaled_features = feature_df.values
                st.warning("Using unscaled features - scaler not available")
            
            # Make prediction
            if hasattr(self.model, 'predict'):
                prediction = self.model.predict(scaled_features)[0]
                
                # Get probabilities if available
                if hasattr(self.model, 'predict_proba'):
                    probability = self.model.predict_proba(scaled_features)[0]
                    confidence = max(probability)
                else:
                    confidence = 0.5  # Default confidence
            else:
                # Fallback for models without predict method
                prediction = 0
                confidence = 0.5
            
            # Store detection result
            detection = {
                'timestamp': datetime.now(),
                'packet_size': len(packet),
                'protocol': self.get_protocol_name(features['protocol_type']),
                'src_ip': packet[IP].src if IP in packet else 'N/A',
                'dst_ip': packet[IP].dst if IP in packet else 'N/A',
                'prediction': 'Intrusion' if prediction == 1 else 'Normal',
                'confidence': confidence,
                'risk_level': 'High' if confidence > 0.8 else 'Medium' if confidence > 0.6 else 'Low',
                'model_used': self.selected_model
            }
            
            self.detection_history.append(detection)
            
            # Update counters
            if prediction == 1:
                self.intrusion_count += 1
            else:
                self.normal_count += 1
                
        except Exception as e:
            st.warning(f"Prediction error: {str(e)}")
    
    def predict_csv(self, df):
        """Perform batch prediction on CSV data"""
        try:
            results = []
            
            # Ensure the dataframe has the required features
            if self.feature_names:
                # Align columns with feature names
                for feature in self.feature_names:
                    if feature not in df.columns:
                        df[feature] = 0  # Add missing features with default value
                
                # Reorder columns to match feature names
                df = df[self.feature_names]
            
            # Scale features if scaler is available
            if self.scaler is not None:
                features_scaled = self.scaler.transform(df)
            else:
                features_scaled = df.values
            
            # Make predictions
            predictions = self.model.predict(features_scaled)
            
            # Get probabilities if available
            if hasattr(self.model, 'predict_proba'):
                probabilities = self.model.predict_proba(features_scaled)
                confidences = np.max(probabilities, axis=1)
            else:
                confidences = [0.5] * len(predictions)
            
            # Create results
            for i, (prediction, confidence) in enumerate(zip(predictions, confidences)):
                result = {
                    'row_id': i + 1,
                    'prediction': 'Intrusion' if prediction == 1 else 'Normal',
                    'confidence': confidence,
                    'risk_level': 'High' if confidence > 0.8 else 'Medium' if confidence > 0.6 else 'Low'
                }
                results.append(result)
            
            return results
            
        except Exception as e:
            st.error(f"CSV prediction error: {str(e)}")
            return []
    
    def get_protocol_name(self, protocol_type):
        """Convert protocol type to name"""
        protocol_names = {0: 'TCP', 1: 'UDP', 2: 'ICMP', 3: 'Other'}
        return protocol_names.get(protocol_type, 'Unknown')
    
    def start_monitoring(self, interface=None):
        """Start network monitoring"""
        self.is_monitoring = True
        try:
            # Start packet capture in a separate thread
            sniff(prn=self.packet_handler, store=0, iface=interface, count=0)
        except Exception as e:
            st.error(f"Monitoring error: {str(e)}")
    
    def stop_monitoring(self):
        """Stop network monitoring"""
        self.is_monitoring = False

def get_available_models():
    """Get all available models from the models directory"""
    models = {
        'NSL-KDD': {},
        'CICIDS2017': {}
    }
    
    # NSL-KDD models
    nslkdd_path = r"C:\Users\amity\SentinelNet\models\nslkdd"
    nslkdd_models = {
        'Logistic Regression': 'logistic_regression.pkl',
        'Histogram Gradient Boosting': 'histgradientboosting.pkl',
        'Decision Tree': 'decision_tree.pkl',
        'Random Forest': 'random_forest.pkl'
    }
    
    # CICIDS2017 models
    cicids_path = r"C:\Users\amity\SentinelNet\models\cicids2017"
    cicids_models = {
        'Random Forest': 'random_forest.pkl',
        'Logistic Regression': 'logistic_regression.pkl',
        'Histogram Gradient Boosting': 'histogram_gradient_boosting.pkl',
        'Decision Tree': 'decision_tree.pkl'
    }
    
    # Check which models actually exist
    for model_name, model_file in nslkdd_models.items():
        model_path = os.path.join(nslkdd_path, model_file)
        if os.path.exists(model_path):
            models['NSL-KDD'][model_name] = model_path
    
    for model_name, model_file in cicids_models.items():
        model_path = os.path.join(cicids_path, model_file)
        if os.path.exists(model_path):
            models['CICIDS2017'][model_name] = model_path
    
    return models

def check_scaler_files():
    """Check if scaler files exist"""
    scalers = {}
    
    nslkdd_scaler = r"C:\Users\amity\SentinelNet\models\nslkdd\scaler.pkl"
    cicids_scaler = r"C:\Users\amity\SentinelNet\models\cicids2017\scaler.pkl"
    
    scalers['NSL-KDD'] = os.path.exists(nslkdd_scaler)
    scalers['CICIDS2017'] = os.path.exists(cicids_scaler)
    
    return scalers

def main():
    st.title("🛡️ Sentinel-Net: AI-Powered Network Intrusion Detection System")
    st.markdown("---")
    
    # Initialize detector
    if 'detector' not in st.session_state:
        st.session_state.detector = NetworkIntrusionDetector()
    
    detector = st.session_state.detector
    
    # Get available models
    available_models = get_available_models()
    
    # Check scaler files
    scaler_status = check_scaler_files()
    
    # Sidebar for model selection and configuration
    with st.sidebar:
        st.header("Configuration")
        
        # Detection Mode Selection
        detection_mode = st.radio(
            "Select Detection Mode",
            ["Live Network Monitoring", "CSV File Analysis"]
        )
        
        # Dataset selection
        dataset_option = st.selectbox(
            "Select Dataset",
            ["NSL-KDD", "CICIDS2017"]
        )
        
        # Display scaler status
        if dataset_option in scaler_status:
            if scaler_status[dataset_option]:
                st.success(f"✅ Scaler available for {dataset_option}")
            else:
                st.warning(f"⚠️ Scaler not found for {dataset_option}")
        
        # Model selection based on dataset
        if dataset_option in available_models and available_models[dataset_option]:
            model_names = list(available_models[dataset_option].keys())
            model_option = st.selectbox(
                "Select Algorithm",
                model_names
            )
            
            selected_path = available_models[dataset_option][model_option]
        else:
            st.error(f"No models found for {dataset_option}")
            selected_path = None
            model_option = None
        
        # Display model info
        if selected_path:
            st.info(f"Selected: {model_option} ({dataset_option})")
            
            # Add inspect button
            if st.button("Inspect Model Structure"):
                with st.spinner("Inspecting model..."):
                    model_data = detector.inspect_model(selected_path)
        
        # Load model button
        if st.button("Load Model", type="primary", disabled=selected_path is None):
            with st.spinner("Loading model and scaler..."):
                if detector.load_model(selected_path, dataset_option):
                    detector.selected_model = f"{model_option} ({dataset_option})"
                    detector.selected_dataset = dataset_option
                else:
                    st.error("❌ Failed to load model")
        
        st.markdown("---")
        
        if detection_mode == "Live Network Monitoring":
            # Network interface selection
            interfaces = psutil.net_if_addrs().keys()
            selected_interface = st.selectbox(
                "Network Interface",
                list(interfaces)
            )
            
            # Monitoring controls
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Start Monitoring", type="primary"):
                    if detector.model is None:
                        st.error("Please load a model first!")
                    else:
                        # Start monitoring in separate thread
                        monitor_thread = threading.Thread(
                            target=detector.start_monitoring,
                            args=(selected_interface,)
                        )
                        monitor_thread.daemon = True
                        monitor_thread.start()
                        st.success("🚀 Monitoring started!")
            
            with col2:
                if st.button("Stop Monitoring"):
                    detector.stop_monitoring()
                    st.warning("🛑 Monitoring stopped!")
        
        elif detection_mode == "CSV File Analysis":
            st.subheader("CSV File Upload")
            uploaded_file = st.file_uploader(
                "Upload network traffic CSV file", 
                type=['csv'],
                help="Upload a CSV file containing network traffic features for batch analysis"
            )
            
            if uploaded_file is not None:
                try:
                    # Read the CSV file
                    df = pd.read_csv(uploaded_file)
                    st.success(f"✅ CSV file loaded successfully! Shape: {df.shape}")
                    
                    # Show preview
                    with st.expander("Preview uploaded data"):
                        st.dataframe(df.head(10))
                    
                    # Analyze button
                    if st.button("Analyze CSV File", type="primary"):
                        if detector.model is None:
                            st.error("Please load a model first!")
                        else:
                            with st.spinner("Analyzing CSV file..."):
                                results = detector.predict_csv(df)
                                detector.csv_results = results
                                
                                if results:
                                    st.success(f"✅ Analysis complete! Processed {len(results)} records")
                                    
                                    # Display results
                                    results_df = pd.DataFrame(results)
                                    st.subheader("Analysis Results")
                                    st.dataframe(results_df)
                                    
                                    # Download results
                                    csv = results_df.to_csv(index=False)
                                    st.download_button(
                                        label="Download Results as CSV",
                                        data=csv,
                                        file_name="intrusion_detection_results.csv",
                                        mime="text/csv"
                                    )
                except Exception as e:
                    st.error(f"Error reading CSV file: {str(e)}")
        
        st.markdown("---")
        
        # Statistics
        st.subheader("Live Statistics")
        st.metric("Packets Captured", detector.packets_captured)
        st.metric("Intrusions Detected", detector.intrusion_count)
        st.metric("Normal Traffic", detector.normal_count)
        
        if detector.packets_captured > 0:
            intrusion_rate = (detector.intrusion_count / detector.packets_captured) * 100
            st.metric("Intrusion Rate", f"{intrusion_rate:.2f}%")
        
        # Model information
        if detector.model is not None:
            st.markdown("---")
            st.subheader("Model Info")
            st.write(f"**Loaded Model:** {detector.selected_model}")
            st.write(f"**Model Type:** {detector.model.__class__.__name__}")
            if detector.feature_names:
                st.write(f"**Features:** {len(detector.feature_names)}")
            if detector.scaler is not None:
                st.success("**Scaler:** ✅ Available and loaded")
            else:
                st.warning("**Scaler:** ⚠️ Not available (using raw features)")
    
    # Main content area
    if detection_mode == "Live Network Monitoring":
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("📊 Real-time Detection Dashboard")
            
            # Display current model info
            if detector.model is not None:
                st.success(f"🔍 Active Model: **{detector.selected_model}**")
                if detector.scaler is not None:
                    st.success("✅ Feature scaling enabled")
                else:
                    st.warning("⚠️ Feature scaling disabled - using raw features")
            else:
                st.warning("⚠️ No model loaded. Please select and load a model from the sidebar.")
            
            # Detection history table
            if detector.detection_history:
                recent_detections = detector.detection_history[-10:]  # Last 10 detections
                df_detections = pd.DataFrame(recent_detections)
                
                # Style the dataframe based on risk level
                def color_risk_level(val):
                    if val == 'High':
                        return 'color: red; font-weight: bold'
                    elif val == 'Medium':
                        return 'color: orange'
                    elif val == 'Low':
                        return 'color: green'
                    else:
                        return ''
                
                styled_df = df_detections.style.applymap(
                    color_risk_level, 
                    subset=['risk_level']
                )
                
                st.dataframe(styled_df, use_container_width=True)
            else:
                st.info("No detections yet. Start monitoring to see live network traffic analysis.")
        
        with col2:
            st.subheader("🚨 Threat Overview")
            
            # Threat indicators
            if detector.detection_history:
                recent_intrusions = [d for d in detector.detection_history[-20:] if d['prediction'] == 'Intrusion']
                
                if recent_intrusions:
                    st.error(f"🚨 {len(recent_intrusions)} recent intrusions detected!")
                    
                    # Show high confidence threats
                    high_threats = [d for d in recent_intrusions if d['confidence'] > 0.8]
                    if high_threats:
                        st.warning(f"⚠️ {len(high_threats)} high-confidence threats!")
                        
                    # Show threat by protocol
                    threat_protocols = pd.Series([d['protocol'] for d in recent_intrusions]).value_counts()
                    for protocol, count in threat_protocols.items():
                        st.write(f"• {protocol}: {count} threats")
                else:
                    st.success("✅ No recent intrusions detected")
            else:
                st.info("Waiting for network traffic...")
            
            # Quick actions
            st.markdown("---")
            st.subheader("Quick Actions")
            if st.button("Clear History"):
                detector.detection_history.clear()
                detector.packets_captured = 0
                detector.intrusion_count = 0
                detector.normal_count = 0
                st.success("History cleared!")
                st.rerun()
        
        # Charts and visualizations for live monitoring
        if detector.detection_history:
            st.markdown("---")
            st.subheader("📈 Detection Analytics")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                # Prediction distribution
                pred_counts = pd.Series([d['prediction'] for d in detector.detection_history]).value_counts()
                fig, ax = plt.subplots(figsize=(8, 6))
                colors = ['#ff6b6b' if pred == 'Intrusion' else '#51cf66' for pred in pred_counts.index]
                ax.pie(pred_counts.values, labels=pred_counts.index, autopct='%1.1f%%', 
                       startangle=90, colors=colors)
                ax.set_title('Traffic Classification')
                st.pyplot(fig)
            
            with col2:
                # Protocol distribution
                protocol_counts = pd.Series([d['protocol'] for d in detector.detection_history]).value_counts()
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.bar(protocol_counts.index, protocol_counts.values, color='#339af0')
                ax.set_xticklabels(protocol_counts.index, rotation=45)
                ax.set_title('Protocol Distribution')
                ax.set_ylabel('Count')
                st.pyplot(fig)
            
            with col3:
                # Risk level distribution
                risk_counts = pd.Series([d['risk_level'] for d in detector.detection_history]).value_counts()
                fig, ax = plt.subplots(figsize=(8, 6))
                colors = ['#ff6b6b', '#ffa94d', '#51cf66']  # Red, Orange, Green
                sns.barplot(x=risk_counts.index, y=risk_counts.values, ax=ax, 
                           palette=colors, order=['High', 'Medium', 'Low'])
                ax.set_title('Risk Level Distribution')
                ax.set_ylabel('Count')
                st.pyplot(fig)
    
    elif detection_mode == "CSV File Analysis":
        st.subheader("📁 CSV File Analysis")
        
        if detector.model is not None:
            st.success(f"🔍 Active Model: **{detector.selected_model}**")
            
            if detector.csv_results:
                results_df = pd.DataFrame(detector.csv_results)
                
                # Display summary statistics
                col1, col2, col3, col4 = st.columns(4)
                
                total_records = len(results_df)
                intrusions = len(results_df[results_df['prediction'] == 'Intrusion'])
                normal = len(results_df[results_df['prediction'] == 'Normal'])
                intrusion_rate = (intrusions / total_records) * 100 if total_records > 0 else 0
                
                with col1:
                    st.metric("Total Records", total_records)
                with col2:
                    st.metric("Intrusions", intrusions)
                with col3:
                    st.metric("Normal", normal)
                with col4:
                    st.metric("Intrusion Rate", f"{intrusion_rate:.2f}%")
                
                # Display results table
                st.subheader("Detailed Results")
                st.dataframe(results_df, use_container_width=True)
                
                # Visualization for CSV analysis
                st.subheader("Analysis Visualization")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    # Prediction distribution
                    pred_counts = results_df['prediction'].value_counts()
                    fig, ax = plt.subplots(figsize=(6, 6))
                    colors = ['#ff6b6b' if pred == 'Intrusion' else '#51cf66' for pred in pred_counts.index]
                    ax.pie(pred_counts.values, labels=pred_counts.index, autopct='%1.1f%%', 
                           startangle=90, colors=colors)
                    ax.set_title('Prediction Distribution')
                    st.pyplot(fig)
                
                with col2:
                    # Risk level distribution
                    risk_counts = results_df['risk_level'].value_counts()
                    fig, ax = plt.subplots(figsize=(6, 6))
                    colors = ['#ff6b6b', '#ffa94d', '#51cf66']  # Red, Orange, Green
                    sns.barplot(x=risk_counts.index, y=risk_counts.values, ax=ax, 
                               palette=colors, order=['High', 'Medium', 'Low'])
                    ax.set_title('Risk Level Distribution')
                    ax.set_ylabel('Count')
                    st.pyplot(fig)
        else:
            st.warning("⚠️ Please load a model first to analyze CSV files.")
    
    # Real-time updates for live monitoring
    if detection_mode == "Live Network Monitoring" and detector.is_monitoring:
        st.sidebar.info("🔴 Live monitoring active...")
        time.sleep(2)
        st.rerun()
    
    # About Me section at the bottom
    st.markdown("---")
    st.markdown(
        """
          <div style='text-align: center; padding: 20px; font-family: Arial, sans-serif;'>
        <h3 style='margin-bottom: 5px;'>Made with ❤️ by <a href='https://github.com/theamityadavv' target='_blank' style='color:inherit; text-decoration:none;'>Amityadav</a></h3>
        <!-- Horizontal line -->
        <hr style='width: 150px; border: 1px solid #ccc; margin: 10px auto;'>
        <p style='margin: 5px 0;'>
            Connect with me: 
            <a href='https://github.com/theamityadavv' target='_blank' style='color:inherit; text-decoration:none;'>GitHub</a> •
            <a href='https://www.linkedin.com/in/amityadavv/' target='_blank' style='color:inherit; text-decoration:none;'>LinkedIn</a> •
            <a href='https://theamityadavv.github.io/portfolio/' target='_blank' style='color:inherit; text-decoration:none;'>Portfolio</a> •
            <a href='mailto:amityadavv@outlook.in' style='color:inherit; text-decoration:none;'>Email</a>
        </p>
    </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()