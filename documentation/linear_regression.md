# Linear Regression - From what I understood

Linear Regression is one of the simplest and most widely used algorithms in Machine Learning.  
If you’ve ever tried to draw a straight line through a set of points to see the trend, you’ve already done a version of linear regression!

---

## What is Linear Regression?

Linear Regression is a method to model the relationship between a **dependent variable (Y)** and one or more **independent variables (X)**.  
The goal is simple: find the best-fitting straight line that predicts Y from X.

In its simplest form (with one independent variable), the equation looks like this:

\[
Y = mX + c
\]

- **Y** → Dependent variable (what we want to predict)  
- **X** → Independent variable (input)  
- **m** → Slope of the line  
- **c** → Intercept (value of Y when X = 0)

If there are multiple features (X₁, X₂, X₃...), the equation becomes:

\[
Y = b_0 + b_1X_1 + b_2X_2 + ... + b_nX_n
\]

---

## How Does It Work?

1. **Collect Data** → Example: House prices vs square footage.  
2. **Plot Data** → See if the relationship looks roughly like a line.  
3. **Fit a Line** → The algorithm finds the line that minimizes the error between predicted and actual values.  
   - The error is often measured using **Mean Squared Error (MSE)**.  
4. **Make Predictions** → Once the line is fitted, you can plug in new X values to predict Y.  

---

## Types of Linear Regression

- **Simple Linear Regression** – One independent variable.  
- **Multiple Linear Regression** – Two or more independent variables.  

---

## Assumptions of Linear Regression

Before trusting the model, check these assumptions:

1. **Linearity** – Relationship between X and Y should be linear.  
2. **Independence** – Observations are independent of each other.  
3. **Homoscedasticity** – Constant variance of errors.  
4. **Normality of Errors** – Errors should be normally distributed.  
5. **No Multicollinearity** (in multiple regression) – Features should not be highly correlated with each other.  

---

##  Advantages

- Very simple to implement and interpret.  
- Works well when the relationship is approximately linear.  
- Computationally efficient.  

---

##  Limitations

- Struggles when the relationship is not linear.  
- Sensitive to outliers.  
- Requires those assumptions (above) to hold true.  

---
PS: I have included a pretty basic implementation of linear regression on two different datasets and compared their accuracy and efficieny. Do check it out in the /notebooks folder !
---
