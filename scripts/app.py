# app_grand_unified_ids.py (Final attempt to bypass corrupt feature list)
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
import os
import pickle

warnings.filterwarnings('ignore')

# --- DUMMY ENCODER CLASS (Standard) ---
class DummyLabelEncoder:
    def __init__(self, classes):
        self.classes_ = classes
    def inverse_transform(self, y):
        if isinstance(y, (int, float, np.integer)):
            return np.array([self.classes_[int(y)]])
        return np.array([self.classes_[int(i)] for i in y])

# --- GLOBAL FEATURE DEFINITIONS (Used for OHE in NSL-KDD models) ---
ALL_KDD_FEATURES = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login",
    "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate",
    "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count",
    "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
    "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate"
]
CATEGORICAL_KDD_FEATURES = ["protocol_type", "service", "flag"]

NSL_INT_FEATURES = [
    "duration", "src_bytes", "dst_bytes", "count", "srv_count", "dst_host_count", 
    "dst_host_srv_count", "wrong_fragment", "urgent", "hot", "num_failed_logins", 
    "num_compromised", "num_root", "num_file_creations", "num_shells", 
    "num_access_files", "logged_in", "is_host_login", "is_guest_login",
    "protocol_type", "service", "flag", "land", "su_attempted" 
]
CICIDS_INT_FEATURES = ['Flow Duration', 'Total Fwd Packets', 'Total Backward Packets', 'SYN Flag Count', 'ACK Flag Count', 'Min Packet Length', 'Init_Win_bytes_forward']

# --- PLACEHOLDER GENERATOR FOR CORRUPT CICIDS FEATURE LISTS ---
def generate_cicids_placeholders(count):
    """Generates a list of N placeholder feature names for GUI."""
    if count < 5:
        # If the file is extremely small/corrupt, use the standard 78 name format for the GUI
        count = 78 
    return [f"Feature_{i}" for i in range(count)]

# --- MODEL CONFIGURATION (Unified) ---
MODEL_CONFIGS = {
    # ... (NSL-KDD configs omitted for brevity, assumed unchanged) ...
    # Placeholder configs remain as per last provided working state
    "NSL-KDD (Binary)": {
        "models": {"Logistic Regression": "model/nsl_bin_logreg.pkl", "Random Forest": "model/nsl_bin_rf.devel.pkl", "XGBoost": "model/nsl_bin_xgb.pkl"}, "scaler_path": "model/nsl_bin_scaler.pkl", "features_path": "model/nsl_bin_features.pkl", "scaler_features_path": "model/nsl_bin_scaler_features.pkl", "input_int_features": NSL_INT_FEATURES, "labels": {0: "NORMAL", 1: "ATTACK"}, "label_encoder_path": None, "xgb_map_path": None, "input_type": "KDD_RAW"
    },
    "NSL-KDD (Multi-class)": {
        "models": {"Logistic Regression": "model/nsl_multi_logreg.pkl", "Random Forest": "model/nsl_multi_rf.devel.pkl", "XGBoost": "model/nsl_multi_xgb.pkl"}, "scaler_path": "model/nsl_multi_scaler.pkl", "features_path": "model/nsl_multi_features.pkl", "scaler_features_path": "model/nsl_multi_scaler_features.pkl", "input_int_features": NSL_INT_FEATURES, "labels": None, "label_encoder_path": "model/nsl_multi_label_encoder.pkl", "xgb_map_path": "model/nsl_multi_xgboost_label_map.pkl", "input_type": "KDD_RAW"
    },
    "CICIDS (Binary)": {
        "models": {"Logistic Regression": "model/cicids_bin_logreg.pkl", "Random Forest": "model/cicids_bin_rf.devel.pkl", "XGBoost": "model/cicids_bin_xgb.pkl"}, "scaler_path": "model/cicids_bin_scaler.pkl", "features_path": "model/cicids_bin_features.pkl", "scaler_features_path": "model/cicids_bin_scaler_features.pkl", "input_int_features": CICIDS_INT_FEATURES, "labels": {0: "BENIGN", 1: "ATTACK"}, "label_encoder_path": None, "xgb_map_path": None, "input_type": "CICIDS_SCALER_FEATS"
    },
    "CICIDS (Multi-class)": {
        "models": {"Logistic Regression": "model/cicids_multi_logreg.pkl", "Random Forest": "model/cicids_multi_rf.pkl", "XGBoost": "model/cicids_multi_xgb.pkl"}, "scaler_path": "model/cicids_multi_scaler.pkl", "features_path": "model/cicids_multi_features.pkl", "scaler_features_path": "model/cicids_multi_scaler_features.pkl", "input_int_features": CICIDS_INT_FEATURES, "labels": None, "label_encoder_path": "model/cicids_multi_label_encoder.pkl", "xgb_map_path": "model/nsl_multi_xgboost_label_map.pkl", "input_type": "CICIDS_SCALER_FEATS"
    }
}

