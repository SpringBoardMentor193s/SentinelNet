# Load  Dataset

#import library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#assign the names to each columns
columns = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot',
    'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations',
    'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count',
    'serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate',
    'dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate',
    'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','label','difficulty_level'
]
#load the dataset and observe the first 10 rows
dataset=pd.read_csv(r"C:\Users\amity\SentinelNet\data\NSL-KDD\KDDTrain+.txt", header=None, names=columns)

## Explore Basic info:
dataset.head(10)
print(dataset.info())
print(dataset.describe())
# Number of rows, columns
rows, cols = dataset.shape
print(f"Rows: {rows}, Columns: {cols}")
# Unique attack types
unique_attacks = dataset['label'].unique()
print("Unique attack types:", unique_attacks)
# Top 5 frequent attacks
top_attacks = dataset['label'].value_counts().head(5)
print("Top 5 frequent attack types:\n", top_attacks)

## Bar chart of attack categories.

import matplotlib.pyplot as plt
import os

# Ensure the directory exists
os.makedirs("docs/eda", exist_ok=True)

# Plot attack type distribution
plt.figure(figsize=(12,6))
dataset['label'].value_counts().plot(kind='bar', color='skyblue')
plt.title("NSL-KDD Attack Type Distribution")
plt.xlabel("Attack Type")
plt.ylabel("Frequency")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot
plt.savefig("docs/eda/nslkdd_attack_distribution.png")

# Show the plot
plt.show()

# Pie Chart: Normal vs Attack Traffic

# Create a new column to classify normal vs attack
dataset['attack_type'] = dataset['label'].apply(lambda x: 'normal' if x == 'normal' else 'attack')

plt.figure(figsize=(6,6))
dataset['attack_type'].value_counts().plot.pie(
    autopct='%1.1f%%', colors=['skyblue', 'salmon'], startangle=90
)
plt.title("Normal vs Attack Traffic")
plt.ylabel('')  # Remove y-label for clarity
plt.tight_layout()

# Save the pie chart
plt.savefig("docs/eda/nslkdd_normal_vs_attack.png")

# Show the pie chart
plt.show()

##  Preprocessing

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np

# 1. Drop duplicate rows
dataset = dataset.drop_duplicates()
# 2. Handle missing values (NSL-KDD has none, but safer to fill if any)
dataset = dataset.fillna(0)

# 3. Drop unnecessary columns
dataset = dataset.drop(columns=['difficulty_level'], errors='ignore')

# 5. Encode labels
# Binary label: normal=0, attack=1
dataset['binary_label'] = dataset['label'].apply(lambda x: 0 if x == 'normal' else 1)
# Multi-class label: keep original attack names
dataset['multi_label'] = dataset['label']

# 6. Remove original labels from features
X = dataset.drop(columns=['label', 'binary_label', 'multi_label', 'attack_type'], errors='ignore')
y_binary = dataset['binary_label']
y_multi = dataset['multi_label']

# 7. Identify numeric columns for scaling
numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()

# 8. Scale numeric features
scaler = StandardScaler()
X_scaled = X.copy()
X_scaled[numeric_cols] = scaler.fit_transform(X[numeric_cols])

from sklearn.model_selection import train_test_split

# Step 1: Split into train+val (80%) and test (20%)
X_trainval, X_test, y_trainval, y_test = train_test_split(
    X_scaled, y_binary, test_size=0.2, stratify=y_binary, random_state=42
)

# Step 2: Split train+val into train (60%) and validation (20%)
# 0.25 of 80% = 20% validation
X_train, X_val, y_train, y_val = train_test_split(
    X_trainval, y_trainval, test_size=0.25, stratify=y_trainval, random_state=42
)

# Check non-numeric columns (should be 0 after one-hot encoding)
print("Non-numeric columns in X_train:", X_train.select_dtypes(include=['object','bool']).columns.tolist())

# Print shapes
print("Train:", X_train.shape)
print("Validation:", X_val.shape)
print("Test:", X_test.shape)

import matplotlib.pyplot as plt
import seaborn as sns

# Compute correlation matrix for training set
corr_matrix = X_train.corr()

