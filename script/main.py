import pandas as pd
import matplotlib.pyplot as plt
import os

# output directory creation
#output_dir = "../outputs"
output_dir = "/workspaces/SentinelNet/outputs"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- Function to save plots ---
def save_plot(fig_name):
    plt.savefig(os.path.join(output_dir, fig_name), bbox_inches='tight')
    plt.show()
    plt.close()

# NSL-KDD dataset

# Load dataset
#kdd_file_path = "./data/NSL-KDD/KDDTrain+.txt"
kdd_file_path="/workspaces/SentinelNet/data/NSL-KDD/KDDTrain+.txt"

try:
    df = pd.read_csv(kdd_file_path, header=None, sep=',')
except FileNotFoundError:
    print(f"File not found: {kdd_file_path}")
    exit()

# Rename columns
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
print("\nTop 5 attack types:")
print(df["outcome"].value_counts().head(5))

# attack types
plt.figure(figsize=(10, 6))
df["outcome"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Attack Types in NSL-KDD Dataset")
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.xticks(rotation=90)
#plt.show()
save_plot("kdd_attack_types.png")


print("\n--- Dataset Overview ---")
print(df.head())
print(df.info())
print(df.describe())

print("\nFeature Types:")
print(df.dtypes)

# Map attacks
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

# Plot attack 
plt.figure(figsize=(6,4))
df['category'].value_counts().plot(kind='bar')
plt.title("Attack Categories in NSL-KDD")
plt.xlabel("Category")
plt.ylabel("Count")
#plt.show()
save_plot("kdd_attack_categories.png")

print("\nClass Imbalance Check (%):")
imbalance = (df['category'].value_counts() / len(df)) * 100
print(imbalance)

print("Current working directory:", os.getcwd())


# CICIDS2017 Dataset

cicids_file_path = "/workspaces/SentinelNet/data/CICIDS-2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

try:
    cicids = pd.read_csv(cicids_file_path)
    print("\nCICIDS2017 Dataset Loaded")
    print("Shape:", cicids.shape)

    
    label_col = None
    for col in cicids.columns:
        if col.strip().lower() == "label":
            label_col = col
            break

    if label_col:
        print("\nUnique attack types:", cicids[label_col].nunique())
        print("\nTop 5 frequent attack types:\n", cicids[label_col].value_counts().head())

        # Plot top 10 attacks
        top_attacks = cicids[label_col].value_counts().head(10)
        plt.figure(figsize=(10,6))
        top_attacks.plot(kind="bar")
        plt.title("Top 10 Attack Types in CICIDS2017 Dataset")
        plt.xlabel("Attack Type")
        plt.ylabel("Count")
        plt.xticks(rotation=90)
        save_plot("cicids_top10_attack_types.png")  # <- plot saved here

        
        total = len(cicids)
        imbalance = (cicids[label_col].value_counts() / total) * 100
        print("\nClass Imbalance Check (%):")
        print(imbalance)
    else:
        print("No 'label' column found in CICIDS dataset.")

    # Dataset overview
    print("\n--- CICIDS Dataset Overview ---")
    print(cicids.head())
    print(cicids.info())
    print(cicids.describe())

    # Missing values
    print("\nMissing values per column:")
    print(cicids.isnull().sum())

except FileNotFoundError:
    print(f"CICIDS file not found: {cicids_file_path}")

