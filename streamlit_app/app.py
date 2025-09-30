# streamlit_app/app.py
import streamlit as st
import pandas as pd
import joblib
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils.preprocessing import DataPreprocessor
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc

st.set_page_config(page_title="SentinelNet (minimal)", layout="wide")
st.title("SentinelNet - Minimal App")

# Sidebar config
dataset_choice = st.sidebar.selectbox("Dataset", ["CICIDS2017", "NSL-KDD"])
classification_choice = st.sidebar.selectbox("Classification", ["Binary"])
model_choice = st.sidebar.selectbox("Model", ["Random Forest", "Gradient Boosting", "Decision Tree", "Logistic Regression"])
debug = st.sidebar.checkbox("Debug", False)

# Map to file paths
def model_and_preproc_paths(dataset, model_name):
    ds = 'cicids' if 'CICIDS' in dataset.upper() else 'nsl_kdd'
    cls = 'binary'
    model_file = f"streamlit_app/models/{ds}_{cls}/{model_name.lower().replace(' ', '_')}.pkl"
    preproc_file = f"streamlit_app/scalers/{ds}_{cls}_preprocessor.pkl"
    return model_file, preproc_file

uploaded = st.file_uploader("Upload CSV file (optional)", type=["csv"])

if uploaded:
    try:
        df = pd.read_csv(uploaded)
        st.write("Preview:", df.head())
    except Exception as e:
        st.error(f"Unable to read CSV: {e}")
        st.stop()
else:
    st.info("No CSV uploaded. Enter feature values manually below:")
    # Define features manually (replace with actual feature names)
    feature_names = ['feature1', 'feature2', 'feature3', 'feature4']  
    input_data = {}
    for feature in feature_names:
        input_data[feature] = st.number_input(f"{feature}", value=0.0)
    df = pd.DataFrame([input_data])

# Load model + preprocessor
model_path, preproc_path = model_and_preproc_paths(dataset_choice, model_choice)
if debug:
    st.sidebar.write("Model path:", model_path)
    st.sidebar.write("Preprocessor path:", preproc_path)

if not os.path.exists(model_path) or not os.path.exists(preproc_path):
    st.error("Model or preprocessor file not found.")
    st.stop()

@st.cache_resource
def load_artifacts(mp, pp):
    m = joblib.load(mp)
    pre = DataPreprocessor('cicids' if 'cicids' in pp else 'nsl_kdd').load_preprocessor(pp)
    return m, pre

model, preprocessor = load_artifacts(model_path, preproc_path)

X_proc, y_true = preprocessor.preprocess(df, is_training=False)
st.write("Processed shape:", X_proc.shape)

# Predict
with st.spinner("Running prediction..."):
    preds = model.predict(X_proc)
    probs = model.predict_proba(X_proc) if hasattr(model, "predict_proba") else None

# Show metrics if true labels are present
if y_true is not None:
    y_true = y_true.reset_index(drop=True)
    preds_series = pd.Series(preds)
    acc = accuracy_score(y_true, preds_series)
    prec = precision_score(y_true, preds_series)
    rec = recall_score(y_true, preds_series)
    f1 = f1_score(y_true, preds_series)

    st.metric("Accuracy", f"{acc*100:.2f}%")
    st.metric("Precision", f"{prec:.4f}")
    st.metric("Recall", f"{rec:.4f}")
    st.metric("F1-score", f"{f1:.4f}")

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
        ax2.set_xlabel("FPR"); ax2.set_ylabel("TPR"); ax2.set_title("ROC Curve")
        ax2.legend()
        st.pyplot(fig2)

# Feature importance
if hasattr(model, "feature_importances_"):
    importances = model.feature_importances_
    feat_names = X_proc.columns
    df_imp = pd.DataFrame({"feature": feat_names, "importance": importances})
    df_imp = df_imp.sort_values("importance", ascending=False).head(20)
    fig3, ax3 = plt.subplots(figsize=(8,4))
    sns.barplot(x="importance", y="feature", data=df_imp, ax=ax3)
    ax3.set_title("Top 20 Feature Importances")
    st.pyplot(fig3)

# Download predictions
out_df = df.reset_index(drop=True).copy()
out_df["predicted"] = preds
if probs is not None:
    out_df["confidence"] = np.max(probs, axis=1)

st.download_button("Download predictions CSV", out_df.to_csv(index=False).encode('utf-8'),
                   file_name="predictions.csv", mime="text/csv")
st.success("Prediction complete!")