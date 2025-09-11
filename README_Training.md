# SentinelNet ‒ Model Training & Evaluation

This section explains how to train the ML models and evaluate them.

---

## Training

- The training logic is likely in `Scripts/` and/or `main.py`.  
- You’ll need clean, preprocessed data (see Data Preparation README) before training.  
- Hyperparameters (learning rate, number of estimators, depth, etc.) may be set/configured in code or via configuration files (if used).

---

## Evaluation Metrics

Common metrics for Network Intrusion Detection Systems include:

- Accuracy  
- Precision  
- Recall  
- F1‑Score  
- ROC AUC (to see trade‑off between true positive rate & false positive rate)  
- Confusion Matrix (to see false positives vs false negatives)

---

## Generating Reports & Visualizations

- Confusion matrices and ROC curves are helpful.  
- Use plots to show model performance (e.g. via matplotlib / seaborn).  
- Save model evaluation results in logs or output files for reproducibility.

---

## Example Training Workflow

```python
# Pseudocode

from Scripts.preprocessing import load_data, preprocess
from Scripts.model import train_model, evaluate_model

# Load and preprocess
X_train, X_test, y_train, y_test = load_data(...)
X_train_prep, X_test_prep = preprocess(X_train, X_test)

# Train
model = train_model(X_train_prep, y_train, hyperparams={...})

# Evaluate
metrics = evaluate_model(model, X_test_prep, y_test)
print(metrics)
# Save plots/reports
```

---

## Saving Model

- After training, save the final model (e.g. using joblib / pickle) so it can be reused without retraining.  
- Store versioned model files into a directory (e.g. `models/` if you create one).
