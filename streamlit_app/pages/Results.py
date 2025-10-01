import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import time

st.set_page_config(
    page_title="Results - SentinelNet", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Check if predictions exist
if "predictions" not in st.session_state:
    st.error("⚠️ No prediction results found! Please go back and run predictions first.")
    if st.button("← Back to Prediction"):
        st.switch_page("pages/Prediction.py")
    st.stop()

st.title("📊 Prediction Results")
st.markdown("---")

# Get data from session state
predictions = st.session_state["predictions"]
prediction_probs = st.session_state.get("prediction_probs")
processed_data = st.session_state["processed_data"]
model = st.session_state["model"]

# Display configuration
st.markdown(f"""
**Configuration Summary:**
- **Dataset:** {st.session_state['selected_dataset']}
- **Classification:** {st.session_state.get('classification_type', 'Binary')}
- **Model:** {st.session_state['selected_model']}
- **Data Points:** {len(predictions)}
""")

st.markdown("---")

# Results overview
col1, col2, col3, col4 = st.columns(4)

# Calculate basic statistics
unique_predictions, counts = np.unique(predictions, return_counts=True)
total_samples = len(predictions)

with col1:
    st.metric("Total Samples", total_samples)

with col2:
    st.metric("Unique Classes", len(unique_predictions))

with col3:
    # Calculate accuracy if we have ground truth
    accuracy = None
    true_labels = None
    if "uploaded_data" in st.session_state:
        df_uploaded = st.session_state["uploaded_data"]
        # Try common label column names
        for col in ["label", "Label", "target", "y_true", "class"]:
            if col in df_uploaded.columns:
                true_labels = df_uploaded[col].values
                break
    if true_labels is not None and len(true_labels) == len(predictions):
        accuracy = np.mean(np.array(predictions) == np.array(true_labels))
        st.metric("Accuracy", f"{accuracy:.2%}")
    else:
        st.metric("Accuracy", "N/A")
    st.metric("Model Confidence", f"{np.mean(np.max(prediction_probs, axis=1)):.2%}" if prediction_probs is not None else "N/A")

with col4:
    most_common = Counter(predictions).most_common(1)[0]
    st.metric("Most Common Class", f"{most_common[0]} ({most_common[1]} samples)")

st.markdown("---")

# Classification results
st.markdown("### 🎯 Classification Results")

# Create results dataframe
results_df = pd.DataFrame({
    'Sample_ID': range(1, len(predictions) + 1),
    'Prediction': predictions,
    'Confidence': np.max(prediction_probs, axis=1) if prediction_probs is not None else [1.0] * len(predictions)
})

# Map predictions to labels based on dataset and classification type
def map_predictions_to_labels(predictions, dataset, classification_type):
    """Map numeric predictions to meaningful labels"""
    
    if dataset == "NSL-KDD":
        if classification_type == "Binary":
            # Binary: 0 = Normal, 1 = Attack
            return ["Normal" if p == 0 else "Attack" for p in predictions]
        else:  # Multiclass
            # Multiclass: 0 = Normal, 1 = DoS, 2 = Probe, 3 = R2L, 4 = U2R
            label_map = {0: "Normal", 1: "DoS", 2: "Probe", 3: "R2L", 4: "U2R"}
            return [label_map.get(p, f"Unknown_{p}") for p in predictions]
    else:  # CIC-IDS
        # Binary: 0 = Normal, 1 = Attack
        return ["Normal" if p == 0 else "Attack" for p in predictions]

# Add label column
results_df['Label'] = map_predictions_to_labels(
    predictions, 
    st.session_state["selected_dataset"], 
    st.session_state.get("classification_type", "Binary")
)

# Display results table
st.dataframe(results_df, use_container_width=True)

st.markdown("---")

# Visualization section
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📈 Prediction Distribution")
    
    # Count predictions by label
    label_counts = Counter(results_df['Label'])
    
    # Create pie chart
    fig_pie = px.pie(
        values=list(label_counts.values()),
        names=list(label_counts.keys()),
        title="Prediction Distribution",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.markdown("### 📊 Confidence Distribution")
    
    if prediction_probs is not None:
        # Create confidence histogram
        fig_hist = px.histogram(
            results_df,
            x='Confidence',
            nbins=20,
            title="Prediction Confidence Distribution",
            labels={'Confidence': 'Confidence Score', 'count': 'Number of Samples'}
        )
        st.plotly_chart(fig_hist, use_container_width=True)
    else:
        st.info("Confidence scores not available for this model.")

# Detailed analysis
st.markdown("---")
st.markdown("### 🔍 Detailed Analysis")

# Summary statistics
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Class Distribution:")
    for label, count in label_counts.items():
        percentage = (count / total_samples) * 100
        st.write(f"**{label}:** {count} samples ({percentage:.1f}%)")

with col2:
    st.markdown("#### Confidence Statistics:")
    if prediction_probs is not None:
        st.write(f"**Average Confidence:** {np.mean(results_df['Confidence']):.3f}")
        st.write(f"**Min Confidence:** {np.min(results_df['Confidence']):.3f}")
        st.write(f"**Max Confidence:** {np.max(results_df['Confidence']):.3f}")
        st.write(f"**Std Deviation:** {np.std(results_df['Confidence']):.3f}")
    else:
        st.info("Confidence statistics not available.")

# Risk assessment
st.markdown("---")
st.markdown("### ⚠️ Security Assessment")

# Count attacks
attack_count = sum(1 for label in results_df['Label'] if label != "Normal")
normal_count = total_samples - attack_count

if attack_count > 0:
    st.error(f"🚨 **SECURITY ALERT:** {attack_count} potential attacks detected out of {total_samples} samples!")
    
    # Show high-risk samples
    high_risk_samples = results_df[
        (results_df['Label'] != "Normal") & 
        (results_df['Confidence'] > 0.8)
    ]
    
    if len(high_risk_samples) > 0:
        st.warning(f"**High Confidence Attacks:** {len(high_risk_samples)} samples with >80% confidence")
        
        with st.expander("🔴 High-Risk Samples Details"):
            st.dataframe(high_risk_samples, use_container_width=True)
else:
    st.success("✅ **SECURITY STATUS:** No attacks detected in the analyzed samples!")

# Download results
st.markdown("---")
st.markdown("### 💾 Download Results")

# Create downloadable CSV
csv_data = results_df.to_csv(index=False)
st.download_button(
    label="📥 Download Results as CSV",
    data=csv_data,
    file_name=f"sentinelnet_results_{st.session_state['selected_dataset']}_{st.session_state['selected_model'].replace(' ', '_')}.csv",
    mime="text/csv"
)

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🔄 Run New Prediction"):
        st.switch_page("pages/Prediction.py")

with col2:
    if st.button("📁 Upload New File"):
        st.switch_page("pages/File_Upload.py")

with col3:
    if st.button("🏠 Back to Home"):
        st.switch_page("Home.py")
