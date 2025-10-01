import streamlit as st
import pandas as pd
import io

st.set_page_config(
    page_title="File Upload - SentinelNet", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Check if model is selected
if "selected_model" not in st.session_state:
    st.error("⚠️ Please go back and select a model first!")
    if st.button("← Back to Model Selection"):
        st.switch_page("pages/Model_Selection.py")
    st.stop()

st.title("📁 Data Upload")
st.markdown("---")

st.write(f"**Selected Dataset:** {st.session_state['selected_dataset']}")
if "classification_type" in st.session_state:
    st.write(f"**Classification Type:** {st.session_state['classification_type']}")
st.write(f"**Selected Model:** {st.session_state['selected_model']}")

st.markdown("""
### Upload your CSV file for prediction:

Choose one of the upload methods below:
""")

# File upload section
upload_method = st.radio(
    "Upload Method:",
    ["📤 Drag and Drop", "🔍 Browse Files"],
    horizontal=True
)

st.markdown("---")

if upload_method == "📤 Drag and Drop":
    st.markdown("#### Drag and Drop your CSV file here:")
    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=['csv'],
        help="Upload a CSV file with the appropriate features for your selected dataset",
        label_visibility="collapsed"
    )
else:
    st.markdown("#### Browse and select your CSV file:")
    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=['csv'],
        help="Browse your computer to select a CSV file with the appropriate features"
    )

# Dataset requirements
st.markdown("---")
st.markdown("#### 📋 Dataset Requirements:")

if st.session_state["selected_dataset"] == "NSL-KDD":
    st.markdown("""
    **NSL-KDD Dataset Requirements:**
    - **File format:** CSV (.csv)
    - **Expected features:** 41 columns
    - **Required columns:** duration, protocol_type, service, flag, src_bytes, dst_bytes, land, wrong_fragment, urgent, hot, num_failed_logins, logged_in, num_compromised, root_shell, su_attempted, num_root, num_file_creations, num_shells, num_access_files, num_outbound_cmds, is_host_login, is_guest_login, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, srv_diff_host_rate, dst_host_count, dst_host_srv_count, dst_host_same_srv_rate, dst_host_diff_srv_rate, dst_host_same_src_port_rate, dst_host_srv_diff_host_rate, dst_host_serror_rate, dst_host_srv_serror_rate, dst_host_rerror_rate, dst_host_srv_rerror_rate
    """)
else:  # CIC-IDS
    st.markdown("""
    **CIC-IDS Dataset Requirements:**
    - **File format:** CSV (.csv)
    - **Expected features:** 78 columns
    - **Required columns:** Various network flow features including flow duration, total packets, total bytes, source/destination information, protocol details, and statistical features
    """)

# File processing
if uploaded_file is not None:
    try:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        st.success(f"✅ File uploaded successfully!")
        st.markdown(f"**File:** {uploaded_file.name}")
        st.markdown(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
        
        # Store the dataframe in session state
        st.session_state["uploaded_data"] = df
        st.session_state["uploaded_file_name"] = uploaded_file.name
        
        # Show preview
        with st.expander("📊 Preview your data (first 5 rows)"):
            st.dataframe(df.head())
        
        # Validate dataset compatibility
        expected_features = 41 if st.session_state["selected_dataset"] == "NSL-KDD" else 78
        
        if df.shape[1] == expected_features:
            st.success(f"✅ Dataset compatibility confirmed! Expected {expected_features} features, found {df.shape[1]}.")
        else:
            st.warning(f"⚠️ Feature count mismatch! Expected {expected_features} features, found {df.shape[1]}. The model may not work correctly.")
        
        # Proceed button
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Proceed to Prediction", use_container_width=True):
                st.switch_page("pages/Prediction.py")
                
    except Exception as e:
        st.error(f"❌ Error reading the CSV file: {str(e)}")
        st.markdown("Please ensure your file is a valid CSV format.")

# Navigation
st.markdown("---")
if st.button("← Back to Model Selection"):
    st.switch_page("pages/Model_Selection.py")
