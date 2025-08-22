import pandas as pd
import os
import matplotlib.pyplot as plt
# ----------------------------
# Load NSL-KDD dataset
# ----------------------------
nsl_kdd_path = r"C:\Users\amity\SentinelNet\data\NSL-KDD"
print("NSL-KDD files:", os.listdir(nsl_kdd_path))


# Load training dataset
nsl_train = pd.read_csv(os.path.join(nsl_kdd_path, "KDDTrain+.txt"), header=None)

# Quick look
print("\n--- First 5 rows ---")
print(nsl_train.head())

print("\n--- Dataset Info ---")
print(nsl_train.info())

print("\n--- Feature types ---")
print(nsl_train.dtypes)

print("\n--- Missing values ---")
print(nsl_train.isnull().sum())


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

print("\n--- Attack Category Distribution ---")
print(nsl_train['attack_category'].value_counts())


#Dataset Shape & Stats
print("\n--- Dataset Shape ---")
print(nsl_train.shape)

print("\n--- Numeric Features Stats ---")
print(nsl_train.describe())


#Groupwise Analysis
print("\n--- Grouped Label Counts ---")
print(nsl_train.groupby(['attack_category', 'label']).size())


#

# Bar chart for attack categories
nsl_train['attack_category'].value_counts().plot(kind='bar', figsize=(6,4))
plt.title("Attack Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
nsl_train['attack_category'].value_counts().plot(kind='bar')
plt.title("Attack Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")

# Save the figure in docs folder
plt.savefig("docs/attack_category_distribution.png", dpi=300)

plt.show()
