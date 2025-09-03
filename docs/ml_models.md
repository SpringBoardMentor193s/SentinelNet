# 📘 Machine Learning Models Documentation  

This repository contains simple implementations and explanations of fundamental Machine Learning algorithms.  
The goal is to **understand the intuition, math, and applications** of each model through small projects.  

---

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
  \[
  y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n + \epsilon
  \]  
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
  \[
  P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1x_1 + ... + \beta_nx_n)}}
  \]  
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
  - **Gini Index:**  
    \[
    Gini = 1 - \sum p_i^2
    \]  
  - **Entropy (Information Gain):**  
    \[
    Entropy = - \sum p_i \log_2(p_i)
    \]  
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
  \[
  \hat{y} = \frac{1}{N} \sum_{i=1}^N h_i(x)
  \]  
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
  \[
  w^Tx + b = 0
  \]  
  Maximize margin:  
  \[
  \text{Maximize } \frac{2}{||w||}
  \]  
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

| Algorithm            | Type            | Formula / Principle                | Pros                          | Cons                          |
|-----------------------|----------------|-----------------------------------|-------------------------------|-------------------------------|
| Linear Regression     | Regression     | \( y = \beta_0 + \beta_1x_1 + ...\)| Simple, interpretable         | Sensitive to outliers         |
| Logistic Regression   | Classification | Sigmoid: \( \frac{1}{1+e^{-z}} \) | Probabilistic output          | Linear boundary only          |
| Decision Tree         | Both           | Gini / Entropy                    | Easy to visualize             | Overfitting, unstable         |
| Random Forest         | Both (Ensemble)| Bagging of decision trees          | High accuracy, less overfit   | Hard to interpret             |
| SVM                   | Classification | Max margin hyperplane              | Works in high dimensions      | Slow on large datasets        |

---