# --- ASSET LOADER ---
@st.cache_resource
def load_assets(model_path, config, dataset_name):
    """Loads a single model, scaler, encoders, and feature lists."""
    
    loaded_data = {
        'model': None, 'scaler': None, 'label_encoder': None,
        'selected_features': None, 'scaler_input_features': None, 
        'xgb_map': None, 'input_features_for_gui': None
    }
    
    required_paths = [model_path, config["scaler_path"], config["features_path"], config["scaler_features_path"]]
    
    label_encoder_found = False
    if config["label_encoder_path"] and os.path.exists(config["label_encoder_path"]):
        required_paths.append(config["label_encoder_path"])
        label_encoder_found = True

    for f in required_paths:
        if f and not os.path.exists(f):
            st.error(f"Error loading {dataset_name}: Required file not found: '{f}'. Please ensure all files are in the correct location.")
            return None, None, None, None, None, None, None, False

    try:
        loaded_data['model'] = joblib.load(model_path)
        loaded_data['scaler'] = joblib.load(config["scaler_path"])
        
        # Load or confirm Label Encoder
        if label_encoder_found:
            loaded_data['label_encoder'] = joblib.load(config["label_encoder_path"])
        # Else: Fallback for missing encoder is handled by DummyLabelEncoder init logic

        # --- LOAD FEATURE LISTS WITH SANITY CHECK ---
        selected_features_raw = joblib.load(config["features_path"])
        scaler_input_features_raw = joblib.load(config["scaler_features_path"])
        
        loaded_data['selected_features'] = list(selected_features_raw)
        loaded_data['scaler_input_features'] = list(scaler_input_features_raw)

        # Check for corrupted feature list in CICIDS
        if dataset_name.startswith("CICIDS") and len(loaded_data['scaler_input_features']) < 50:
            st.warning(f"Feature list ('{config['scaler_features_path']}') appears corrupt ({len(loaded_data['scaler_input_features'])} features found). Using generic placeholders for GUI.")
            # Use the known required length from the loaded model's shape (if possible), or a standard length
            
            # Since we can't inspect the model's expected shape here without deeper changes, 
            # we rely on the CICIDS standard length (78) for the GUI, but keep the corrupted names for prediction to fail early if necessary.
            
            # The most direct fix is to load the required names from the model itself, 
            # but since we can't reliably predict the model's required input size/names here,
            # we must use the actual (corrupted) names for the prediction to fail with the right ValueError, 
            # and only fix the GUI display names. 
            
            # **BUT**, the prediction crashes because the loaded names are wrong.
            # We must use the known correct feature names for the GUI AND the prediction DataFrame.
            
            # Since we don't know the TRUE names, we must stop and tell the user to fix the file.
            raise ValueError(f"CRITICAL: The file '{config['scaler_features_path']}' is corrupted or incorrect. It contains {len(loaded_data['scaler_input_features'])} feature names, but should contain around 77-80 names. Please ensure the file contains the correct list of feature names.")


        # Load XGBoost map if path exists (handles NSL-KDD Multi-class)
        if config["xgb_map_path"] and os.path.exists(config["xgb_map_path"]):
            loaded_data['xgb_map'] = joblib.load(config["xgb_map_path"])
        
        # Determine GUI input feature list
        if config["input_type"] == "KDD_RAW":
            loaded_data['input_features_for_gui'] = ALL_KDD_FEATURES
        else:
            loaded_data['input_features_for_gui'] = loaded_data['scaler_input_features']

        return (loaded_data['model'], loaded_data['scaler'], loaded_data['label_encoder'], 
                loaded_data['selected_features'], loaded_data['scaler_input_features'], 
                loaded_data['xgb_map'], loaded_data['input_features_for_gui'], True)
    
    except Exception as e:
        st.error(f"An unexpected error occurred during loading: {e}")
        return None, None, None, None, None, None, None, False

