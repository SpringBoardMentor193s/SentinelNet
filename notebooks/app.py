import streamlit as st
import pandas as pd
import joblib
import pickle
import numpy as np 
import os
import warnings # Added for warning suppression
from xgboost import XGBClassifier # Added for XGBClassifier definition

# Suppress scikit-learn UserWarning about missing feature names
warnings.filterwarnings(
    "ignore", 
    message="X does not have valid feature names, but*", 
    category=UserWarning
)

# ---------------------------
# Dataset + Models Config
# ---------------------------
MODEL_CONFIGS = {
    "NSL-KDD (Binary)": {
        "models": {
            "Logistic Regression": "model/nslkdd_bin_logisticregression.pkl",
            "Random Forest": "model/nslkdd_bin_randomforest.pkl",
            "XGBoost": "model/nslkdd_bin_xgboost.pkl",
            "SVM": "model/nslkdd_bin_svm.pkl"
        },
        "scaler_path": "model/nslkdd_bin_scaler.pkl",
        "features_path": "model/nslkdd_bin_features.pkl",
        "protocol_map": {"TCP (1)": 1, "UDP (2)": 2, "ICMP (0)": 0},
        "flag_map": {"SF": 9, "S0": 5, "REJ": 1, "RSTO": 4, "RSTR": 3, "SH": 2,
                     "OTH": 0, "S3": 6, "S2": 7, "S1": 8, "RSTOS0": 10},
        "label_map": {0: "Normal (0)", 1: "Attack (1)"}, # Binary
    },
    "NSL-KDD (Multi-class)": {
        "models": {
            "Logistic Regression": "model/nsl_multi_logreg.pkl",
            "Random Forest": "model/nsl_multi_rf.pkl",
            "XGBoost": "model/nsl_multi_xgb.pkl",
        },
        "scaler_path": "model/nsl_multi_scaler.pkl",
        "features_path": "model/nsl_multi_features.pkl",
        "protocol_map": {"TCP (1)": 1, "UDP (2)": 2, "ICMP (0)": 0},
        "flag_map": {"SF": 9, "S0": 5, "REJ": 1, "RSTO": 4, "RSTR": 3, "SH": 2,
                     "OTH": 0, "S3": 6, "S2": 7, "S1": 8, "RSTOS0": 10},
        "label_map": {
            0: "back", 1: "buffer_overflow", 2: "ftp_write", 3: "guess_passwd", 
            4: "imap", 5: "ipsweep", 6: "land", 7: "loadmodule", 8: "multihop", 
            9: "neptune", 10: "nmap", 11: "normal", 12: "perl", 13: "phf", 
            14: "pod", 15: "portsweep", 16: "rootkit", 17: "satan", 18: "smurf", 
            19: "teardrop", 20: "warezclient", 21: "warezmaster"
        },
    },
    "CICIDS (Binary)": {
        "models": {
            "Logistic Regression": "model/cicids_bin_logisticregression.pkl",
            "Random Forest": "model/cicids_bin_randomforest.pkl",
            "XGBoost": "model/cicids_bin_xgboost.pkl",
            "KNN": "model/cicids_bin_knn.pkl"
        },
        "scaler_path": "model/cicids_bin_scaler.pkl",
        "features_path": "model/cicids_bin_features.pkl",
        "protocol_map": {},
        "flag_map": {},
        "label_map": {0: "BENIGN (0)", 1: "ATTACK (1)"}, # Binary
    },
    "CICIDS (Multi-class)": {
        "models": {
            "Logistic Regression": "model/cicids_multi_logisticregression.pkl",
            "Random Forest": "model/cicids_multi_randomforest.pkl",
            "XGBoost": "model/cicids_multi_xgboost.pkl",
        },
        "scaler_path": "model/cicids_multi_scaler.pkl",
        "features_path": "model/cicids_multi_features.pkl",
        "protocol_map": {},
        "flag_map": {},
        "label_map": {
            0: "BENIGN", 1: "DDoS", 2: "DoS Hulk", 3: "PortScan", 
            4: "Web Attack - Brute Force", 5: "Web Attack - XSS" 
        },
    }
}

# ---------------------------
# Cache Loader
# ---------------------------
@st.cache_resource
def load_assets(model_path, scaler_path, features_path):
    """Loads the ML model, scaler, and feature names."""
    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        with open(features_path, "rb") as f:
            feature_names = pickle.load(f)
        return model, scaler, feature_names
    except Exception as e:
        st.error(f"Error loading assets from {model_path} or related files. Please ensure all model/scaler/feature files are present. Details: {e}")
        return None, None, None

# ---------------------------
# Prediction Utility
# ---------------------------
def make_prediction(model, scaler, feature_names, input_data, label_map=None):
    """Makes a prediction and returns the final label and probabilities."""
    # Convert input list to DataFrame (ensures feature names are present)
    input_df = pd.DataFrame([input_data], columns=feature_names)
    
    # Scale the input
    scaled_input = scaler.transform(input_df)
    
    # Make prediction
    pred_numeric = model.predict(scaled_input)[0]

    # Convert prediction to standard Python int if it's a NumPy type
    if isinstance(pred_numeric, np.generic):
        pred_numeric = pred_numeric.item()

    # Convert numeric prediction to string label if map is provided
    pred_final = label_map.get(pred_numeric, f"Unknown Label ({pred_numeric})") if label_map else pred_numeric

    # Get probabilities
    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(scaled_input)[0]
        
    return pred_final, proba, pred_numeric

