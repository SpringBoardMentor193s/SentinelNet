import streamlit as st

st.set_page_config(page_title="SentinelNet", layout="centered")

st.title("SentinelNet NSL_KDD Dataset - Model Selection")

# Dropdown for models
model_choice = st.selectbox(
    "Select a Model:",
    ["Logistic Regression", "Decision Tree", "Random Forest"]
)

# Save selection in session_state
if st.button("Next ➡️"):
    st.session_state["selected_model"] = model_choice
    st.switch_page("pages/Feature_Input.py")


# Showing accuracy