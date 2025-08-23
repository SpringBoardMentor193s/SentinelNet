import pandas as pd

file_path = "NIDS dataset/KDDTest+.txt"
df = pd.read_csv(file_path, header=None)

base_cols = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "label"]
extra_cols = [f"extra_{i}" for i in range(df.shape[1] - len(base_cols))]
df.columns = base_cols + extra_cols

print(" Dataset Preview:")
print(df.sample(5))   

print("\n Shape of dataset:", df.shape)
print(" Column Data Types:")
print(df.dtypes.value_counts())

print("\n DataFrame Info:")
df.info(verbose=True)

missing = df.isna().sum()
print("\n Missing Values (per column):")
print(missing[missing > 0] if missing.sum() > 0 else "No missing values")

dup_count = df.duplicated().sum()
print(f"\n Number of duplicate rows: {dup_count}")

print("\n Numerical Columns Summary:")
print(df.describe().T)
