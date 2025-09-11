# Performance Metrics

## 1. Confusion Matrix
A Confusion Matrix is a table that describes the performance of a classification model on a set of test data for which the true values are known.

	Predicted Positive	Predicted Negative
Actual Positive	True Positive (TP)	False Negative (FN)
Actual Negative	False Positive (FP)	True Negative (TN)

## 2. Accuracy
Accuracy measures the overall correctness of the model:

Acc=(TP+TN)/(TP+TN+FP+FN)

## 3. Precision
Precision is the ratio of correctly predicted positive observations to total predicted positives.

Precision=(TP)/(TP+FP)

## 4. Recall (Sensitivity)

Recall is the ratio of correctly predicted positive observations to all actual positives.

Recall=(TP)/(TP+FN)

## 5. F1-Score
The F1-Score is the harmonic mean of Precision and Recall.

F1-score=2*(Precision*Recall)/(precision+recall)

## ROC CURVE(Receiver Operating Characteristic) AND AUC(Area Under Curve)
- The ROC Curve plots True Positive Rate (Recall) vs False Positive Rate (FPR).
FPR=FP/(FP+TN)
- AUC indicates how well the model separates the classes (higher is better).