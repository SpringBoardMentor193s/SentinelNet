import pandas as pd
import matplotlib.pyplot as plt

# Paths (relative so it's portable)
train_path = r"C:\Users\ASUS\OneDrive\Desktop\Project\SentinelNet\Data\KDDTrain+.txt"
test_path  = r"C:\Users\ASUS\OneDrive\Desktop\Project\SentinelNet\Data\KDDTest+.txt"


# Load datasets (no header in NSL-KDD raw files)
df_train = pd.read_csv(train_path, header=None)
df_test = pd.read_csv(test_path, header=None)

print("Train shape:", df_train.shape)
print("Test shape:", df_test.shape)

# =========================
# 1. Basic inspection
# =========================
print("\n--- Train Head ---")
print(df_train.head())

print("\n--- Train Info ---")
print(df_train.info())

print("\n--- Train Describe ---")
print(df_train.describe())

# =========================
# 2. Label column (last column in NSL-KDD)
# =========================
label_col = df_train.columns[-1]

print("\nUnique labels:", df_train[label_col].nunique())
print("Labels:", df_train[label_col].unique())

# Top 5 most frequent attacks
print("\nTop 5 frequent attack types:")
print(df_train[label_col].value_counts().head())

# =========================
# 3. Plot distribution of attack types
# =========================
plt.figure(figsize=(12, 6))
df_train[label_col].value_counts().plot(kind='bar')
plt.title("Attack Type Distribution (Train Set)")
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
