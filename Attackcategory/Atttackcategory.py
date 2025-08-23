#Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
#  Define column names (from NSL-KDD dataset)
columns = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment',
    'urgent','hot','num_failed_logins','logged_in','num_compromised','root_shell','su_attempted',
    'num_root','num_file_creations','num_shells','num_access_files','num_outbound_cmds',
    'is_host_login','is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
    'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate',
    'dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate',
    'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate',
    'outcome','level'
]
# Load Train & Test dataset
train = pd.read_csv(r"D:\SpringBoard\Datasets_nslkdd\KDDTrain+.txt", names=columns)
test  = pd.read_csv(r"D:\SpringBoard\Datasets_nslkdd\KDDTest+.txt", names=columns)

print("Train shape:", train.shape)
print("Test shape:", test.shape)


#  Define Attack Categories (as per NSL-KDD)
dos = ['back','land','neptune','pod','smurf','teardrop']
probe = ['satan','ipsweep','nmap','portsweep']
r2l = ['guess_passwd','ftp_write','imap','phf','multihop','warezmaster','warezclient','spy']
u2r = ['buffer_overflow','loadmodule','perl','rootkit']

#Define Mapping Function

def map_attack_category(label):
    """ Map each attack outcome to a broader category """
    if label == "normal":
        return "normal"
    elif label in dos:
        return "dos"
    elif label in probe:
        return "probe"
    elif label in r2l:
        return "r2l"
    elif label in u2r:
        return "u2r"
    else:
        return "unknown"


# Apply Function to Train & Test
train["attack_category"] = train["outcome"].apply(map_attack_category)
test["attack_category"]  = test["outcome"].apply(map_attack_category)
# Explore Dataset
print("\n🔹 First 10 rows of outcome → attack_category mapping:")
print(train[["outcome","attack_category"]].head(10))

print("\n🔹 Count of categories in Train dataset:")
print(train["attack_category"].value_counts())

print("\n🔹 Count of categories in Test dataset:")
print(test["attack_category"].value_counts())
#  Plot Category Distribution (your method)
counts = train['attack_category'].value_counts().sort_values(ascending=False)
plt.figure()
counts.plot(kind='bar')
plt.title("Attack Category Distribution (Train)")
plt.xlabel("Category")
plt.ylabel("Count")
plt.grid()
plt.show()
plt.legend()

