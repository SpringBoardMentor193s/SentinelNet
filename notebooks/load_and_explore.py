import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
# ----------------------------
# Load NSL-KDD dataset
# ----------------------------
nsl_kdd_path = r"C:\Users\amity\SentinelNet\data\NSL-KDD"
print("NSL-KDD files:", os.listdir(nsl_kdd_path))

# Load training dataset
nsl_train = pd.read_csv(os.path.join(nsl_kdd_path, "KDDTrain+.txt"), header=None)



# Define column names
columns = [
    "duration","protocol_type","service","flag","src_bytes","dst_bytes",
    "land","wrong_fragment","urgent","hot","num_failed_logins","logged_in",
    "num_compromised","root_shell","su_attempted","num_root","num_file_creations",
    "num_shells","num_access_files","num_outbound_cmds","is_host_login",
    "is_guest_login","count","srv_count","serror_rate","srv_serror_rate",
    "rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate",
    "srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
    "dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate",
    "label","difficulty"
]

nsl_train.columns = columns
print("\n--- Columns Assigned ---")
print(nsl_train.head())

# Dataset Overview
print("\n--- First 5 rows ---")
print(nsl_train.head())

print("\n--- Dataset Info ---")
print(nsl_train.info())

print("\n--- Feature types ---")
print(nsl_train.dtypes)

print("\n--- Missing values ---")
print(nsl_train.isnull().sum())



#Explore target variable (attack types)
print("\n--- Label Distribution ---")
print(nsl_train['label'].value_counts())

#Attack Categories Mapping
# Mapping dictionary
attack_types = {
    'normal': 'normal',

    # DOS Attacks
    'back': 'dos','land': 'dos','neptune': 'dos','pod': 'dos','smurf': 'dos','teardrop': 'dos',

    # Probe Attacks
    'satan': 'probe','ipsweep': 'probe','nmap': 'probe','portsweep': 'probe',

    # R2L Attacks
    'ftp_write': 'r2l','guess_passwd': 'r2l','imap': 'r2l','multihop': 'r2l',
    'phf': 'r2l','spy': 'r2l','warezclient': 'r2l','warezmaster': 'r2l',

    # U2R Attacks
    'buffer_overflow': 'u2r','loadmodule': 'u2r','perl': 'u2r','rootkit': 'u2r'
}


# Add new column for attack category
nsl_train['attack_category'] = nsl_train['label'].map(attack_types)

#NSL-KDD SUMMARY
print("\n================ NSL-KDD SUMMARY ================")
print("Rows:", nsl_train.shape[0])
print("Features:", nsl_train.shape[1])
print("Unique attack labels:", nsl_train['label'].nunique())
print("Attack categories:", nsl_train['attack_category'].unique())
print("Top 5 frequent attacks:\n", nsl_train['label'].value_counts().head(5))

print("\n--- Attack Category Distribution ---")
print(nsl_train['attack_category'].value_counts())


#Dataset Shape & Stats
print("\n--- NSL-KDD Shape ---")
print(nsl_train.shape)

print("\n--- NSL-KDD Label Distribution ---")
print(nsl_train['label'].value_counts())

print("\n--- NSL-KDD Attack Category Distribution ---")
print(nsl_train['attack_category'].value_counts())

print("\n--- NSL-KDD Numeric Stats ---")
print(nsl_train.describe())



#Groupwise Analysis
print("\n--- Grouped Label Counts ---")
print(nsl_train.groupby(['attack_category', 'label']).size())



# Bar chart for attack categories
nsl_train['attack_category'].value_counts().plot(kind='bar', figsize=(6,4))
plt.title("Attack Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

print("Rows:", nsl_train.shape[0])
print("Unique attack labels:", nsl_train['label'].nunique())
print("Top 5 attacks:", nsl_train['label'].value_counts().head(5))
# ------------------------------
# ------------------------------
# 1) NSL-KDD attack categories
# ------------------------------
plt.figure(figsize=(6, 4))
nsl_train['attack_category'].value_counts().sort_values(ascending=False).plot(kind='bar')
plt.title("NSL-KDD Attack Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ------------------------------
# 2) NSL-KDD fine-grained labels
# ------------------------------
plt.figure(figsize=(12, 5))
nsl_train['label'].value_counts().sort_values(ascending=False).plot(kind='bar')
plt.title("NSL-KDD Attack Type Distribution (Fine-grained)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ------------------------------
# ------------------------------
# 3) CICIDS2017 attack types
# ------------------------------
cicids_path = r"C:\Users\amity\SentinelNet\data\CICIDS2017"
files = sorted(glob.glob(os.path.join(cicids_path, "*.csv")))
if not files:
    print("No CSV files found in CICIDS2017 folder!")
else:
    # Concatenate all CSVs
    df_cic = pd.concat((pd.read_csv(f, low_memory=False) for f in files), ignore_index=True)

    # Detect the label column
    for col in ['Label', 'label', 'class']:
        if col in df_cic.columns:
            label_col = col
            break
    else:
        raise ValueError("No label column found in CICIDS2017 dataset!")

    # Clean label strings
    df_cic[label_col] = df_cic[label_col].astype(str).str.strip()

    # CICIDS2017 Summary
    print("\n================ CICIDS2017 SUMMARY ================")
    print("Rows:", df_cic.shape[0])
    print("Features:", df_cic.shape[1])
    print("Unique attack labels:", df_cic[label_col].nunique())
    print("Sample attack labels:", df_cic[label_col].unique()[:10])
    print("Top 5 frequent attacks:\n", df_cic[label_col].value_counts().head(5))

    # ------------------------------
    # Comparison with NSL-KDD
    # ------------------------------
    print("\n================ COMPARISON ================")
    print("NSL-KDD: Smaller (~125k rows), 43 features, older dataset (1999 DARPA), 4 attack categories.")
    print("CICIDS2017: Much larger (millions of rows), ~80+ features, modern attacks (DDoS, Botnet, Web, etc.), realistic network traffic.")

    # ------------------------------
    # CICIDS2017: Plot top 20 attack types
    # ------------------------------
    plt.figure(figsize=(12, 5))
    df_cic[label_col].value_counts().head(20).plot(kind='bar')
    plt.title("CICIDS2017 Attack Type Distribution (Top 20)")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Final stats
    print("\nCICIDS2017 Rows:", df_cic.shape[0])
    print("Unique attack labels:", df_cic[label_col].nunique())
    print("Top 5 attacks:\n", df_cic[label_col].value_counts().head(5))