# Set figure size
plt.figure(figsize=(15,12))

# Plot heatmap
sns.heatmap(
    corr_matrix,
    annot=False,        # True agar har cell me value chahiye
    cmap='coolwarm',    # Color palette
    linewidths=0.5,
    vmin=-1, vmax=1
)

plt.title("Correlation Heatmap of NSL-KDD Features (Training Set)", fontsize=16, fontweight='bold')
plt.xlabel("Features")
plt.ylabel("Features")
plt.tight_layout()
plt.show()

from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
)
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define models
# Define models with hyperparameter tweaks
# Define models with hyperparameter tweaks
models = {
    "Random Forest": RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    min_samples_leaf=20,
    min_samples_split=50,
    max_features='sqrt',
    class_weight='balanced',
    random_state=42
),

    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        random_state=42
    ),

    "Decision Tree": DecisionTreeClassifier(
    max_depth=6,
    min_samples_leaf=20,
    min_samples_split=50,
    class_weight='balanced',
    random_state=42
),


    "HistGradientBoosting": HistGradientBoostingClassifier(
    max_depth=6,
    min_samples_leaf=20,
    learning_rate=0.05,
    max_iter=200,
    l2_regularization=0.1,
    early_stopping=True,
    random_state=42
)
}

# Initialize results list
results = []


# 

for name, model in models.items():
    print(f"\n=== {name} ===")
    
    # Train model
    model.fit(X_train, y_train)
    
    # Predict on train, validation, and test sets
    y_train_pred = model.predict(X_train)
    y_val_pred = model.predict(X_val)
    y_test_pred = model.predict(X_test)
    
    # Compute accuracies
    train_acc = accuracy_score(y_train, y_train_pred) * 100
    val_acc = accuracy_score(y_val, y_val_pred) * 100
    test_acc = accuracy_score(y_test, y_test_pred) * 100
    
    print(f"Train Accuracy: {train_acc:.2f}%")
    print(f"Validation Accuracy: {val_acc:.2f}%")
    print(f"Test Accuracy: {test_acc:.2f}%")
    
    # Store predictions in results for later metrics
    results.append({
        "Model": name,
        "Train Accuracy": train_acc,
        "Validation Accuracy": val_acc,
        "Test Accuracy": test_acc,
        "y_test_pred": y_test_pred,
        "model_obj": model
    })

for r in results:
    model = r['model_obj']
    
    # Predictions
    y_train_pred = model.predict(X_train)
    y_val_pred = model.predict(X_val)
    y_test_pred = r['y_test_pred']
    
    # Compute accuracies
    train_acc = accuracy_score(y_train, y_train_pred) * 100
    val_acc = accuracy_score(y_val, y_val_pred) * 100
    test_acc = accuracy_score(y_test, y_test_pred) * 100
    
    # Print accuracies
    print(f"\n=== {r['Model']} ===")
    print(f"Train Accuracy: {train_acc:.2f}%")
    print(f"Validation Accuracy: {val_acc:.2f}%")
    print(f"Test Accuracy: {test_acc:.2f}%")
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_test_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title(f"{r['Model']} Confusion Matrix (Test Set)")
    plt.show()

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Define colors and line styles for clarity
colors = ['blue', 'green', 'red', 'purple']
linestyles = ['-', '--', '-.', ':']

# ---- ROC Curve for Validation Set ----
plt.figure(figsize=(10,7))
for i, r in enumerate(results):
    model = r['model_obj']
    try:
        y_val_prob = model.predict_proba(X_val)[:,1]
    except AttributeError:
        print(f"{r['Model']} does not support predict_proba, skipping ROC for validation.")
        continue
    
    fpr, tpr, _ = roc_curve(y_val, y_val_prob)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, color=colors[i % len(colors)], linestyle=linestyles[i % len(linestyles)],
             linewidth=2, label=f"{r['Model']} (AUC = {roc_auc:.3f})")

