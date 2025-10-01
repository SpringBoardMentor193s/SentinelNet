import streamlit as st

st.set_page_config(
    page_title="Classification Type - SentinelNet", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Check if dataset is selected
if "selected_dataset" not in st.session_state or st.session_state["selected_dataset"] != "NSL-KDD":
    st.error("⚠️ Please go back and select NSL-KDD dataset first!")
    if st.button("← Back to Dataset Selection"):
        st.switch_page("Home.py")
    st.stop()

st.title("🎯 Classification Type Selection")
st.markdown("---")

st.write(f"**Selected Dataset:** {st.session_state['selected_dataset']}")

st.markdown("""
### Choose your classification approach:

NSL-KDD dataset supports both binary and multiclass classification approaches:
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🔴 Binary Classification
    - **Simpler approach**
    - Classifies traffic as **Normal** or **Attack**
    - Faster training and prediction
    - Good for general intrusion detection
    - **2 classes**: Normal, Attack
    """)
    
    if st.button("Select Binary Classification", key="binary", use_container_width=True):
        st.session_state["classification_type"] = "Binary"
        st.switch_page("pages/Model_Selection.py")

with col2:
    st.markdown("""
    ### 🟡 Multiclass Classification
    - **Detailed approach**
    - Identifies specific attack types
    - More informative results
    - Requires more computational resources
    - **5 classes**: Normal, DoS, Probe, R2L, U2R
    """)
    
    if st.button("Select Multiclass Classification", key="multiclass", use_container_width=True):
        st.session_state["classification_type"] = "Multiclass"
        st.switch_page("pages/Model_Selection.py")

st.markdown("---")
st.markdown("""
**Classification Details:**

**Binary Classification:**
- Normal: Legitimate network traffic
- Attack: Any malicious activity

**Multiclass Classification:**
- Normal: Legitimate network traffic
- DoS: Denial of Service attacks
- Probe: Surveillance and probing attacks
- R2L: Remote to Local attacks
- U2R: User to Root attacks
""")

if st.button("← Back to Dataset Selection"):
    st.switch_page("Home.py")
