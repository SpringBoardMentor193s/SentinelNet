import streamlit as st

st.set_page_config(
    page_title="SentinelNet", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("🛡️ SentinelNet - Intrusion Detection System")
st.markdown("---")

st.markdown("""
### Welcome to SentinelNet!

SentinelNet is an advanced intrusion detection system that uses machine learning to identify potential cyber threats and attacks in network traffic.

**Choose your dataset to get started:**
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📊 NSL-KDD Dataset
    - **41 features** for network traffic analysis
    - Supports both **Binary** and **Multiclass** classification
    - Binary: Normal vs Attack
    - Multiclass: 5 attack categories
    """)
    
    if st.button("Select NSL-KDD Dataset", key="nsl_kdd", use_container_width=True):
        st.session_state["selected_dataset"] = "NSL-KDD"
        st.switch_page("pages/Classification_Type.py")

with col2:
    st.markdown("""
    ### 🔍 CIC-IDS Dataset
    - **78 features** for comprehensive traffic analysis
    - Modern dataset with realistic attack scenarios
    - Supports **Binary** classification only
    - Includes various attack types like DDoS, Botnet, etc.
    """)
    
    if st.button("Select CIC-IDS Dataset", key="cic_ids", use_container_width=True):
        st.session_state["selected_dataset"] = "CIC-IDS"
        st.session_state["classification_type"] = "Binary"  # CIC-IDS only supports binary
        st.switch_page("pages/Model_Selection.py")

st.markdown("---")
st.markdown("""
**Dataset Information:**
- **NSL-KDD**: Classic benchmark with detailed feature engineering
- **CIC-IDS**: Modern dataset with real-world attack scenarios

Select a dataset above to proceed with model training and prediction.
""")