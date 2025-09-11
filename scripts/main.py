import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# ----------------------------
# Load Dataset
# ----------------------------
def load_data(train_path, test_path):
    columns = [
        "duration","protocol_type","service","flag","src_bytes","dst_bytes",
        "land","wrong_fragment","urgent","hot","num_failed_logins","logged_in",
        "num_compromised","root_shell","su_attempted","num_root","num_file_creations",
        "num_shells","num_access_files","num_outbound_cmds","is_host_login",
        "is_guest_login","count","srv_count","serror_rate","srv_serror_rate",
        "rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate",
        "srv_diff_host_rate","dst_host_count","dst_host_srv_count",
        "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
        "dst_host_srv_diff_host_rate","dst_host_serr_rate","dst_host_srv_serror_rate",
        "dst_host_rerror_rate","dst_host_srv_rerror_rate","label","difficulty"
    ]

    train_df = pd.read_csv(train_path, header=None)
    test_df = pd.read_csv(test_path, header=None)

    train_df.columns = columns
    test_df.columns = columns

    return train_df, test_df

# ----------------------------
# Preprocessing
# ----------------------------
def preprocess_data(df, binary=True):
    # Drop difficulty column (not useful for classification)
    if 'difficulty' in df.columns:
        df = df.drop('difficulty', axis=1)

    # Encode categorical features
    categorical_cols = ['protocol_type', 'service', 'flag']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Convert labels
    if binary:
        df['label'] = df['label'].apply(lambda x: 'normal' if x == 'normal' else 'attack')
    
    le = LabelEncoder()
    df['label'] = le.fit_transform(df['label'])

    # Separate features and target
    X = df.drop('label', axis=1)
    y = df['label']

    # Scale numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

# ----------------------------
# Train-Test Split
# ----------------------------
def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    train_path = "KDDTrain+.txt"
    test_path = "KDDTest+.txt"

    print("Loading dataset...")
    train_df, test_df = load_data(train_path, test_path)
    print("Train shape:", train_df.shape, "Test shape:", test_df.shape)

    print("Checking missing values in train data:")
    print(train_df.isnull().sum().sum())

    print("Top 5 frequent attack types in train data:")
    print(train_df['label'].value_counts().head())

    print("Preprocessing train and test datasets...")
    X_train, y_train = preprocess_data(train_df, binary=True)
    X_test, y_test = preprocess_data(test_df, binary=True)

    print("Final Train shape:", X_train.shape, y_train.shape)
    print("Final Test shape:", X_test.shape, y_test.shape)
