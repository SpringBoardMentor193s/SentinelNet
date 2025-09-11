# SentinelNet ‒ Model Explanation

This section explains the machine learning model(s) used in SentinelNet, their rationale, and how they contribute to intrusion detection.

---

## Problem Context

Network Intrusion Detection is a classification problem: given network traffic data, the system must decide whether the traffic is **normal** or an **attack** (malicious).  
Challenges include:

- **High dimensionality**: Many network features (protocols, ports, packet sizes, etc.)  
- **Class imbalance**: Attacks may be far fewer than normal traffic  
- **Real-time constraints**: Models must be efficient and scalable

---

## Model Choice

SentinelNet primarily uses **XGBoost (Extreme Gradient Boosting)**, a powerful ensemble learning method.  

- **Why XGBoost?**
  - Handles high-dimensional tabular data effectively.  
  - Built-in ability to deal with missing values.  
  - Robust against overfitting with proper regularization.  
  - Provides feature importance scores for interpretability.  
  - Scales well to large datasets, crucial for network traffic analysis.

Other experimental models may include:
- Logistic Regression (baseline)  
- Random Forests (bagging ensemble for interpretability)  
- Deep Learning (optional for sequence modeling of traffic)

---

## How the Model Works

1. **Input Features**  
   - Preprocessed traffic data (numerical & categorical features scaled/encoded).  
   - Example features: protocol type, service, duration, bytes sent/received, flags.

2. **Model Training**  
   - XGBoost builds multiple weak learners (decision trees).  
   - Each new tree focuses on the errors of the previous ones.  
   - Loss function minimized with gradient boosting.  

3. **Output**  
   - Probability score for each class (normal vs. attack type).  
   - Final classification based on threshold (default 0.5, can be tuned).  

---

## Evaluation Metrics

Key metrics for intrusion detection:

- **Accuracy** – overall correctness  
- **Precision** – proportion of predicted attacks that are true attacks  
- **Recall** – ability to catch actual attacks (low false negatives)  
- **F1 Score** – balance between precision & recall  
- **ROC-AUC** – model’s discrimination ability  

---

## Interpretability

- **Feature Importance**: SentinelNet can output ranked features that contributed most to the predictions (via XGBoost’s `feature_importances_`).  
- **Confusion Matrix**: Helps visualize errors (false positives vs false negatives).  

---

## Model Limitations

- May require frequent retraining as attack patterns evolve.  
- XGBoost models, while faster than deep networks, may still be heavy for strict real-time use.  
- Data quality heavily influences performance (garbage in → garbage out).  

---

## Future Model Improvements

- Ensemble multiple algorithms (stacking, voting).  
- Incorporate **unsupervised anomaly detection** (for unknown/new attacks).  
- Explore **deep learning architectures** like LSTMs or Transformers for sequential network data.  
- Integrate online learning for real-time updates.  
