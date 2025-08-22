import pandas as pd
from sklearn.preprocessing import MinMaxScaler
cols = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
    'wrong_fragment','urgent','hot','num_failed_logins','logged_in','num_compromised',
    'root_shell','su_attempted','num_root','num_file_creations','num_shells',
    'num_access_files','num_outbound_cmds','is_host_login','is_guest_login',
    'count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate',
    'same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count',
    'dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate',
    'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate',
    'label','difficulty'
]
data=pd.read_csv("../data/nsl-kdd/KDDTrain+.txt",names=cols)

df=pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.describe())

print("Missing values per column:\n",df.isnull().sum())
df=df.dropna()

print("Before removing duplicates:", df.shape)
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

categorical_cols = ['protocol_type', 'service', 'flag']
df = pd.get_dummies(df, columns=categorical_cols)
scaler = MinMaxScaler()
num_cols = df.drop(columns=['label']).columns
df[num_cols] = scaler.fit_transform(df[num_cols])

print("Preprocessed dataset shape:", df.shape)
print(df.head())