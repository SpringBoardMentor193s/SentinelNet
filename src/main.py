import pandas as pd
import matplotlib.pyplot as plt

# Column names 
col_names = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent',
    'hot','num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root',
    'num_file_creations','num_shells','num_access_files','num_outbound_cmds','is_host_login',
    'is_guest_login','count','srv_count','serror_rate','srv_serror_rate','rerror_rate',
    'srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count',
    'dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
    'dst_host_rerror_rate','dst_host_srv_rerror_rate','label'
]

# Load the dataset
file_path = "data/NSL-KDD/KDDTrain+.txt"
df = pd.read_csv(file_path, names=col_names)

print(df.head())
print(df.info())
print(df.describe())

#missing values and duplicates
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
# Remove duplicates
df = df.drop_duplicates()


print("Number of rows:", df.shape[0])
print("Unique labels:", df['label'].nunique())
print("Top 5 frequent attack types:\n", df['label'].value_counts().head(5))


#Attack data visualization
attack_counts = df['label'].value_counts()
attack_counts.plot(kind='bar', figsize=(12,6))
plt.title("Attack Type Distribution")
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/attack_distribution.png")
plt.show()
