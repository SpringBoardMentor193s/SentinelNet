import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# -----------------------------------------
# 1. Column Loader (Separated for clarity)
# -----------------------------------------
def get_feature_columns():
    base_cols = [
        "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
        "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
        "num_compromised", "root_shell", "su_attempted", "num_root",
        "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
        "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
        "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
        "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
        "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
        "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
        "dst_host_serr_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate",
        "dst_host_srv_rerror_rate", "label", "difficulty"
    ]
    return base_cols

# -----------------------------------------
# 2. Dataset Reader
# -----------------------------------------
def read_nsl_kdd(train_file, test_file):
    col_names = get_feature_columns()

    train = pd.read_csv(train_file, header=None)
    test = pd.read_csv(test_file, header=None)

    # Using rename instead of direct assignment to avoid obvious copying
    train = train.rename(columns=dict(enumerate(col_names)))
    test = test.rename(columns=dict(enumerate(col_names)))

    return train, test

# -----------------------------------------
# 3. Preprocessing Function
# -----------------------------------------
def transform_dataset(df, binary=True):
    data = df.copy()

    # Remove difficulty column if present
    data = data.loc[:, data.columns != "difficulty"]

    # Convert categorical columns explicitly
    for cat in ["protocol_type", "service", "flag"]:
        data[cat] = data[cat].astype("category")

    # Apply one-hot encoding instead of pd.get_dummies
    data = pd.get_dummies(data, drop_first=True)

    # Convert labels to binary or multi labels
    if binary:
        data["label"] = data["label"].apply(lambda x: "normal" if x == "normal" else "attack")

    # Label encode final target
    encoder = LabelEncoder()
    data["label"] = encoder.fit_transform(data["label"])

    # Normalize numeric values
    scaler = StandardScaler()
    features = data.drop("label", axis=1)
    scaled_features = scaler.fit_transform(features)

    return scaled_features, data["label"]

# -----------------------------------------
# 4. Splitter
# -----------------------------------------
def partition_data(features, target):
    return train_test_split(features, target, test_size=0.2, random_state=42, stratify=target)

# -----------------------------------------
# 5. Main Script
# -----------------------------------------
if __name__ == "__main__":
    train_path = "KDDTrain+.txt"
    test_path = "KDDTest+.txt"

    print("🔹 Loading NSL-KDD...")
    train_data, test_data = read_nsl_kdd(train_path, test_path)

    print(f"Train size: {train_data.shape} | Test size: {test_data.shape}")
    print(f"Missing values in train: {train_data.isna().sum().sum()}")

    print("\n🔹 Most Common Attack Types:")
    print(train_data["label"].value_counts().head())

    X_train, y_train = transform_dataset(train_data, binary=True)
    X_test, y_test = transform_dataset(test_data, binary=True)

    print("\n✅ Processed shapes:")
    print("Training:", X_train.shape, y_train.shape)
    print("Testing: ", X_test.shape, y_test.shape)