# ---------------------------
# Streamlit Layout
# ---------------------------
st.set_page_config(page_title="🛡️ Unified IDS GUI", layout="wide")
st.title("🛡️ Intrusion Detection System")
st.sidebar.header("Configuration")

# Dataset & Model selection
dataset_choice = st.sidebar.selectbox("Choose Dataset", list(MODEL_CONFIGS.keys()))
config = MODEL_CONFIGS[dataset_choice]
ml_choice = st.sidebar.selectbox("Choose Machine Learning Model", list(config["models"].keys()))
model_path = config["models"][ml_choice]

# Load assets
model, scaler, feature_names = load_assets(model_path, config["scaler_path"], config["features_path"])
if model is None:
    st.stop()
st.success(f"✅ Loaded **{ml_choice}** model for **{dataset_choice}**")

# Input Mode
input_mode = st.sidebar.radio("Input Mode", ["Live Input", "Upload CSV"])

input_df = None
if input_mode == "Live Input":
    st.header(f"Define Features for {dataset_choice}")
    with st.form("live_form"):
        input_values = {}

        if dataset_choice.startswith("NSL-KDD"):
            # --- NSL-KDD Feature Inputs ---
            col1, col2 = st.columns(2)
            input_values["duration"] = col1.number_input("Duration", min_value=0, max_value=50000, value=0)
            proto = col2.selectbox("Protocol", options=list(config["protocol_map"].keys()))
            input_values["protocol_type"] = config["protocol_map"][proto]

            col3, col4 = st.columns(2)
            input_values["src_bytes"] = col3.number_input("Source Bytes", min_value=0, value=0)
            input_values["dst_bytes"] = col4.number_input("Destination Bytes", min_value=0, value=0)

            flag_choice = st.selectbox("Flag", options=list(config["flag_map"].keys()))
            input_values["flag"] = config["flag_map"][flag_choice]

            # NSL extra features (simplified list for GUI)
            input_values["hot"] = st.number_input("Hot", min_value=0, value=0)
            input_values["num_failed_logins"] = st.number_input("Num Failed Logins", min_value=0, value=0)
            input_values["logged_in"] = st.number_input("Logged In", min_value=0, max_value=1, value=0)
            input_values["num_compromised"] = st.number_input("Num Compromised", min_value=0, value=0)
            input_values["root_shell"] = st.number_input("Root Shell", min_value=0, value=0)
            input_values["su_attempted"] = st.number_input("SU Attempted", min_value=0, value=0)

            # Map the input values to the order required by feature_names
            full_input_data = [input_values.get(feat, 0) for feat in feature_names]

        else:  
            # --- CICIDS Feature Inputs (Simplified List) ---
            input_dict = {}
            for feat in feature_names:
                # Use a simplified number input, guessing default values
                input_dict[feat] = st.number_input(feat.strip(), min_value=0.0, value=0.0, format="%.4f")
            
            full_input_data = list(input_dict.values())
        
        # --- Prediction and Display ---
        submit = st.form_submit_button("🔍 Analyse Connection")
        
        if submit:
            label_map = config.get("label_map")
            
            # Make prediction using the full list of feature values
            pred_label, proba, pred_numeric = make_prediction(model, scaler, feature_names, full_input_data, label_map)
            
            st.subheader("Analysis Result")
            
            if dataset_choice.endswith("Multi-class"):
                st.info(f"🔎 Predicted Attack Type: **{pred_label}** (Numeric Label: {pred_numeric})")
                
                if proba is not None:
                    st.write("**Class Probabilities:**")
                    
                    classes = model.classes_
                    # Map numeric classes back to string labels for display
                    if all(isinstance(c, (int, np.integer)) for c in classes) and label_map:
                        display_classes = [label_map.get(int(c), c) for c in classes]
                    else:
                        display_classes = classes 

                    for cls, p in zip(display_classes, proba):
                        st.write(f"- {cls}: **{p:.4f}**")
                        
            else: # Binary Classification
                # Binary classification is a special case of multi-class (2 classes)
                if pred_numeric == 0:
                    st.success(f"✅ Connection Status: **{pred_label}**")
                    if proba is not None:
                        st.metric("Confidence (Normal)", f"{proba[0]:.4f}")
                else:
                    st.error(f"🚨 ATTACK DETECTED: **{pred_label}**")
                    if proba is not None:
                        st.metric("Confidence (Attack)", f"{proba[1]:.4f}")

elif input_mode == "Upload CSV":
    st.header("Upload CSV for Batch Prediction")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
        st.dataframe(input_df.head())
        if st.button("🔍 Predict CSV"):
            try:
                # Ensure the input DataFrame has the correct feature columns and order
                df_to_predict = input_df[feature_names]
                
                scaled_input = scaler.transform(df_to_predict)
                predictions_numeric = model.predict(scaled_input)
                
                # Reverse map predictions for display
                label_map = config.get("label_map")
                if label_map:
                    predictions_final = [label_map.get(int(p), f"Unknown ({p})") for p in predictions_numeric]
                else:
                    predictions_final = predictions_numeric
                    
                input_df["Prediction"] = predictions_final
                
                st.dataframe(input_df.head(20))
                csv = input_df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="📥 Download Predictions as CSV",
                    data=csv,
                    file_name="predictions.csv",
                    mime="text/csv",
                )
            except Exception as e:
                st.error(f"Prediction failed. Ensure your CSV has all the required features in the correct order. Details: {e}")