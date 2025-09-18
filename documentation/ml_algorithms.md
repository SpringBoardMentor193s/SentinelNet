# Machine Learning Algorithms Documentation

## 1. Linear Regression  
- **What it is:** A supervised learning algorithm used for predicting continuous values (e.g., house prices, sales).  
- **How it works:** Fits a straight line (or hyperplane) to the data by minimizing the error between predicted and actual values.  
  - Formula:  \( y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n \)  
- **Pros:**
  - Easy to understand and implement.  
  - Works well for simple relationships.  
- **Cons:**
  - Assumes linearity between features and target.  
  - Sensitive to outliers.  
- **Use cases:** Predicting prices, forecasting demand, estimating risk.  

---

## 2. Logistic Regression  
- **What it is:** A supervised algorithm used for **classification** (binary or multi-class).  
- **How it works:** Uses the logistic (sigmoid) function to map predictions into probabilities between 0 and 1.  
  - Formula: \( P(y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1x_1 + ... + \beta_nx_n)}} \)  
- **Pros:**
  - Simple, interpretable results.  
  - Outputs probabilities.  
- **Cons:**
  - Only works well when classes are linearly separable.  
  - Limited for complex problems.  
- **Use cases:** Spam detection, medical diagnosis, fraud detection.  

---

## 3. Decision Trees  
- **What it is:** A tree-based model for both classification and regression.  
- **How it works:** Splits data into branches based on feature values, forming a tree where leaves represent predictions.  
- **Pros:**
  - Easy to visualize and interpret.  
  - Handles both numerical and categorical data.  
- **Cons:**
  - Prone to overfitting if not pruned.  
  - Small changes in data can create different trees.  
- **Use cases:** Customer segmentation, credit scoring, medical decision-making.  

---

## 4. Random Forest  
- **What it is:** An **ensemble** method that combines many decision trees to improve accuracy.  
- **How it works:**  
  - Trains multiple decision trees on random subsets of data and features.  
  - Final output is decided by majority vote (classification) or average (regression).  
- **Pros:**
  - High accuracy, less overfitting than single trees.  
  - Handles missing values and noisy data well.  
- **Cons:**
  - Less interpretable than a single decision tree.  
  - Can be computationally heavy for very large datasets.  
- **Use cases:** Fraud detection, stock market prediction, recommendation systems.  

---

## 5. Support Vector Machines (SVM)  
- **What it is:** A powerful algorithm for classification (and regression, called SVR).  
- **How it works:** Finds the **optimal hyperplane** that maximizes the margin between different classes. Can use **kernels** for non-linear data.  
- **Pros:**
  - Works well with high-dimensional data.  
  - Effective for complex boundaries using kernel trick.  
- **Cons:**
  - Computationally expensive for large datasets.  
  - Harder to interpret results.  
- **Use cases:** Text classification, image recognition, bioinformatics.  
