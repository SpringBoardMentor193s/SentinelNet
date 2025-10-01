import streamlit as st

st.set_page_config(
    page_title="Model Selection - SentinelNet", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Check if dataset is selected
if "selected_dataset" not in st.session_state:
    st.error("⚠️ Please go back and select a dataset first!")
    if st.button("← Back to Dataset Selection"):
        st.switch_page("Home.py")
    st.stop()

st.title("🤖 Model Selection")
st.markdown("---")

st.write(f"**Selected Dataset:** {st.session_state['selected_dataset']}")
if "classification_type" in st.session_state:
    st.write(f"**Classification Type:** {st.session_state['classification_type']}")

st.markdown("""
### Choose your machine learning model:

Select from the available pre-trained models optimized for your dataset and classification type:
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📈 Logistic Regression
    - **Linear model** with good interpretability
    - Fast training and prediction
    - Good baseline performance
    - Suitable for binary classification
    - **Pros**: Fast, interpretable, no hyperparameter tuning
    - **Cons**: Assumes linear relationships
    """)
    
    if st.button("Select Logistic Regression", key="logistic", use_container_width=True):
        st.session_state["selected_model"] = "Logistic Regression"
        st.switch_page("pages/File_Upload.py")

with col2:
    st.markdown("""
    ### 🌳 Decision Tree
    - **Tree-based model** with high interpretability
    - Can capture non-linear relationships
    - Good performance on structured data
    - Prone to overfitting
    - **Pros**: Interpretable, handles non-linear data
    - **Cons**: Can overfit, unstable
    """)
    
    if st.button("Select Decision Tree", key="decision_tree", use_container_width=True):
        st.session_state["selected_model"] = "Decision Tree"
        st.switch_page("pages/File_Upload.py")

with col3:
    st.markdown("""
    ### 🌲 Random Forest
    - **Ensemble method** combining multiple trees
    - Best overall performance
    - Robust to overfitting
    - More computationally intensive
    - **Pros**: High accuracy, robust, feature importance
    - **Cons**: Less interpretable, slower training
    """)
    
    if st.button("Select Random Forest", key="random_forest", use_container_width=True):
        st.session_state["selected_model"] = "Random Forest"
        st.switch_page("pages/File_Upload.py")

st.markdown("---")
st.markdown("""
**Model Performance Expectations:**

| Model | Accuracy | Training Speed | Interpretability | Best For |
|-------|----------|----------------|------------------|----------|
| Logistic Regression | Good | Fast | High | Binary classification |
| Decision Tree | Good | Medium | High | Feature importance analysis |
| Random Forest | Best | Slow | Medium | Overall performance |

**Note:** All models are pre-trained and optimized for your selected dataset and classification type.
""")

if st.button("← Back"):
    if st.session_state["selected_dataset"] == "NSL-KDD":
        st.switch_page("pages/Classification_Type.py")
    else:
        st.switch_page("Home.py")
