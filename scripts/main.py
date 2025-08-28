import pandas as pd

train_data = pd.read_csv("KDDTrain+.txt", header=None)
test_data=pd.read_csv("KDDTest+.txt",header=None)

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

train_data.columns = columns
test_data.columns = columns
print(train_data.head())
print(test_data.head())

# Number of rows
print("Rows & Columns:", df.shape)

# Unique labels
print("Unique labels:", df.iloc[:, -1].unique())

# Top 5 frequent attack types
print("Top 5 frequent attacks:")
print(df.iloc[:, -1].value_counts().head())

