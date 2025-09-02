import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# NSL-KDD Dataset


# Load dataset
df = pd.read_csv("./data/KDDTrain+.txt", header=None)

# Rename columns immediately
columns = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot',
    'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations',
    'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count',
    'serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
    'srv_diff_host_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
    'dst_host_rerror_rate','dst_host_srv_rerror_rate','outcome','level'
]
df.columns = columns


print("Number of rows:", len(df))
print("\nUnique labels in outcome:", df["outcome"].unique())

# Top 5 frequent attack types
print("\nTop 5 attack types:")
print(df["outcome"].value_counts().head(5))

# Plot attack distribution
attack_counts = df["outcome"].value_counts().head(10)
plt.figure(figsize=(10, 6))
attack_counts.plot(kind="bar")
plt.title("Top 10 Attack Types in NSL-KDD Dataset")
plt.xlabel("Attack Type", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=90)
plt.show()


# Dataset overview
print("\n--- Dataset Overview ---")
print(df.head())
print(df.info())
print(df.describe())

print("\nFeature Types:")
print(df.dtypes)

# Group attacks into broader categories
attack_mapping = {
    'neptune': 'DoS', 'smurf': 'DoS', 'back': 'DoS', 'teardrop': 'DoS', 'pod': 'DoS',
    'satan': 'Probe', 'ipsweep': 'Probe', 'nmap': 'Probe', 'portsweep': 'Probe',
    'guess_passwd': 'R2L', 'ftp_write': 'R2L', 'imap': 'R2L', 'phf': 'R2L',
    'multihop': 'R2L', 'warezmaster': 'R2L', 'warezclient': 'R2L',
    'buffer_overflow': 'U2R', 'loadmodule': 'U2R', 'rootkit': 'U2R', 'perl': 'U2R',
    'normal': 'Normal'
}
df['category'] = df['outcome'].map(attack_mapping).fillna('Other')

print("\nAttack categories distribution:")
print(df['category'].value_counts())

# Plot categories
df['category'].value_counts().plot(kind='bar', figsize=(6,4))
plt.title("Attack Categories in NSL-KDD")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Class imbalance check
print("\nClass Imbalance Check (%):")
total = len(df)
imbalance = (df['category'].value_counts() / total) * 100
print(imbalance)



# CICIDS2017 Dataset


# Load dataset
cicids = pd.read_parquet("./data/DoS-Wednesday-no-metadata.parquet")

print("\nCICIDS2017 Dataset Loaded")
print("Shape:", cicids.shape)

if "Label" in cicids.columns:
    print("\nUnique attack types:", cicids["Label"].nunique())
    print("\nTop 5 frequent attack types:\n", cicids["Label"].value_counts().head())

    cicids["Label"].value_counts().plot(kind="bar", figsize=(8,5))
    plt.title("CICIDS2017 Attack Type Distribution")
    plt.xlabel("Attack Type")
    plt.ylabel("Count")
    plt.show()

print("\n--- CICIDS Dataset Overview ---")
print(cicids.head())
print(cicids.info())
print(cicids.describe())


# Categorical vs Numerical features

print("\nCategorical vs Numerical Features (NSL-KDD):")
categorical_features = df.select_dtypes(include=["object"]).columns.tolist()
numerical_features = df.select_dtypes(exclude=["object"]).columns.tolist()

print("Categorical:", categorical_features)
print("Numerical:", numerical_features)


print("\nCategorical vs Numerical Features (CICIDS2017):")
categorical_features_cicids = cicids.select_dtypes(include=["object"]).columns.tolist()
numerical_features_cicids = cicids.select_dtypes(exclude=["object"]).columns.tolist()

print("Categorical:", categorical_features_cicids)
print("Numerical:", numerical_features_cicids)


# Check for missing values and duplicates

print("\nMissing values check (NSL-KDD):")
print(df.isnull().sum().sum(), "missing values")

print("Duplicate rows in NSL-KDD:", df.duplicated().sum())

print("\nMissing values check (CICIDS2017):")
print(cicids.isnull().sum().sum(), "missing values")

print("Duplicate rows in CICIDS2017:", cicids.duplicated().sum())


# Schema mapping table

def create_schema(df, dataset_name):
    schema = []
    for col in df.columns:
        dtype = str(df[col].dtype)
        if col in categorical_features or col in categorical_features_cicids:
            feature_type = "categorical"
            action = "encode (one-hot/label)"
        elif dtype in ["int64", "float64"]:
            feature_type = "numerical"
            action = "scale/normalize"
        else:
            feature_type = "binary"
            action = "keep as is"

        # semantic categories
        if "bytes" in col or "count" in col or "rate" in col:
            semantic = "traffic"
        elif "login" in col or "shell" in col or "root" in col:
            semantic = "privilege"
        elif "flag" in col or "protocol" in col or "service" in col:
            semantic = "behavior"
        elif col in ["outcome", "Label", "category"]:
            semantic = "target"
        else:
            semantic = "other"

        schema.append([col, feature_type, action, semantic])

    schema_df = pd.DataFrame(schema, columns=["Feature", "Type", "Preprocessing Action", "Semantic Category"])
    print(f"\nSchema mapping for {dataset_name}:")
    print(schema_df.head(15))  
    return schema_df


schema_nsl = create_schema(df, "NSL-KDD")
schema_cicids = create_schema(cicids, "CICIDS2017")


#Feature Scaling & Train-Test Split

#NSL-KDD
X_nsl = df.drop(columns=['outcome', 'category', 'level'])
y_nsl = df['category']

# Scale numerical features
numerical_features_nsl = X_nsl.select_dtypes(include=['int64', 'float64']).columns
scaler_nsl = StandardScaler()
X_nsl_scaled = X_nsl.copy()
X_nsl_scaled[numerical_features_nsl] = scaler_nsl.fit_transform(X_nsl_scaled[numerical_features_nsl])
X_nsl = X_nsl_scaled

# Train-test split
X_train_nsl, X_test_nsl, y_train_nsl, y_test_nsl = train_test_split(
    X_nsl, y_nsl, test_size=0.2, random_state=42, stratify=y_nsl
)

print("\nNSL-KDD: Train shape:", X_train_nsl.shape, "Test shape:", X_test_nsl.shape)

#CICIDS2017 
if "Label" in cicids.columns:
    X_cic = cicids.drop(columns=['Label'])
    y_cic = cicids['Label']

    numerical_features_cic = X_cic.select_dtypes(include=['int64', 'float64']).columns
    scaler_cic = StandardScaler()
    X_cic_scaled = X_cic.copy()
    X_cic_scaled[numerical_features_cic] = scaler_cic.fit_transform(X_cic_scaled[numerical_features_cic])
    X_cic = X_cic_scaled

    # Train-test split
    X_train_cic, X_test_cic, y_train_cic, y_test_cic = train_test_split(
        X_cic, y_cic, test_size=0.2, random_state=42, stratify=y_cic
    )

    print("\nCICIDS2017: Train shape:", X_train_cic.shape, "Test shape:", X_test_cic.shape)
