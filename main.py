import pandas as pd
import os

# Correct folder path
data_folder = r"C:/Users/Hp/OneDrive/Documents/Desktop/web/SentinelNet/data/NSL-KDD"



print("Files in folder:", os.listdir(data_folder))

# Choose which file to load (KDDTrain+.txt or KDDTest+.txt)
csv_file = "KDDTrain+.txt"
file_path = os.path.join(data_folder, csv_file)

# Load dataset (space-separated)
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

df = pd.read_csv(file_path, sep=",", header=None, names=columns)

print("Dataset loaded successfully. Shape:", df.shape)

# Show first few rows
print(df.head())