plt.plot([0,1], [0,1], color='gray', linestyle='--', label='Random Guess')
plt.xlabel("False Positive Rate", fontsize=12)
plt.ylabel("True Positive Rate", fontsize=12)
plt.title("ROC Curve Comparison (Validation Set)", fontsize=14, fontweight='bold')
plt.legend(loc="lower right", fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


# ---- ROC Curve for Test Set ----
plt.figure(figsize=(10,7))
for i, r in enumerate(results):
    model = r['model_obj']
    try:
        y_test_prob = model.predict_proba(X_test)[:,1]
    except AttributeError:
        print(f"{r['Model']} does not support predict_proba, skipping ROC for test.")
        continue
    
    fpr, tpr, _ = roc_curve(y_test, y_test_prob)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, color=colors[i % len(colors)], linestyle=linestyles[i % len(linestyles)],
             linewidth=2, label=f"{r['Model']} (AUC = {roc_auc:.3f})")

plt.plot([0,1], [0,1], color='gray', linestyle='--', label='Random Guess')
plt.xlabel("False Positive Rate", fontsize=12)
plt.ylabel("True Positive Rate", fontsize=12)
plt.title("ROC Curve Comparison (Test Set)", fontsize=14, fontweight='bold')
plt.legend(loc="lower right", fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.figure(figsize=(12,6))

# Define bright, visible colors
palette_colors = {'Normal':'limegreen', 'Attack':'red'}

# Loop through each model
for r in results:
    model = r['model_obj']
    try:
        y_test_prob = model.predict_proba(X_test)[:,1]  # probability of Attack
    except AttributeError:
        print(f"{r['Model']} does not support predict_proba, skipping box plot.")
        continue
    
    # Prepare DataFrame for plotting
    df_plot = pd.DataFrame({
        'Predicted Probability': y_test_prob,
        'True Label': y_test.map({0:'Normal', 1:'Attack'})
    })
    
    # Horizontal box plot for this model
    sns.boxplot(
        data=df_plot,
        x='Predicted Probability',
        y=pd.Series([r['Model']]*len(df_plot)),  # horizontal orientation
        hue='True Label',
        orient='h',
        palette=palette_colors
    )

plt.title("Predicted Probabilities Box Plot for Test Set", fontsize=16, fontweight='bold')
plt.xlabel("Predicted Probability of Attack", fontsize=13)
plt.ylabel("Model", fontsize=13)
plt.legend(title='True Label', fontsize=12, title_fontsize=13, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Check distributions of predicted probabilities
for r in results:
    model = r['model_obj']
    try:
        y_val_prob = model.predict_proba(X_val)[:,1]
        y_test_prob = model.predict_proba(X_test)[:,1]
        print(r['Model'])
        print("Validation probabilities min/max:", y_val_prob.min(), y_val_prob.max())
        print("Test probabilities min/max:", y_test_prob.min(), y_test_prob.max())
        print("---")
    except AttributeError:
        continue

## Compute sensitivity, specificity, precision, F1, AUC

for r in results:
    cm = confusion_matrix(y_test, r['y_test_pred'])
    tn, fp, fn, tp = cm.ravel()
    
    sensitivity = tp / (tp + fn) * 100
    specificity = tn / (tn + fp) * 100
    precision = precision_score(y_test, r['y_test_pred']) * 100
    f1 = f1_score(y_test, r['y_test_pred']) * 100
    try:
        y_test_prob = r['model_obj'].predict_proba(X_test)[:,1]
        auc = roc_auc_score(y_test, y_test_prob) * 100
    except AttributeError:
        auc = None
    
    # Update results dict
    r.update({
        "Sensitivity (Recall)": sensitivity,
        "Specificity": specificity,
        "Precision": precision,
        "F1-Score": f1,
        "AUC": auc
    })
     # Print metrics for this model
    print(f"\n=== {r['Model']} Metrics ===")
    print(f"Sensitivity (Recall): {sensitivity:.2f}%")
    print(f"Specificity: {specificity:.2f}%")
    print(f"Precision: {precision:.2f}%")
    print(f"F1-Score: {f1:.2f}%")
    if auc is not None:
        print(f"AUC: {auc:.2f}%")

summary_df = pd.DataFrame(results).drop(columns=['y_test_pred','model_obj'])
pd.set_option('display.float_format', '{:.2f}'.format)
print("\n=== NSL-KDD Summary Table ===")
summary_df
