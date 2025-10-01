import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# -------------------- Sidebar --------------------
st.sidebar.title("⚡ SentinelNet IDS")
st.sidebar.subheader("Upload & Configure")

# Upload dataset
uploaded_file = st.sidebar.file_uploader("📂 Upload CSV Dataset", type=["csv"])

# Select model
model_choice = st.sidebar.radio(
    "🤖 Choose ML Model",
    ["Logistic Regression", "Random Forest", "Decision Tree", "Gradient Boosting"]
)

# Button to trigger training
train_button = st.sidebar.button("🚀 Run Intrusion Detection")

# -------------------- Main Page --------------------
st.title("🔐 Network Intrusion Detection System")
st.write("Upload a dataset, choose a model from the sidebar, and detect intrusions.")

if uploaded_file is not None:
    # Load dataset
    df = pd.read_csv(uploaded_file)
    st.success(f"✅ Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    st.dataframe(df.head())

    if train_button:
        try:
            # -------------------- Data Preprocessing --------------------
            # Assume last column is target
            X = df.iloc[:, :-1].copy()
            y = df.iloc[:, -1].copy()

            # If target is continuous → convert to binary
            if pd.api.types.is_numeric_dtype(y):
                # Threshold = median
                y_binary = (y > y.median()).astype(int)
                y = y_binary
                st.info("ℹ️ Target column was continuous → converted to binary classes (0/1).")

            # If target is categorical text → encode
            elif y.dtype == 'object':
                le_target = LabelEncoder()
                y = le_target.fit_transform(y)

            # Encode categorical features
            for col in X.columns:
                if X[col].dtype == 'object':
                    le = LabelEncoder()
                    X[col] = le.fit_transform(X[col])

            # Train/test split
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )

            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # -------------------- Model Selection --------------------
            if model_choice == "Logistic Regression":
                model = LogisticRegression(max_iter=1000)
            elif model_choice == "Random Forest":
                model = RandomForestClassifier(n_estimators=100, random_state=42)
            elif model_choice == "Decision Tree":
                model = DecisionTreeClassifier(random_state=42)
            elif model_choice == "Gradient Boosting":
                model = GradientBoostingClassifier(random_state=42)

            # -------------------- Training --------------------
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)

            # -------------------- Metrics --------------------
            acc = accuracy_score(y_test, y_pred)
            prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
            rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
            f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

            st.subheader("📊 Evaluation Metrics")
            st.write(f"**Model Used:** {model_choice}")
            st.write(f"**Accuracy:** {acc:.4f}")
            st.write(f"**Precision:** {prec:.4f}")
            st.write(f"**Recall:** {rec:.4f}")
            st.write(f"**F1 Score:** {f1:.4f}")

            # -------------------- Confusion Matrix --------------------
            cm = confusion_matrix(y_test, y_pred)
            fig, ax = plt.subplots()
            disp = ConfusionMatrixDisplay(confusion_matrix=cm)
            disp.plot(ax=ax, cmap="Blues", colorbar=False)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"❌ Error during training: {e}")

else:
    st.warning("⚠️ Please upload a dataset to proceed.")
