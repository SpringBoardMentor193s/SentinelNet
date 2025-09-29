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
    plot_prediction_distribution, plot_metrics_comparison, create_attack_type_chart
)

# Page configuration
st.set_page_config(
    page_title="SentinelNet - Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title
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

# Dataset selection
dataset_choice = st.sidebar.selectbox(
    "📊 Select Dataset",
    ["NSL-KDD", "CICIDS2017"],
    help="Choose the dataset type for intrusion detection"
)

# Classification type
classification_type = st.sidebar.selectbox(
    "🎯 Classification Type",
    ["Binary Classification", "Multi-Class Classification"],
    help="Binary: Normal vs Attack | Multi-Class: Specific attack types"
)

# Model selection
model_choice = st.sidebar.selectbox(
    "🤖 Select Model",
    ["Logistic Regression", "Decision Tree", "Random Forest", "Gradient Boosting"],
    help="Choose the machine learning model for prediction"
)

st.sidebar.markdown("---")

# Display selected configuration
st.sidebar.markdown("### 📋 Current Configuration")
st.sidebar.info(f"""
**Dataset:** {dataset_choice}  
**Classification:** {classification_type}  
**Model:** {model_choice}
""")

# Helper function to load model
@st.cache_resource
def load_model_and_preprocessor(dataset, classification, model):
    """Load the trained model and preprocessor"""
    try:
        # Construct paths
        dataset_folder = dataset.lower().replace('-', '_')
        classification_folder = 'binary' if 'Binary' in classification else 'multiclass'
        model_name = model.lower().replace(' ', '_')
        
        model_path = f"models/{dataset_folder}_{classification_folder}/{model_name}.pkl"
        preprocessor_path = f"scalers/{dataset_folder}_preprocessor.pkl"
        
        # Load model
        if os.path.exists(model_path):
            loaded_model = joblib.load(model_path)
            st.sidebar.success("✅ Model loaded successfully!")
        else:
            st.sidebar.error(f"❌ Model file not found: {model_path}")
            return None, None
        
        # Load preprocessor
        preprocessor = DataPreprocessor(dataset_type=dataset_folder)
        if os.path.exists(preprocessor_path):
            preprocessor.load_preprocessor(preprocessor_path)
            st.sidebar.success("✅ Preprocessor loaded successfully!")
        else:
            st.sidebar.warning("⚠️ Preprocessor not found. Using default preprocessing.")
        
        return loaded_model, preprocessor
    
    except Exception as e:
        st.sidebar.error(f"❌ Error loading model: {str(e)}")
        return None, None

# Main content area tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📤 Upload & Predict", "📊 Results & Analytics", "ℹ️ About"])

# Tab 1: Home/Information
with tab1:
    st.markdown('<h2 class="sub-header">Welcome to SentinelNet</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 Purpose")
        st.write("""
        SentinelNet is an AI-powered Network Intrusion Detection System (NIDS) designed to 
        automatically identify and classify network attacks in real-time using advanced machine learning techniques.
        """)
    
    with col2:
        st.markdown("### 📚 Datasets")
        st.write("""
        - **NSL-KDD**: Legacy dataset with 41 features
        - **CICIDS2017**: Modern enterprise traffic with 78-83 features
        
        Both support binary and multi-class classification.
        """)
    
    with col3:
        st.markdown("### 🤖 Models")
        st.write("""
        - Logistic Regression
        - Decision Tree
        - Random Forest
        - Gradient Boosting
        
        All models are pre-trained and optimized.
        """)
    
    st.markdown("---")
    
    # Dataset comparison
    st.markdown("### 📊 Dataset Comparison")
    
    comparison_data = {
        "Attribute": ["Features", "Records", "Traffic Type", "Attack Categories", "Best Use Case"],
        "NSL-KDD": ["41", "~150,000", "Simulated", "4 Categories", "Research & Benchmarking"],
        "CICIDS2017": ["78-83", ">2.8 Million", "Enterprise-scale", "14+ Types", "Real-world Deployment"]
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    st.table(df_comparison)
    
    # Performance metrics
    st.markdown("### 🏆 Model Performance Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### NSL-KDD Binary Classification")
        perf_nsl = {
            "Model": ["Logistic Regression", "Decision Tree", "Random Forest", "Gradient Boosting"],
            "Accuracy": ["81.88%", "86.48%", "86.66%", "86.20%"],
            "F1-Score": ["0.82", "0.86", "0.86", "0.86"]
        }
        st.dataframe(pd.DataFrame(perf_nsl), hide_index=True)
    
    with col2:
        st.markdown("#### CICIDS2017 Binary Classification")
        perf_cicids = {
            "Model": ["Logistic Regression", "Decision Tree", "Random Forest", "Gradient Boosting"],
            "Accuracy": ["97.04%", "99.08%", "99.77%", "99.83%"],
            "F1-Score": ["0.97", "0.99", "1.00", "1.00"]
        }
        st.dataframe(pd.DataFrame(perf_cicids), hide_index=True)

# Tab 2: Upload and Predict
with tab2:
    st.markdown('<h2 class="sub-header">Upload Data & Make Predictions</h2>', unsafe_allow_html=True)
    
    # File upload
    st.markdown("### 📁 Upload Network Traffic Data")
    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=['csv'],
        help="Upload a CSV file containing network traffic features"
    )
    
    if uploaded_file is not None:
        try:
            # Load data
            df = pd.read_csv(uploaded_file)
            
            st.success(f"✅ File uploaded successfully! Shape: {df.shape}")
            
            # Display data preview
            st.markdown("### 👀 Data Preview")
            st.dataframe(df.head(10), use_container_width=True)
            
            # Data statistics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Records", df.shape[0])
            with col2:
                st.metric("Total Features", df.shape[1])
            with col3:
                st.metric("Missing Values", df.isnull().sum().sum())
            with col4:
                numeric_cols = df.select_dtypes(include=[np.number]).shape[1]
                st.metric("Numeric Features", numeric_cols)
            
            st.markdown("---")
            
            # Prediction button
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                predict_button = st.button("🚀 Run Prediction", type="primary", use_container_width=True)
            
            if predict_button:
                with st.spinner("🔄 Loading model and making predictions..."):
                    # Load model and preprocessor
                    model, preprocessor = load_model_and_preprocessor(
                        dataset_choice, classification_type, model_choice
                    )
                    
                    if model is not None and preprocessor is not None:
                        try:
                            # Preprocess data
                            X_processed, y_true = preprocessor.preprocess(df, is_training=False)
                            
                            # Make predictions
                            predictions = model.predict(X_processed)
                            prediction_proba = model.predict_proba(X_processed) if hasattr(model, 'predict_proba') else None
                            
                            # Store results in session state
                            st.session_state.predictions_made = True
                            st.session_state.prediction_results = {
                                'predictions': predictions,
                                'probabilities': prediction_proba,
                                'true_labels': y_true,
                                'data': df,
                                'processed_data': X_processed
                            }
                            
                            st.success("✅ Predictions completed successfully!")
                            st.balloons()
                            
                            # Display immediate results
                            st.markdown("### 🎯 Prediction Summary")
                            
                            # Convert predictions to readable format
                            if 'Binary' in classification_type:
                                pred_labels = ['Normal' if p == 0 else 'Attack' for p in predictions]
                            else:
                                dataset_type = 'nsl_kdd' if 'NSL-KDD' in dataset_choice else 'cicids'
                                pred_labels = [get_attack_category(p, dataset_type) for p in predictions]
                            
                            # Count predictions
                            unique, counts = np.unique(pred_labels, return_counts=True)
                            pred_summary = pd.DataFrame({'Type': unique, 'Count': counts, 'Percentage': (counts/len(pred_labels)*100).round(2)})
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.dataframe(pred_summary, hide_index=True, use_container_width=True)
                            with col2:
                                fig = plot_prediction_distribution(pred_labels)
                                st.plotly_chart(fig, use_container_width=True)
                            
                            # Show accuracy if true labels available
                            if y_true is not None:
                                accuracy = accuracy_score(y_true, predictions)
                                st.metric("🎯 Accuracy", f"{accuracy*100:.2f}%")
                            
                        except Exception as e:
                            st.error(f"❌ Error during prediction: {str(e)}")
                            st.exception(e)
                    else:
                        st.error("❌ Failed to load model. Please check if model files exist.")
        
        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")
    
    else:
        st.info("👆 Please upload a CSV file to begin")
        
        # Show sample data format
        with st.expander("📋 View Expected Data Format"):
            if 'NSL-KDD' in dataset_choice:
                st.markdown("""
                **NSL-KDD Dataset Format:**
                - Duration, protocol_type, service, flag, src_bytes, dst_bytes, etc.
                - Total: 41 features
                - Sample columns: `duration, protocol_type, service, flag, src_bytes, dst_bytes`
                """)
            else:
                st.markdown("""
                **CICIDS2017 Dataset Format:**
                - Flow Duration, Total Fwd Packets, Total Backward Packets, etc.
                - Total: 78-83 features
                - Sample columns: `Flow Duration, Total Fwd Packets, Flow Bytes/s`
                """)

# Tab 3: Results and Analytics
with tab3:
    st.markdown('<h2 class="sub-header">Detailed Results & Analytics</h2>', unsafe_allow_html=True)
    
    if st.session_state.predictions_made and st.session_state.prediction_results is not None:
        results = st.session_state.prediction_results
        predictions = results['predictions']
        probabilities = results['probabilities']
        y_true = results['true_labels']
        
        # Convert predictions to labels
        if 'Binary' in classification_type:
            pred_labels = ['Normal' if p == 0 else 'Attack' for p in predictions]
        else:
            dataset_type = 'nsl_kdd' if 'NSL-KDD' in dataset_choice else 'cicids'
            pred_labels = [get_attack_category(p, dataset_type) for p in predictions]
        
        # Section 1: Prediction Distribution
        st.markdown("### 📊 Prediction Distribution")
        col1, col2 = st.columns(2)
        
        with col1:
            fig_dist = plot_prediction_distribution(pred_labels)
            st.plotly_chart(fig_dist, use_container_width=True)
        
        with col2:
            fig_attack = create_attack_type_chart(pred_labels, dataset_type='nsl_kdd' if 'NSL-KDD' in dataset_choice else 'cicids')
            st.plotly_chart(fig_attack, use_container_width=True)
        
        st.markdown("---")
        
        # Section 2: Performance Metrics (if true labels available)
        if y_true is not None:
            st.markdown("### 📈 Performance Metrics")
            
            # Calculate metrics
            accuracy = accuracy_score(y_true, predictions)
            precision = precision_score(y_true, predictions, average='weighted', zero_division=0)
            recall = recall_score(y_true, predictions, average='weighted', zero_division=0)
            f1 = f1_score(y_true, predictions, average='weighted', zero_division=0)
            
            # Display metrics in columns
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("🎯 Accuracy", f"{accuracy*100:.2f}%")
            with col2:
                st.metric("🎖️ Precision", f"{precision:.4f}")
            with col3:
                st.metric("📊 Recall", f"{recall:.4f}")
            with col4:
                st.metric("⚖️ F1-Score", f"{f1:.4f}")
            
            st.markdown("---")
            
            # Confusion Matrix
            st.markdown("### 🔲 Confusion Matrix")
            fig_cm = plot_confusion_matrix(y_true, predictions, title=f"{model_choice} - Confusion Matrix")
            st.plotly_chart(fig_cm, use_container_width=True)
            
            st.markdown("---")
            
            # ROC Curve (for binary classification)
            if 'Binary' in classification_type and probabilities is not None:
                st.markdown("### 📉 ROC Curve")
                # Get probability for positive class
                y_true_binary = (y_true != 0).astype(int) if not isinstance(y_true[0], str) else y_true
                y_proba = probabilities[:, 1] if probabilities.shape[1] == 2 else probabilities[:, 0]
                fig_roc = plot_roc_curve(y_true_binary, y_proba, title=f"{model_choice} - ROC Curve")
                st.plotly_chart(fig_roc, use_container_width=True)
        
        else:
            st.info("ℹ️ True labels not available in uploaded data. Performance metrics cannot be calculated.")
        
        st.markdown("---")
        
        # Section 3: Detailed Predictions Table
        st.markdown("### 📋 Detailed Predictions")
        
        # Create results dataframe
        results_df = results['data'].copy()
        results_df['Predicted_Label'] = pred_labels
        
        if probabilities is not None:
            if 'Binary' in classification_type:
                results_df['Confidence'] = probabilities.max(axis=1)
            else:
                results_df['Confidence'] = probabilities.max(axis=1)
        
        if y_true is not None:
            results_df['True_Label'] = y_true
            results_df['Correct'] = (predictions == y_true)
        
        # Show interactive table
        st.dataframe(results_df, use_container_width=True, height=400)
        
        # Download button
        csv = results_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Predictions as CSV",
            data=csv,
            file_name=f"sentinelnet_predictions_{dataset_choice}_{classification_type}.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        st.markdown("---")
        
        # Section 4: Feature Importance (for tree-based models)
        if model_choice in ["Decision Tree", "Random Forest", "Gradient Boosting"]:
            model, _ = load_model_and_preprocessor(dataset_choice, classification_type, model_choice)
            if model is not None and hasattr(model, 'feature_importances_'):
                st.markdown("### 🌳 Feature Importance")
                
                feature_names = results['processed_data'].columns
                importances = model.feature_importances_
                importance_dict = dict(zip(feature_names, importances))
                
                fig_importance = plot_feature_importance(importance_dict, top_n=20)
                st.plotly_chart(fig_importance, use_container_width=True)
    
    else:
        st.info("ℹ️ No predictions available. Please upload data and run predictions in the 'Upload & Predict' tab.")

# Tab 4: About
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
        
        ### 🔬 Methodology
        
        1. **Data Preprocessing**: Feature scaling, encoding, and handling missing values
        2. **Model Training**: Pre-trained models on NSL-KDD and CICIDS2017 datasets
        3. **Prediction**: Real-time classification of network traffic
        4. **Evaluation**: Comprehensive metrics including accuracy, precision, recall, F1-score
        
        ### 📊 Performance Highlights
        
        - **NSL-KDD**: Up to 86.66% accuracy with Random Forest
        - **CICIDS2017**: Up to 99.83% accuracy with Gradient Boosting
        - **Fast Inference**: Real-time predictions on large datasets
        - **High Precision**: Minimized false positives for production deployment
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
        
        ### 📄 Documentation
        
        Full research paper and technical documentation available in the project repository.
        """)
    
    st.markdown("---")
    
    # Attack Type Information
    st.markdown("### 🎯 Attack Type Categories")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### NSL-KDD Attack Types
        
        **DoS (Denial of Service)**
        - Neptune, Smurf, Pod, Teardrop
        - Goal: Overwhelm system resources
        
        **Probe**
        - Portsweep, Ipsweep, Nmap, Satan
        - Goal: Gather information about network
        
        **R2L (Remote to Local)**
        - FTP Write, Guess Password, Warezmaster
        - Goal: Unauthorized access from remote machine
        
        **U2R (User to Root)**
        - Buffer Overflow, Rootkit, Loadmodule
        - Goal: Gain root access
        """)
    
    with col2:
        st.markdown("""
        #### CICIDS2017 Attack Types
        
        **DDoS Attacks**
        - Hulk, GoldenEye, Slowloris, Slowhttptest
        - Distributed denial of service
        
        **Brute Force**
        - FTP-Patator, SSH-Patator
        - Password guessing attacks
        
        **Web Attacks**
        - SQL Injection, XSS
        - Application layer attacks
        
        **Others**
        - Botnet, Infiltration, PortScan, Heartbleed
        - Various modern attack vectors
        """)
    
    st.markdown("---")
    
    # Usage Instructions
    with st.expander("📖 How to Use This Application"):
        st.markdown("""
        ### Step-by-Step Guide
        
        1. **Select Configuration** (Sidebar)
           - Choose dataset type (NSL-KDD or CICIDS2017)
           - Select classification type (Binary or Multi-Class)
           - Pick ML model for prediction
        
        2. **Upload Data** (Upload & Predict Tab)
           - Click "Browse files" and select your CSV file
           - Ensure data format matches selected dataset
           - Review data preview and statistics
        
        3. **Run Prediction**
           - Click "Run Prediction" button
           - Wait for model to process data
           - View immediate prediction summary
        
        4. **Analyze Results** (Results & Analytics Tab)
           - Review detailed metrics and visualizations
           - Examine confusion matrix and ROC curves
           - Download predictions as CSV file
        
        5. **Interpret Results**
           - Check accuracy and performance metrics
           - Identify attack types in your network traffic
           - Use insights for security decision-making
        
        ### Data Format Requirements
        
        **NSL-KDD**: Must contain 41 features including protocol_type, service, flag, etc.
        
        **CICIDS2017**: Must contain 78-83 features including Flow Duration, packet statistics, etc.
        
        ### Tips for Best Results
        
        - Ensure data quality (no corrupted values)
        - Use appropriate dataset type
        - Try multiple models for comparison
        - Review feature importance for insights
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p><strong>SentinelNet v1.0</strong> | Developed for Infosys Springboard | 2024</p>
        <p>For technical support or questions, please contact the development team.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer for all pages
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1rem; background-color: #f0f2f6; border-radius: 0.5rem;'>
    <p style='margin: 0; color: #666;'>
        🛡️ <strong>SentinelNet</strong> - Protecting Networks with AI | 
        Built with Streamlit | © 2024 Infosys Springboard
    </p>
</div>
""", unsafe_allow_html=True)