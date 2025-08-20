import pandas as pd
import matplotlib.pyplot as plt


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
plt.xlabel("Attack Type")
plt.ylabel("Count")
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
