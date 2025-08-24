import pandas as pd

# Load the dataset
path = "NIDS dataset/KDDTest+.txt"
data = pd.read_csv(path, header=None)

# Assign column names
main_features = ["duration", "protocol", "service", "flag", "src_bytes", "dst_bytes", "attack_type"]
other_features = [f"feature_{j}" for j in range(data.shape[1] - len(main_features))]
data.columns = main_features + other_features

# Quick look at data
print("\n=== Random Records Preview ===")
print(data.sample(n=5))

# Dataset overview
print("\nTotal rows and columns:", data.shape)
print("\nData types distribution:")
print(data.dtypes.value_counts())

print("\n=== DataFrame Overview ===")
data.info(verbose=False)

# Missing values check
missing_values = data.isnull().sum()
if missing_values.sum() == 0:
    print("\nNo missing values found.")
else:
    print("\nMissing Values per Column:")
    print(missing_values[missing_values > 0])

# Duplicate rows check
duplicates = data.duplicated().sum()
print(f"\nDuplicate entries in dataset: {duplicates}")

# Numerical stats
print("\n=== Summary of Numeric Columns ===")
print(data.describe(include='all').T)

