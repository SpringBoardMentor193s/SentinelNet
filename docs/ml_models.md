# 📘 Machine Learning Models Documentation  


## 📌 Table of Contents
1. [Introduction](#-introduction)  
2. [Linear Regression](#-1-linear-regression)  
3. [Logistic Regression](#-2-logistic-regression)  
4. [Decision Tree](#-3-decision-tree)  
5. [Random Forest](#-4-random-forest)  
6. [Support Vector Machine (SVM)](#-5-support-vector-machine-svm)  
7. [Summary Table](#-summary-table)  

---

## 🔰 Introduction
Machine Learning (ML) algorithms allow computers to learn patterns from data and make predictions.  
In this project, we cover the following models:  

- Linear Regression  
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Support Vector Machine (SVM)  

Each section includes:  
- Purpose  
- Mathematical Formula  
- Working Principle  
- Example Use Case  
- Pros & Cons  

---

## 🔹 1. Linear Regression
- **Purpose:** Predicts continuous values.  
- **Formula:**  
  y = β0 + β1·x1 + β2·x2 + … + βn·xn + ε  

- **Working Principle:** Fits a straight line that minimizes the Mean Squared Error (MSE).  
- **Example Use Case:** House price prediction.  

**✅ Pros**  
- Simple and interpretable  
- Fast training  

**⚠️ Cons**  
- Assumes linear relationship  
- Sensitive to outliers  

---

## 🔹 2. Logistic Regression
- **Purpose:** Binary classification (Yes/No, 0/1).  
- **Formula:**  
  P(Y=1|X) = 1 / (1 + e^-(β0 + β1·x1 + … + βn·xn))  

- **Working Principle:** Uses sigmoid function to map output between 0 and 1.  
- **Example Use Case:** Email spam detection.  

**✅ Pros**  
- Probabilistic interpretation  
- Simple and efficient  

**⚠️ Cons**  
- Only linear decision boundaries  
- Limited with complex datasets  

---

## 🔹 3. Decision Tree
- **Purpose:** Handles both classification & regression.  
- **Formula (Splitting Criteria):**  
  - **Gini Index:** Gini = 1 − Σ(pᵢ²)  
  - **Entropy:** Entropy = − Σ(pᵢ log₂(pᵢ))  

- **Working Principle:** Splits data recursively into branches using rules.  
- **Example Use Case:** Customer churn prediction.  

**✅ Pros**  
- Easy to visualize and interpret  
- Works with both categorical & numerical data  

**⚠️ Cons**  
- Prone to overfitting  
- Small data changes can affect structure  

---

## 🔹 4. Random Forest
- **Purpose:** Ensemble of decision trees (Bagging method).  
- **Formula (Prediction):**  
  ŷ = (1/N) Σ hᵢ(x)  

  where hᵢ(x) = prediction of the i-th decision tree.  

- **Working Principle:** Builds multiple decision trees on random subsets of data; uses majority vote/average.  
- **Example Use Case:** Fraud detection.  

**✅ Pros**  
- High accuracy  
- Reduces overfitting  

**⚠️ Cons**  
- Harder to interpret  
- Computationally expensive  

---

## 🔹 5. Support Vector Machine (SVM)
- **Purpose:** Classification (and regression).  
- **Formula (Hyperplane):**  
  wᵀx + b = 0  

- **Optimization Objective:**  
  Maximize margin = 2 / ||w||  

- **Working Principle:** Finds optimal hyperplane that separates classes with maximum margin; supports kernels for non-linear data.  
- **Example Use Case:** Handwritten digit classification.  

**✅ Pros**  
- Effective in high-dimensional spaces  
- Works well with clear margins  

**⚠️ Cons**  
- Slow with large datasets  
- Needs careful kernel tuning  

---

## 📊 Summary Table  

| Algorithm            | Type            | Formula / Principle               | Pros                          | Cons                          |
|-----------------------|----------------|-----------------------------------|-------------------------------|-------------------------------|
| Linear Regression     | Regression     | y = β0 + β1·x1 + … + βn·xn + ε   | Simple, interpretable         | Sensitive to outliers         |
| Logistic Regression   | Classification | Sigmoid: 1 / (1 + e^(-z))        | Probabilistic output          | Linear boundary only          |
| Decision Tree         | Both           | Gini / Entropy splits            | Easy to visualize             | Overfitting, unstable         |
| Random Forest         | Both (Ensemble)| Average of many trees             | High accuracy, less overfit   | Hard to interpret             |
| SVM                   | Classification | Max margin hyperplane             | Works in high dimensions      | Slow on large datasets        |

---
## ML Metrics 

# ML Performance Metrics Demo

This project demonstrates **model evaluation metrics** for binary classification using scikit-learn.

---

## 📌 Steps Covered
1. **Data Preprocessing**
   - Synthetic imbalanced dataset created using `make_classification`.
   - Train-test split with stratification.

2. **Model Training**
   - Logistic Regression trained on the dataset.

3. **Performance Metrics**
   - **Confusion Matrix** → Shows TP, FP, FN, TN.
   - **Accuracy** → (TP + TN) / Total.
   - **Precision** → TP / (TP + FP).
   - **Recall** → TP / (TP + FN).
   - **F1-Score** → Harmonic mean of Precision & Recall.
   - **ROC-AUC** → Area under ROC curve.

4. **Visualization**
   - Confusion Matrix heatmap.
   - ROC Curve with AUC score.

---

## 📊 Why F1-Score Always?
- Accuracy can be **misleading** in imbalanced datasets.
  - Example: If 95% of samples are class 0, predicting all as 0 gives 95% accuracy but **0 recall for class 1**.
- Precision focuses on "how many predicted positives were correct".
- Recall focuses on "how many actual positives were found".
- **F1-score balances both** → It is especially important when:
  - Classes are imbalanced.
  - Both false positives & false negatives matter.

---

## 🔑 Importance of F1-Score
- Provides a **single metric** combining **precision & recall**.
- Useful in:
  - **Fraud detection** (false negatives costly).
  - **Medical diagnosis** (false negatives very risky).
  - **Cybersecurity** (both FP & FN are important).
- Helps ensure models do not just memorize majority class but also detect minority class.

---

## 🚀 How to Run
```bash
pip install scikit-learn matplotlib seaborn
python ml_metrics_demo.py

```

# NSL-KDD Performance Metrics Demo

This project demonstrates **model evaluation metrics** for binary classification on the **NSL-KDD dataset**.

---

## 📌 Steps
1. **Data Preprocessing**
   - Load `KDDTrain+` and `KDDTest+` files.
   - Convert labels → `0 = normal`, `1 = attack`.
   - One-hot encode categorical features (`protocol_type`, `service`, `flag`).
   - Scale numerical features.

2. **Model Training**
   - Logistic Regression trained on preprocessed features.

3. **Performance Metrics**
   - **Confusion Matrix** (TP, FP, FN, TN).
   - **Accuracy** → `(TP+TN) / Total`.
   - **Precision** → `TP / (TP+FP)`.
   - **Recall** → `TP / (TP+FN)`.
   - **F1-Score** → harmonic mean of Precision & Recall.
   - **ROC-AUC** → probability-based evaluation.

4. **Visualization**
   - Confusion Matrix heatmap.
   - ROC Curve with AUC score.

---

## 📊 Why F1-Score Always?
- Accuracy is misleading on **imbalanced datasets** (NSL-KDD has many more attacks).
- Precision shows how many predicted attacks were correct.
- Recall shows how many actual attacks were caught.
- **F1-Score balances both**, making it the most reliable metric for IDS.

---

## 🚀 Run
```bash
pip install scikit-learn matplotlib seaborn pandas
python nsl_kdd_metrics.py
```
# ML Training Notebook

This package includes:
- `ml_training_notebook.ipynb` — auto-detect dataset, perform EDA, train multiple ML models, evaluate, save results.

## How to use
1. Place your dataset CSV in the notebook folder (or name it `data.csv`).
2. Run all notebook cells.
3. Outputs:
   - `results_summary.csv` — model test scores
   - `best_model.joblib` — best pipeline
   - `grid_best_estimator.joblib` — optional GridSearch best model

## Notes
- Classification: target categorical or ≤15 unique numeric values.
- Regression: target continuous numeric.
- Includes feature importances plot for RandomForest.
- Requires: Python 3.8+, pandas, numpy, scikit-learn, matplotlib, joblib.
