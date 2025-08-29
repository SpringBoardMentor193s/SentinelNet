# Linear Regression Documentation

## Introduction
Linear Regression is one of the most fundamental algorithms in Machine Learning.  
It is used to model the relationship between a dependent variable (target) and one or more independent variables (features).

It assumes a **linear relationship** between input variables and the target.

---

## Mathematical Representation


The hypothesis of Linear Regression can be represented as:

\[
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n + \epsilon
\]

Where:
- \( y \): Predicted value (target)
- \( x_1, x_2, ..., x_n \): Input features
- \( \beta_0 \): Intercept term
- \( \beta_1, \beta_2, ..., \beta_n \): Coefficients (weights)
- \( \epsilon \): Error term

---

## Cost Function


To find the best fit line, Linear Regression minimizes the **Mean Squared Error (MSE):**

\[
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

Where:
- \( y_i \): Actual values
- \( \hat{y}_i \): Predicted values
- \( n \): Number of samples

---

## Types of Linear Regression


1. **Simple Linear Regression** – One independent variable.  
   Example: Predicting house price based on square footage.  

2. **Multiple Linear Regression** – Multiple independent variables.  
   Example: Predicting house price based on square footage, location, and number of rooms.  

---

## Example for Linear Regression


```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample dataset
data = {
    "Square_Feet": [1000, 1500, 2000, 2500, 3000],
    "Price": [200000, 250000, 300000, 350000, 400000]
}
df = pd.DataFrame(data)

# Features and target
X = df[["Square_Feet"]]
y = df["Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

```

---

## Advantages

- Easy to implement and interpret.
- Works well with linearly separable data.
- Fast and efficient for small to medium datasets.

## Limitations

- Assumes linear relationship between variables.
- Sensitive to outliers.
- Does not work well with non-linear data.

## Applications

- Predicting house prices.
- Forecasting sales.
- Estimating growth trends
- Risk assessment in finance

## Conclusion 

Linear Regression is a simple yet powerful supervised learning algorithm.
It provides a strong foundation for understanding more complex algorithms in machine learning.