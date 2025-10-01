# import streamlit as st
# import joblib
# import pandas as pd
# import numpy as np
# import os
# from sklearn.preprocessing import LabelEncoder
# import time

# st.set_page_config(
#     page_title="Prediction - SentinelNet", 
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Check if data is uploaded
# if "uploaded_data" not in st.session_state:
#     st.error("⚠️ Please go back and upload your data first!")
#     if st.button("← Back to File Upload"):
#         st.switch_page("pages/File_Upload.py")
#     st.stop()

# st.title("🔮 Prediction Engine")
# st.markdown("---")

# # Display current selections
# st.write(f"**Dataset:** {st.session_state['selected_dataset']}")
# if "classification_type" in st.session_state:
#     st.write(f"**Classification Type:** {st.session_state['classification_type']}")
# st.write(f"**Model:** {st.session_state['selected_model']}")
# st.write(f"**File:** {st.session_state['uploaded_file_name']}")
# st.write(f"**Data Shape:** {st.session_state['uploaded_data'].shape}")

# st.markdown("---")

# # Load and preprocess data
# df = st.session_state["uploaded_data"].copy()

# # Data preprocessing function
# def preprocess_data(df, dataset_type, classification_type):
#     """Preprocess the uploaded data for prediction"""
    
#     if dataset_type == "NSL-KDD":
#         # NSL-KDD specific preprocessing
#         # Handle categorical variables if they exist
#         categorical_columns = ['protocol_type', 'service', 'flag']
        
#         for col in categorical_columns:
#             if col in df.columns:
#                 if df[col].dtype == 'object':
#                     # Label encode categorical variables
#                     le = LabelEncoder()
#                     df[col] = le.fit_transform(df[col])
        
#         # Ensure all columns are numeric
#         df = df.select_dtypes(include=[np.number])
        
#         # Handle missing values
#         df = df.fillna(df.median())
        
#     else:  # CIC-IDS
#         # CIC-IDS specific preprocessing
#         # Remove any non-numeric columns
#         df = df.select_dtypes(include=[np.number])
        
#         # Handle missing values
#         df = df.fillna(df.median())
        
#         # Handle infinite values
#         df = df.replace([np.inf, -np.inf], np.nan)
#         df = df.fillna(df.median())
    
#     return df

# # Prediction function
# def load_model_and_predict(data, dataset_type, classification_type, model_name):
#     """Load the appropriate model and make predictions"""
    
#     # Construct model filename based on selections
#     if dataset_type == "NSL-KDD":
#         if classification_type == "Binary":
#             model_filename = f"{model_name.replace(' ', '_')}.pkl"
#         else:  # Multiclass
#             model_filename = f"{model_name.replace(' ', '_')}_Multiclass.pkl"
#     else:  # CIC-IDS
#         model_filename = f"{model_name.replace(' ', '_')}_CIC_IDS.pkl"
    
#     # Get the directory where this script is located
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     # Go up from streamlit_app/pages to streamlit_app, then up to project root
#     streamlit_app_dir = os.path.dirname(script_dir)
#     project_root = os.path.dirname(streamlit_app_dir)
    
#     # Try multiple possible paths for the models
#     possible_paths = [
#         os.path.join(project_root, "notebooks", "models", model_filename),  # From project root
#         os.path.join(script_dir, "..", "..", "notebooks", "models", model_filename),  # Relative from pages
#         f"../notebooks/models/{model_filename}",  # Relative from streamlit_app
#         f"notebooks/models/{model_filename}",     # From project root
#         f"E:/SentinelNet/notebooks/models/{model_filename}"  # Absolute path
#     ]
    
#     # Debug information
#     with st.expander("🔍 Debug Information", expanded=False):
#         st.write(f"Script directory: {script_dir}")
#         st.write(f"Streamlit app directory: {streamlit_app_dir}")
#         st.write(f"Project root: {project_root}")
#         st.write(f"Current working directory: {os.getcwd()}")
#         st.write(f"Looking for model: {model_filename}")
#         st.write("Trying paths:")
#         for i, path in enumerate(possible_paths):
#             exists = os.path.exists(path)
#             st.write(f"{i+1}. {path} - {'✅ Exists' if exists else '❌ Not found'}")
    