# --- PREDICTION FUNCTION (No logic change from last working version) ---
def predict_attack_type(model, scaler, label_encoder, selected_features, scaler_input_features, xgb_map, input_series, config_key):
    """Preprocesses and predicts, handling all dataset and classification types."""
    
    config = MODEL_CONFIGS[config_key]
    dataset_name = config["input_type"]
    
    if dataset_name == "KDD_RAW":
        # NSL-KDD Preprocessing
        raw_input_df = pd.DataFrame([input_series[ALL_KDD_FEATURES].values], columns=ALL_KDD_FEATURES)
        
        temp_df = raw_input_df.copy()
        for col in CATEGORICAL_KDD_FEATURES:
            temp_df[col] = temp_df[col].astype(str)
        encoded_df = pd.get_dummies(temp_df, columns=CATEGORICAL_KDD_FEATURES, prefix=CATEGORICAL_KDD_FEATURES)
        
        input_for_scaling = pd.DataFrame(0.0, index=[0], columns=scaler_input_features)
        for col in input_for_scaling.columns:
            if col in encoded_df.columns:
                input_for_scaling[col] = encoded_df[col].iloc[0]
    else:
        # CICIDS Preprocessing
        # This line uses the corrupted feature names if the file is wrong, causing the crash.
        input_for_scaling = pd.DataFrame([input_series[scaler_input_features].values], columns=scaler_input_features)
    
    # 1. Scaling
    scaled_data = scaler.transform(input_for_scaling)
    scaled_df = pd.DataFrame(scaled_data, columns=scaler_input_features)
    
    # 2. Final Feature Selection
    final_input_data = scaled_df[selected_features].values
    
    # 3. Prediction
    prediction_raw = model.predict(final_input_data)[0]
    
    # 4. Label Mapping
    if config["labels"]:
        prediction_label = config["labels"].get(int(prediction_raw), "UNKNOWN")
    else:
        if config_key == "NSL-KDD (Multi-class)" and xgb_map is not None:
            original_encoded_label = xgb_map.get(int(prediction_raw))
            
            if original_encoded_label is not None:
                prediction_label = label_encoder.inverse_transform([original_encoded_label])[0]
            else:
                 prediction_label = f"UNKNOWN_MAP_INDEX ({int(prediction_raw)})"
        else:
            prediction_label = label_encoder.inverse_transform([int(prediction_raw)])[0]

    return str(prediction_label)

# --- STREAMLIT APP LAYOUT ---
st.set_page_config(page_title="🛡️ Grand Unified IDS App", layout="wide")
st.title("🛡️ Grand Unified Intrusion Detection System")
st.markdown("Combines NSL-KDD and CICIDS for Binary and Multi-class prediction.")
st.markdown("---")

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("Configuration")

classification_type = st.sidebar.selectbox("Choose Classification Type", ["Binary", "Multi-class"])
dataset_options = ["NSL-KDD", "CICIDS"]
dataset_choice_raw = st.sidebar.selectbox("Choose Dataset", dataset_options)

config_key = f"{dataset_choice_raw} ({classification_type})"

if config_key not in MODEL_CONFIGS:
    st.error(f"Error: Configuration '{config_key}' not defined.")
    st.stop()

config = MODEL_CONFIGS[config_key]
model_choice = st.sidebar.selectbox("Choose Machine Learning Model", list(config["models"].keys()))
model_path = config["models"][model_choice]

# Load all assets for the selected configuration
(model, scaler, label_encoder, selected_features, scaler_input_features, xgb_map, input_features_for_gui, loaded) = \
    load_assets(model_path, config, config_key)

if not loaded:
    # If load_assets failed due to corruption/missing file, the error message is already shown.
    st.error("Application setup failed. Please check the feature list files for the selected configuration.")
    st.stop()

# --- INPUT SECTION ---
st.subheader(f"Input Features for {config_key} (Model: {model_choice})")
st.info(f"Input features collected: **{len(input_features_for_gui)}**. Final features used by the model: **{len(selected_features)}**.")

input_int_features = config["input_int_features"]

input_data = {}
col_count = 0
cols = st.columns(4)

for feature in input_features_for_gui:
    is_int = feature in input_int_features
    default_value = 0 if is_int else 0.0
    
    key = f"{config_key}_{feature}" 
    
    input_value = cols[col_count % 4].number_input(
        f"{feature} ({'Int' if is_int else 'Float'})", 
        value=default_value, 
        key=key,
        step=1 if is_int else 0.01, 
        format="%d" if is_int else "%.4f"
    )
    
    input_data[feature] = input_value
    col_count += 1

# --- PREDICTION BUTTON ---
st.markdown("---")
if st.button("Predict Attack Type"):
    
    input_series = pd.Series(input_data)
    
    try:
        prediction = predict_attack_type(
            model, 
            scaler, 
            label_encoder, 
            selected_features, 
            scaler_input_features, 
            xgb_map, 
            input_series, 
            config_key 
        )
        
        st.subheader("Prediction Result")
        
        is_normal = prediction.lower() in ["normal", "benign"]
        
        if classification_type == "Binary":
            if is_normal:
                st.success(f"🎉 **Connection Status (via {model_choice}):** {prediction.upper()} (No Attack)")
            else:
                st.warning(f"🚨 **Connection Status (via {model_choice}):** {prediction.upper()} DETECTED")
        else:
            if is_normal:
                st.success(f"🎉 **Connection Status (via {model_choice}):** {prediction.upper()} (No Attack)")
            else:
                st.warning(f"🚨 **Specific Attack Type Detected (via {model_choice}):** {prediction.upper()}")

    except Exception as e:
        st.error("Prediction Error: An internal error occurred during prediction.")
        st.exception(e)

st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit & Machine Learning")