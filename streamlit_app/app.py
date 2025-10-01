import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from pathlib import Path
import plotly.graph_objects as go
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Import custom utilities
from utils.preprocessing import DataPreprocessor, get_attack_category
from utils.visualization import (
    plot_confusion_matrix, plot_roc_curve, plot_feature_importance,
    plot_prediction_distribution, create_attack_type_chart
)

# Page configuration 
st.set_page_config(
    page_title="SentinelNet - Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with smaller footer
st.markdown("""
    <style>
    .main { min-height: 100vh; display: flex; flex-direction: column; }
    .main-header { font-size: 3.5rem; font-weight: bold; color: #1f77b4; text-align: center; margin-bottom: 2rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); }
    .sub-header { font-size: 2rem; color: #ff7f0e; margin-top: 2rem; margin-bottom: 1rem; font-weight: 600; }
    .stButton>button { width: 100%; background-color: #1f77b4; color: white; font-weight: bold; font-size: 1.1rem; padding: 0.75rem; }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p { font-size: 1.3rem; font-weight: 600; }
    h3 { font-size: 1.5rem !important; }
    .footer-container { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 0.5rem; text-align: center; margin-top: auto; margin-bottom: 0.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: sticky; bottom: 0; z-index: 999; }
    .footer-text { color: white; font-size: 1rem; font-weight: 500; margin: 0.25rem 0; }
    .footer-subtext { color: rgba(255,255,255,0.9); font-size: 0.8rem; margin: 0.15rem 0; }
    .feature-highlight { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 1.5rem; border-radius: 1rem; color: white; text-align: center; margin: 1rem 0; }
    .status-success { background-color: #d4edda; border: 1px solid #c3e6cb; color: #155724; padding: 1rem; border-radius: 0.5rem; margin: 0.5rem 0; }
    .content-wrapper { flex: 1; padding-bottom: 1rem; }
    </style>
""", unsafe_allow_html=True)

# Title with content wrapper
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">🛡️ SentinelNet - AI-Powered Network Intrusion Detection System</h1>', unsafe_allow_html=True)
st.markdown("---")

# Initialize session state
if 'predictions_made' not in st.session_state:
    st.session_state.predictions_made = False
if 'prediction_results' not in st.session_state:
    st.session_state.prediction_results = None

# Sidebar configuration
st.sidebar.title("⚙️ Configuration")
st.sidebar.markdown("---")

dataset_choice = st.sidebar.selectbox(
    "📊 Select Dataset",
    ["NSL-KDD", "CICIDS2017"],
    help="Choose the dataset type for intrusion detection"
)

classification_type = st.sidebar.selectbox(
    "🎯 Classification Type",
    ["Binary Classification", "Multi-Class Classification"],
    help="Binary: Normal vs Attack | Multi-Class: Specific attack types"
)

model_choice = st.sidebar.selectbox(
    "🤖 Select Model",
    ["Logistic Regression", "Decision Tree", "Random Forest", "Gradient Boosting"],
    help="Choose the machine learning model for prediction"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Current Configuration")
st.sidebar.info(f"""
**Dataset:** {dataset_choice}  
**Classification:** {classification_type}  
**Model:** {model_choice}
""")
debug_mode = st.sidebar.checkbox("🔧 Debug Mode", value=False, help="Show detailed file paths and debugging info")

# Helper function to load model
@st.cache_resource
def load_model_and_preprocessor(dataset, classification, model):
    """Load the trained model and preprocessor"""
    try:
        if 'NSL-KDD' in dataset:
            dataset_folder, dataset_type = 'nslkdd', 'nsl_kdd'
        else:
            dataset_folder, dataset_type = 'cicids', 'cicids'
        
        classification_folder = 'binary' if 'Binary' in classification else 'multiclass'
        model_name = model.lower().replace(' ', '_')
        
        model_path = f"streamlit_app/models/{dataset_folder}_{classification_folder}/{model_name}.pkl"
        preprocessor_path = f"streamlit_app/scalers/{dataset_type}_preprocessor.pkl"
        
        if not os.path.exists(model_path) or not os.path.exists(preprocessor_path):
            st.sidebar.error(f"❌ Model or Preprocessor file not found.")
            if debug_mode:
                st.sidebar.write(f"Model path: {model_path} (Exists: {os.path.exists(model_path)})")
                st.sidebar.write(f"Preprocessor path: {preprocessor_path} (Exists: {os.path.exists(preprocessor_path)})")
            return None, None
            
        loaded_model = joblib.load(model_path)
        preprocessor = DataPreprocessor(dataset_type=dataset_type).load_preprocessor(preprocessor_path)
        st.sidebar.success("✅ Model & Preprocessor loaded!")
        return loaded_model, preprocessor
    
    except Exception as e:
        st.sidebar.error(f"❌ Error loading files: {str(e)}")
        if debug_mode: st.sidebar.exception(e)
        return None, None

# Main content area tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📤 Upload & Predict", "📊 Results & Analytics", "ℹ️ About"])

with tab1:
    st.markdown('<h2 class="sub-header">Welcome to SentinelNet</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="feature-highlight">
        <h3>🚀 Advanced AI-Powered Network Security</h3>
        <p>Detect and classify network intrusions in real-time using state-of-the-art machine learning algorithms</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🎯 Purpose")
        st.write("SentinelNet is an AI-powered Network Intrusion Detection System (NIDS) designed to automatically identify and classify network attacks in real-time using advanced machine learning techniques.")
    with col2:
        st.markdown("### 📚 Datasets")
        st.write("- **NSL-KDD**: Legacy dataset with 41 features\n- **CICIDS2017**: Modern enterprise traffic with 78-83 features\n\nBoth support binary and multi-class classification.")
    with col3:
        st.markdown("### 🤖 Models")
        st.write("- Logistic Regression\n- Decision Tree\n- Random Forest\n- Gradient Boosting\n\nAll models are pre-trained and optimized.")
    
    st.markdown("---")
    st.markdown("### 🚀 Quick Start Guide")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Step 1: Configure\n1. Select dataset type\n2. Choose classification type\n3. Pick an ML model")
        st.markdown("#### Step 2: Upload\n1. Go to 'Upload & Predict'\n2. Upload your CSV file\n3. Review data preview")
    with col2:
        st.markdown("#### Step 3: Predict\n1. Click 'Run Prediction'\n2. View summary\n3. Check distribution")
        st.markdown("#### Step 4: Analyze\n1. Go to 'Results & Analytics'\n2. Review detailed metrics\n3. Download results")
    
    st.markdown("---")
    st.markdown("### 🏆 Model Performance Summary")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### NSL-KDD Binary Classification")
        perf_nsl = {"Model": ["Logistic Regression", "Decision Tree", "Random Forest", "Gradient Boosting"], "Accuracy": ["81.88%", "86.48%", "86.66%", "86.20%"], "F1-Score": ["0.82", "0.86", "0.86", "0.86"]}
        st.dataframe(pd.DataFrame(perf_nsl), hide_index=True, use_container_width=True)
    with col2:
        st.markdown("#### CICIDS2017 Binary Classification")
        perf_cicids = {"Model": ["Logistic Regression", "Decision Tree", "Random Forest", "Gradient Boosting"], "Accuracy": ["97.04%", "99.08%", "99.77%", "99.83%"], "F1-Score": ["0.97", "0.99", "1.00", "1.00"]}
        st.dataframe(pd.DataFrame(perf_cicids), hide_index=True, use_container_width=True)
    
    st.markdown("---")
    st.markdown("""<div class="status-success"><strong>✅ System Status: Ready</strong><br>All models loaded and system ready for predictions. Upload your data to get started!</div>""", unsafe_allow_html=True)

with tab2:
    st.markdown('<h2 class="sub-header">Upload Data & Make Predictions</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'], help="Upload a CSV file with network traffic features")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"✅ File uploaded successfully! Shape: {df.shape}")
            st.markdown("### 👀 Data Preview")
            # Show only first 10 rows to avoid size issues
            st.dataframe(df.head(10), use_container_width=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                predict_button = st.button("🚀 Run Prediction", type="primary", use_container_width=True)
            
            if predict_button:
                try:
                    with st.spinner("🔄 Loading model and making predictions..."):
                        model, preprocessor = load_model_and_preprocessor(dataset_choice, classification_type, model_choice)
                        if model and preprocessor:
                            X_processed, y_true = preprocessor.preprocess(df, is_training=False)
                            predictions = model.predict(X_processed)
                            prediction_proba = model.predict_proba(X_processed) if hasattr(model, 'predict_proba') else None
                            
                            st.session_state.predictions_made = True
                            st.session_state.prediction_results = {
                                'predictions': predictions, 'probabilities': prediction_proba, 'true_labels': y_true,
                                'data': df, 'processed_data': X_processed
                            }
                            st.success("✅ Predictions completed successfully!")
                            st.balloons()

                except (RuntimeError, ValueError) as e:
                    st.error(f"❌ A critical error occurred: {e}")
                    st.info("This might mean the saved model files (.pkl) are incompatible. Please try regenerating them.")
                
                if st.session_state.get('predictions_made'):
                    st.markdown("### 🎯 Prediction Summary")
                    results = st.session_state.prediction_results
                    dataset_type = 'nsl_kdd' if 'NSL-KDD' in dataset_choice else 'cicids'
                    
                    if 'Binary' in classification_type:
                        pred_labels = ['Attack' if p == 1 else 'Normal' for p in results['predictions']]
                    else:
                        pred_labels = [get_attack_category(p, dataset_type) for p in results['predictions']]
                    
                    unique, counts = np.unique(pred_labels, return_counts=True)
                    pred_summary = pd.DataFrame({'Type': unique, 'Count': counts, 'Percentage': (counts/len(pred_labels)*100).round(2)})
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.dataframe(pred_summary, hide_index=True, use_container_width=True)
                    with col2:
                        fig = plot_prediction_distribution(pred_labels)
                        st.plotly_chart(fig, use_container_width=True, key="dist_summary_chart")

        except Exception as e:
            st.error(f"❌ Error processing file: {str(e)}")
            if debug_mode: st.exception(e)

with tab3:
    st.markdown('<h2 class="sub-header">Detailed Results & Analytics</h2>', unsafe_allow_html=True)
    
    if st.session_state.predictions_made and st.session_state.prediction_results:
        results = st.session_state.prediction_results
        predictions = results['predictions']
        probabilities = results['probabilities']
        y_true = results['true_labels']
        dataset_type = 'nsl_kdd' if 'NSL-KDD' in dataset_choice else 'cicids'
        
        if 'Binary' in classification_type:
            pred_labels = ['Attack' if p == 1 else 'Normal' for p in predictions]
        else:
            pred_labels = [get_attack_category(p, dataset_type) for p in predictions]
        
        st.markdown("### 📊 Prediction Distribution")
        col1, col2 = st.columns(2)
        with col1:
            fig_dist = plot_prediction_distribution(pred_labels)
            st.plotly_chart(fig_dist, use_container_width=True, key="dist_results_chart")
        with col2:
            fig_attack = create_attack_type_chart(pred_labels, dataset_type=dataset_type)
            st.plotly_chart(fig_attack, use_container_width=True, key="attack_type_chart")
        
        st.markdown("---")

        if y_true is not None and not y_true.empty:
            st.markdown("### 📈 Performance Metrics")

            y_true_numeric = y_true.copy()
            if pd.api.types.is_string_dtype(y_true_numeric):
                y_true_numeric = y_true_numeric.str.lower()
                if 'Binary' in classification_type:
                    normal_label = 'benign' if dataset_type == 'cicids' else 'normal'
                    y_true_numeric = y_true_numeric.apply(lambda x: 0 if x == normal_label else 1)
                else:
                    y_true_categories = y_true_numeric.apply(lambda x: get_attack_category(x, dataset_type))
                    if dataset_type == 'nsl_kdd':
                        label_mapping = {'Normal': 0, 'DoS': 1, 'Probe': 2, 'R2L': 3, 'U2R': 4}
                        y_true_numeric = y_true_categories.map(label_mapping)

            try:
                accuracy = accuracy_score(y_true_numeric, predictions)
                precision = precision_score(y_true_numeric, predictions, average='weighted', zero_division=0)
                recall = recall_score(y_true_numeric, predictions, average='weighted', zero_division=0)
                f1 = f1_score(y_true_numeric, predictions, average='weighted', zero_division=0)

                col1, col2, col3, col4 = st.columns(4)
                with col1: st.metric("🎯 Accuracy", f"{accuracy*100:.2f}%")
                with col2: st.metric("🎖️ Precision", f"{precision:.4f}")
                with col3: st.metric("📊 Recall", f"{recall:.4f}")
                with col4: st.metric("⚖️ F1-Score", f"{f1:.4f}")
                
                st.markdown("---")
                st.markdown("### 🔲 Confusion Matrix")
                fig_cm = plot_confusion_matrix(y_true_numeric, predictions, title=f"{model_choice} - Confusion Matrix")
                st.plotly_chart(fig_cm, use_container_width=True, key="confusion_matrix_chart")
                
                if 'Binary' in classification_type and probabilities is not None:
                    st.markdown("---")
                    st.markdown("### 📉 ROC Curve")
                    y_proba = probabilities[:, 1] if probabilities.shape[1] > 1 else probabilities[:, 0]
                    fig_roc = plot_roc_curve(y_true_numeric, y_proba, title=f"{model_choice} - ROC Curve")
                    st.plotly_chart(fig_roc, use_container_width=True, key="roc_curve_chart")
            
            except Exception as e:
                st.error(f"Error calculating metrics: {e}")

        st.markdown("---")
        st.markdown("### 📋 Detailed Predictions")
        
        # FIX: Sample data if too large
        results_df = results['data'].copy()
        results_df['Predicted_Label'] = pred_labels
        if probabilities is not None: 
            results_df['Confidence'] = probabilities.max(axis=1)
        if y_true is not None:
            results_df['True_Label'] = y_true
        
        total_rows = len(results_df)
        
        # Show warning if dataset is large
        if total_rows > 10000:
            st.warning(f"⚠️ Large dataset detected ({total_rows:,} rows). Showing sample of 10,000 rows for display. Full data available in download.")
            display_df = results_df.sample(n=min(10000, total_rows), random_state=42)
            st.info(f"Displaying random sample of {len(display_df):,} rows out of {total_rows:,} total")
        else:
            display_df = results_df
        
        # Display with pagination-friendly height
        st.dataframe(display_df, use_container_width=True, height=400)
        
        # Download button for FULL dataset
        st.markdown("#### 📥 Download Full Results")
        csv = results_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=f"📥 Download All {total_rows:,} Predictions as CSV",
            data=csv,
            file_name=f"sentinelnet_predictions_{total_rows}_rows.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        if model_choice in ["Decision Tree", "Random Forest", "Gradient Boosting"]:
            st.markdown("---")
            st.markdown("### 🌳 Feature Importance")
            model, _ = load_model_and_preprocessor(dataset_choice, classification_type, model_choice)
            if model and hasattr(model, 'feature_importances_'):
                feature_names = results['processed_data'].columns
                importances = model.feature_importances_
                importance_dict = dict(zip(feature_names, importances))
                fig_importance = plot_feature_importance(importance_dict, top_n=20)
                st.plotly_chart(fig_importance, use_container_width=True, key="feature_importance_chart")
    else:
        st.info("ℹ️ No predictions available. Upload data in the 'Upload & Predict' tab.")

with tab4:
    st.markdown('<h2 class="sub-header">About SentinelNet</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📖 Project Overview
        
        **SentinelNet** is an AI-powered Network Intrusion Detection System (NIDS) developed as part of the 
        Infosys Springboard internship program. The system leverages advanced machine learning algorithms 
        to detect and classify network attacks in real-time.
        
        ### 🎯 Key Features
        
        - **Multi-Dataset Support**: Compatible with NSL-KDD and CICIDS2017 datasets
        - **Flexible Classification**: Binary (Normal vs Attack) and Multi-Class (Specific attack types)
        - **Multiple ML Models**: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting
        - **Real-Time Predictions**: Upload network traffic data and get instant predictions
        - **Comprehensive Analytics**: Detailed performance metrics, confusion matrices, and visualizations
        - **Easy to Use**: User-friendly interface with minimal configuration required
        """)
    
    with col2:
        st.markdown("""
        ### 👥 Team
        
        **Author**: Upasana Prabhakar  
        **Mentor**: Dr. N Jagan Mohan  
        **Organization**: Infosys Springboard
        
        ### 📚 Datasets Used
        
        **NSL-KDD**
        - 41 features
        - ~150,000 records
        - 4 attack categories
        
        **CICIDS2017**
        - 78-83 features
        - >2.8M records
        - 14+ attack types
        
        ### 🤖 ML Models
        
        1. Logistic Regression
        2. Decision Tree
        3. Random Forest
        4. Gradient Boosting
        """)

# Close content wrapper and add footer
st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div class="footer-container">
    <p class="footer-text">🛡️ <strong>SentinelNet</strong> - Protecting Networks with AI</p>
    <p class="footer-subtext">Built with Streamlit | Powered by Machine Learning</p>
    <p class="footer-subtext">© 2025 Infosys Springboard | Developed by Upasana Prabhakar</p>
</div>
""", unsafe_allow_html=True)