#     model_path = None
#     for path in possible_paths:
#         if os.path.exists(path):
#             model_path = path
#             break
    
#     if model_path is None:
#         st.error(f"❌ Model file not found! Tried {len(possible_paths)} different paths.")
#         st.error("Please ensure the model files exist in the correct location.")
#         return None, None, None
    
#     # Debug: Show the model path being used
#     st.success(f"✅ Found model at: {model_path}")
    
#     try:
#         # Load the model
#         model = joblib.load(model_path)
        
#         # Make predictions
#         predictions = model.predict(data)
        
#         # Get prediction probabilities if available
#         try:
#             prediction_probs = model.predict_proba(data)
#         except:
#             prediction_probs = None
            
#         return predictions, prediction_probs, model
        
#     except Exception as e:
#         st.error(f"Error loading model {model_filename}: {str(e)}")
#         return None, None, None

# # Main prediction section
# st.markdown("### 🎯 Ready to predict!")

# if st.button("🚀 Run Prediction", use_container_width=True):
    
#     # Show progress
#     progress_bar = st.progress(0)
#     status_text = st.empty()
    
#     # Step 1: Preprocessing
#     status_text.text("📊 Preprocessing data...")
#     progress_bar.progress(25)
    
#     processed_data = preprocess_data(df, st.session_state["selected_dataset"], 
#                                    st.session_state.get("classification_type", "Binary"))
    
#     time.sleep(1)  # Simulate processing time
    
#     # Step 2: Load model
#     status_text.text("🤖 Loading model...")
#     progress_bar.progress(50)
    
#     predictions, prediction_probs, model = load_model_and_predict(
#         processed_data,
#         st.session_state["selected_dataset"],
#         st.session_state.get("classification_type", "Binary"),
#         st.session_state["selected_model"]
#     )
    
#     time.sleep(1)  # Simulate loading time
    
#     # Step 3: Making predictions
#     status_text.text("🔮 Making predictions...")
#     progress_bar.progress(75)
    
#     if predictions is not None:
#         # Step 4: Complete
#         status_text.text("✅ Prediction complete!")
#         progress_bar.progress(100)
        
#         # Store results in session state
#         st.session_state["predictions"] = predictions
#         st.session_state["prediction_probs"] = prediction_probs
#         st.session_state["processed_data"] = processed_data
#         st.session_state["model"] = model
        
#         time.sleep(0.5)
        
#         # Clear progress indicators
#         progress_bar.empty()
#         status_text.empty()
        
#         st.success("🎉 Prediction completed successfully!")
#         st.markdown("**Results are ready! Click below to view detailed results.**")
        
#         if st.button("📊 View Results", use_container_width=True):
#             st.switch_page("pages/Results.py")
#     else:
#         progress_bar.empty()
#         status_text.empty()
#         st.error("❌ Prediction failed. Please check your data and try again.")

# # Show data preview
# with st.expander("📋 Data Preview"):
#     st.markdown("**Original Data:**")
#     st.dataframe(df.head())
    
#     if st.session_state.get("processed_data") is not None:
#         st.markdown("**Processed Data:**")
#         st.dataframe(st.session_state["processed_data"].head())

# # Navigation
# st.markdown("---")
# if st.button("← Back to File Upload"):
#     st.switch_page("pages/File_Upload.py")


import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
import time

st.set_page_config(
    page_title="Prediction - SentinelNet", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------------
# Expected features (same as training)
# -------------------------------
EXPECTED_FEATURES = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
    'wrong_fragment','urgent','hot','num_failed_logins','logged_in',
    'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
    'num_shells','num_access_files','num_outbound_cmds','is_host_login',
    'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
    'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
    'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
    'dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
    'dst_host_serror_rate','dst_host_srv_serror_rate',
    'dst_host_rerror_rate','dst_host_srv_rerror_rate'
]

CATEGORICAL_COLUMNS = ['protocol_type', 'service', 'flag']

