# streamlit_app/app.py
import streamlit as st
import pandas as pd
import joblib
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
from utils.preprocessing import DataPreprocessor

st.set_page_config(page_title="SentinelNet", layout="wide")
st.title("SentinelNet: Network Intrusion Detection")

# ---------------- Sidebar ----------------
dataset_choice = st.sidebar.selectbox("Dataset", ["CICIDS2017", "NSL-KDD"])
classification_choice = st.sidebar.selectbox("Classification", ["Binary"])

available_models = {
    "CICIDS2017": ["Random Forest", "Gradient Boosting", "Decision Tree", "Logistic Regression"],
    "NSL-KDD": ["Random Forest", "Gradient Boosting", "Decision Tree", "Logistic Regression", "XGBoost"]
}

model_choice = st.sidebar.selectbox("Model", available_models[dataset_choice])
debug = st.sidebar.checkbox("Debug", False)

# ---------------- Paths (Updated) ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def model_and_preproc_paths(dataset):
    if 'CICIDS' in dataset.upper():
        model_file = os.path.join(BASE_DIR, "models", "cicids_models.pkl")
        preproc_file = os.path.join(BASE_DIR, "scalers", "cicids_binary_preprocessor.pkl")
        dataset_type = "cicids"
    else:
        model_file = os.path.join(BASE_DIR, "models", "nslkdd_models.pkl")
        preproc_file = os.path.join(BASE_DIR, "scalers", "nsl_kdd_binary_preprocessor.pkl")
        dataset_type = "nsl_kdd"
    return model_file, preproc_file, dataset_type

# ---------------- File Upload ----------------
uploaded = st.file_uploader("Upload CSV file (optional)", type=["csv"])
model_path, preproc_path, dataset_type = model_and_preproc_paths(dataset_choice)

def load_artifacts(model_path, preproc_path, model_name, dataset_type):
    """
    Load trained model and preprocessing artifacts.
    """
    try:
        all_models = joblib.load(model_path)
        model = all_models[model_name]
        preprocessor = DataPreprocessor(dataset_type).load_preprocessor(preproc_path)
        return model, preprocessor
    except Exception as e:
        print(f"Error loading artifacts: {e}")
        return None, None

# If no CSV uploaded, ask user for manual feature inputs
if uploaded:
    try:
        df = pd.read_csv(uploaded)
        st.write("Preview:", df.head())
    except Exception as e:
        st.error(f"Unable to read CSV: {e}")
        st.stop()
else:
    st.info("No CSV uploaded. Enter feature values manually below:")

    # Load preprocessor just to fetch feature names
    try:
        _, preprocessor_tmp = load_artifacts(model_path, preproc_path, model_choice, dataset_type)
        feature_names = preprocessor_tmp.features
    except Exception as e:
        st.warning(f"Could not load preprocessor features: {e}")
        feature_names = [f"feature{i}" for i in range(1, 6)]

    # Build manual input form
    input_data = {}
    for feature in feature_names:
        input_data[feature] = st.number_input(f"{feature}", value=0.0)
    df = pd.DataFrame([input_data])

# ---------------- Load Model + Preprocessor ----------------
if not os.path.exists(model_path) or not os.path.exists(preproc_path):
    st.error("Model or preprocessor file not found.")
    st.stop()

@st.cache_resource
def get_model_and_preprocessor(mp, pp, model_name, dataset_type):
    return load_artifacts(mp, pp, model_name, dataset_type)

model, preprocessor = get_model_and_preprocessor(model_path, preproc_path, model_choice, dataset_type)

# ---------------- Preprocess ----------------
X_proc, y_true = preprocessor.preprocess(df, is_training=False)
st.error("Preprocessing failed.") if X_proc is None else None
st.write("Processed shape:", X_proc.shape)

# ---------------- Predict ----------------
with st.spinner("Running prediction..."):
    preds = model.predict(X_proc)
    probs = model.predict_proba(X_proc) if hasattr(model, "predict_proba") else None

# ---------------- Metrics ----------------
if y_true is not None:
    y_true = y_true.reset_index(drop=True)
    preds_series = pd.Series(preds)
    st.metric("Accuracy", f"{accuracy_score(y_true, preds_series)*100:.2f}%")
    st.metric("Precision", f"{precision_score(y_true, preds_series):.4f}")
    st.metric("Recall", f"{recall_score(y_true, preds_series):.4f}")
    st.metric("F1-score", f"{f1_score(y_true, preds_series):.4f}")

    # Confusion matrix
    cm = confusion_matrix(y_true, preds)
    fig, ax = plt.subplots(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Greens", ax=ax,
                xticklabels=["Benign(0)","Attack(1)"], yticklabels=["Benign(0)","Attack(1)"])
    ax.set_xlabel("Predicted"); ax.set_ylabel("Actual")
    ax.set_title(f"Confusion Matrix - {model_choice}")
    st.pyplot(fig)

    # ROC curve
    if probs is not None and probs.shape[1] > 1:
        y_score = probs[:, 1]
        fpr, tpr, _ = roc_curve(y_true, y_score)
        roc_auc = auc(fpr, tpr)
        fig2, ax2 = plt.subplots(figsize=(5,4))
        ax2.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
        ax2.plot([0,1],[0,1], linestyle="--", color="gray")
        ax2.set_xlabel("FPR"); ax2.set_ylabel("TPR")
        ax2.set_title("ROC Curve")
        ax2.legend()
        st.pyplot(fig2)

# ---------------- Feature Importance ----------------
if hasattr(model, "feature_importances_"):
    importances = model.feature_importances_
    feat_names = X_proc.columns
    df_imp = pd.DataFrame({"feature": feat_names, "importance": importances})
    df_imp = df_imp.sort_values("importance", ascending=False).head(20)
    fig3, ax3 = plt.subplots(figsize=(8,4))
    sns.barplot(x="importance", y="feature", data=df_imp, ax=ax3)
    ax3.set_title("Top 20 Feature Importances")
    st.pyplot(fig3)

# ---------------- Download Predictions ----------------
out_df = df.reset_index(drop=True).copy()
out_df["predicted"] = preds
if probs is not None:
    out_df["confidence"] = np.max(probs, axis=1)

st.download_button("Download predictions CSV", out_df.to_csv(index=False).encode('utf-8'),
                   file_name="predictions.csv", mime="text/csv")
st.success("Prediction complete!")