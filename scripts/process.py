import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

train_path = BASE_DIR / 'data' / 'NSL-KDD' / 'KDDTrain+.txt'
test_path = BASE_DIR / 'data' / 'NSL-KDD' / 'KDDTest+.txt'

df_train = pd.read_csv(train_path, header=None)
df_test = pd.read_csv(test_path, header=None)

print("Train shape:", df_train.shape)
print("Test shape:", df_test.shape)

print("\n--- Train Head ---")
print(df_train.head())

print("\n--- Train Info ---")
print(df_train.info())

print("\n--- Train Describe ---")
print(df_train.describe())

label_col = df_train.columns[-1]

print("\nUnique labels:", df_train[label_col].nunique())
print("Labels:", df_train[label_col].unique())

print("\nTop 5 frequent attack types:")
print(df_train[label_col].value_counts().head())

plt.figure(figsize=(12, 6))
df_train[label_col].value_counts().plot(kind='bar')
plt.title("Attack Type Distribution (Train Set)")
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