# -------------------------------
# Preprocessing function
# -------------------------------
def preprocess_data(df, dataset_type="NSL-KDD", classification_type="Binary"):
    """Preprocess the uploaded data for prediction"""

    # Handle categorical encoding
    for col in CATEGORICAL_COLUMNS:
        if col in df.columns and df[col].dtype == "object":
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])

    # Keep only numeric
    df = df.select_dtypes(include=[np.number])

    # Fill missing values
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(df.median(numeric_only=True))

    # Reorder / fill missing columns
    for col in EXPECTED_FEATURES:
        if col not in df.columns:
            df[col] = 0  # add missing cols as 0

    df = df[EXPECTED_FEATURES]  # enforce order

    return df

# -------------------------------
# Model loader + predictor
# -------------------------------
def load_model_and_predict(data, model_name="Decision_Tree"):
    """Load the model and run predictions"""

    model_filename = f"{model_name.replace(' ', '_')}.pkl"

    # Possible model paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    streamlit_app_dir = os.path.dirname(script_dir)
    project_root = os.path.dirname(streamlit_app_dir)

    possible_paths = [
        os.path.join(project_root, "notebooks", "models", model_filename),
        os.path.join(script_dir, "..", "..", "notebooks", "models", model_filename),
        f"../notebooks/models/{model_filename}",
        f"notebooks/models/{model_filename}",
        f"E:/SentinelNet/notebooks/models/{model_filename}"
    ]

    model_path = None
    for path in possible_paths:
        if os.path.exists(path):
            model_path = path
            break

    if model_path is None:
        st.error(f"❌ Model file not found! ({model_filename})")
        return None, None, None

    st.success(f"✅ Found model at: {model_path}")

    try:
        model = joblib.load(model_path)
        predictions = model.predict(data)

        try:
            prediction_probs = model.predict_proba(data)
        except:
            prediction_probs = None

        return predictions, prediction_probs, model

    except Exception as e:
        st.error(f"❌ Error loading model {model_filename}: {str(e)}")
        return None, None, None

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🔮 Prediction Engine")
st.markdown("---")

if "uploaded_data" not in st.session_state:
    st.error("⚠️ Please go back and upload your data first!")
    if st.button("← Back to File Upload"):
        st.switch_page("pages/File_Upload.py")
    st.stop()

df = st.session_state["uploaded_data"].copy()

st.write(f"**Dataset:** {st.session_state['selected_dataset']}")
if "classification_type" in st.session_state:
    st.write(f"**Classification Type:** {st.session_state['classification_type']}")
st.write(f"**Model:** {st.session_state['selected_model']}")
st.write(f"**File:** {st.session_state['uploaded_file_name']}")
st.write(f"**Data Shape:** {df.shape}")

st.markdown("---")
st.markdown("### 🎯 Ready to predict!")

if st.button("🚀 Run Prediction", use_container_width=True):
    progress_bar = st.progress(0)
    status_text = st.empty()

    # Step 1: Preprocess
    status_text.text("📊 Preprocessing data...")
    progress_bar.progress(25)
    processed_data = preprocess_data(df)
    time.sleep(1)

    # Step 2: Load model
    status_text.text("🤖 Loading model...")
    progress_bar.progress(50)
    predictions, prediction_probs, model = load_model_and_predict(processed_data, st.session_state["selected_model"])
    time.sleep(1)

    # Step 3: Predict
    status_text.text("🔮 Making predictions...")
    progress_bar.progress(75)

    if predictions is not None:
        status_text.text("✅ Prediction complete!")
        progress_bar.progress(100)

        st.session_state["predictions"] = predictions
        st.session_state["prediction_probs"] = prediction_probs
        st.session_state["processed_data"] = processed_data
        st.session_state["model"] = model

        progress_bar.empty()
        status_text.empty()

        st.success("🎉 Prediction completed successfully!")
        if st.button("📊 View Results", use_container_width=True):
            st.switch_page("pages/Results.py")
    else:
        progress_bar.empty()
        status_text.empty()
        st.error("❌ Prediction failed. Please check your data and try again.")

# Preview
with st.expander("📋 Data Preview"):
    st.write("**Original Data:**")
    st.dataframe(df.head())
    if st.session_state.get("processed_data") is not None:
        st.write("**Processed Data:**")
        st.dataframe(st.session_state["processed_data"].head())

st.markdown("---")
if st.button("← Back to File Upload"):
    st.switch_page("pages/File_Upload.py")
