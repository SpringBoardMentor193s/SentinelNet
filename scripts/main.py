#Libraries
import pandas as pd
import matplotlib.pyplot as plt

#Loading Dataset
path=r"..\data\KDDTrain+.txt"
data=pd.read_csv(path,delimiter=",")

#Naming the columns
columns=['duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot'
,'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations'
,'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count','serror_rate'
,'srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count'
,'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate'
,'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','outcome','level']

data.columns=columns

# No of rows
print("NO OF ROWS:")
print(len(data))

#No of Unique Labels
print('NO OF UNIQUE LABELS:')
labels=data.iloc[:,-2]
print(labels.unique())
# or data['outcome'].unique()

#Top 5 freq attack type
print('Top 5 Frequent attack types:')
print(labels.value_counts().head(5))

#Bar chart showing distribution of attack types.
label_count=labels.value_counts()
plt.figure(figsize=(12,6))
label_count.plot(kind='bar')
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

#Basic inspection
print('First 5 rows:')
print(data.head())
print('Last 5 rows:')
print(data.tail())
print('Structure of dataset')
print(data.info())
print('Statistical summary')
print(data.describe())

#Feature types
print('Feature types:')
print(data.dtypes)