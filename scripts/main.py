#Libraries
import pandas as pd
import matplotlib.pyplot as plt
import IPython.display as display #For better visualization
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

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

#Mapping attacks into categories
attack_categories = {
    'normal': 'Normal',
    # DoS
    'back': 'DoS','land': 'DoS','neptune': 'DoS','pod': 'DoS','smurf': 'DoS','teardrop': 'DoS',
    'mailbomb': 'DoS','apache2': 'DoS','processtable': 'DoS','udpstorm': 'DoS',
    # Probe
    'satan': 'Probe','ipsweep': 'Probe','nmap': 'Probe','portsweep': 'Probe',
    'mscan': 'Probe','saint': 'Probe',
    # U2R
    'buffer_overflow': 'U2R','loadmodule': 'U2R','perl': 'U2R','rootkit': 'U2R',
    'xterm': 'U2R','ps': 'U2R','sqlattack': 'U2R','httptunnel': 'U2R',
    # R2L
    'ftp_write': 'R2L','guess_passwd': 'R2L','imap': 'R2L','multihop': 'R2L',
    'phf': 'R2L','spy': 'R2L','warezclient': 'R2L','warezmaster': 'R2L',
    'sendmail': 'R2L','named': 'R2L','snmpgetattack': 'R2L','snmpguess': 'R2L',
    'worm': 'R2L','xlock': 'R2L','xsnoop': 'R2L'
}

#Create a new column for category
data['category'] = data['outcome'].map(attack_categories)

#Frequency count
print("\nAttack Category Distribution:")
print(data['category'].value_counts())

#Plot bar chart for categories
plt.figure(figsize=(8,6))
data['category'].value_counts().plot(kind='bar', color='skyblue')
plt.xlabel('Attack Category')
plt.ylabel('Count')
plt.title('Attack Category Distribution in NSL-KDD')
plt.tight_layout()
plt.show()

#Identify categorical vs. numerical features
categorical_features = data.select_dtypes(include=['object']).columns.tolist()
numerical_features = data.select_dtypes(exclude=['object']).columns.tolist()
print("Categorical Features:", categorical_features)
print("Numerical Features:", numerical_features)

#Checking for missing values and duplicates
#Missing values
print("Missing values per column:")
print(data.isnull().sum())
#For duplicates
num_duplicates = data.duplicated().sum()
print(f"Number of duplicate rows: {num_duplicates}")

#Create a schema mapping table
binary = {"land","logged_in","root_shell","su_attempted","is_host_login","is_guest_login"}
drop = {"num_outbound_cmds","is_host_login","level"}
special = {"src_bytes":"Log-transform + Normalize","dst_bytes":"Log-transform + Normalize"}
labels = {"outcome":"Label encode","category":"Label encode"}
def infer_type(col, s):
    if col in binary: return "Binary"
    if s.dtype=="object": return "Categorical"
    return "Numerical"
def preprocessing(col, t):
    if col in drop: return "Drop"
    if col in special: return special[col]
    if col in labels: return labels[col]
    if t=="Binary": return "Keep as is (0/1)"
    if t=="Categorical": return "One-hot encode / Label encode"
    if t=="Numerical": return "Already normalized" if "_rate" in col else "Normalize/Standardize"
    return "Check"
schema = [{"Feature":c,
           "Type":infer_type(c,data[c]),
           "Preprocessing":preprocessing(c,infer_type(c,data[c])),
           "Semantic":"Label" if c in ["outcome","category"] else "Feature"}
          for c in data.columns]
schema_df = pd.DataFrame(schema)
display.display(schema_df)

#Identify and handle missing values in NSL-KDD dataset
for col in data.columns:
    if data[col].isnull().sum() > 0:
        if data[col].dtype == 'object':  
            data[col].fillna(data[col].mode()[0], inplace=True)
        else:
            data[col].fillna(data[col].median(), inplace=True)
print("Missing values handled.")

#Remove Duplicate Rows
data = data.drop_duplicates()
print("Duplicates removed. Current shape:", data.shape)

#Encoding categorical features using one-hot encoding
le = LabelEncoder()
data['outcome'] = le.fit_transform(data['outcome'])
data['category'] = le.fit_transform(data['category'])
categorical_cols = ['protocol_type','service','flag']
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)
print("Categorical features encoded. Current shape:", data.shape)

#Scale numerical features using MinMaxScaler
numerical_cols = [col for col in data.columns if col not in ['outcome','category']]
scaler = MinMaxScaler()
data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
print("Numerical features scaled.")

