import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
# NSl-KDD 
path = r"C:/Users/Hp/OneDrive/Documents/Desktop/web/SentinelNet/data/NSL-KDD/KDDTrain+.txt"
df_train = pd.read_csv(path, header=None,low_memory=False)

# Add column names
columns = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot',
    'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations',
    'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count',
    'serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate',
    'dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate',
    'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','label','difficulty_level'
]
df_train.columns=columns

#Handling missing values
print(df_train.isnull().sum().sum(), "missing values.")
df_train = df_train.dropna()

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(10,8))
sns.countplot(x='attack_binary', data=df_train, hue='attack_binary', palette="Set2", dodge=False)
plt.title("Normal vs Attack Distribution (0=Normal, 1=Attack)", fontsize=12)
plt.xlabel("Class (0=Normal, 1=Attack)")
plt.ylabel("Number of Records")
plt.show()

label_count = df_train['label'].value_counts()
plt.figure(figsize=(12,6))
label_count.plot(kind='bar')
plt.title('Distribution of attack types')
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

#top 10 attack types
attack_col = 'label' 
top_attacks = df_train[attack_col].value_counts().head(10)
plt.figure(figsize=(12,6))
top_attacks.plot(kind='bar', color='blue')
plt.title('Top 10 Attack Types')
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Dataset overview
print("\n--- Dataset Overview ---")
print(df_train.head())
print(df_train.info())
print(df_train.describe())

print("\nFeature Types:")
print(df_train.dtypes)

#One-hot encode categorical features
encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
X_train_encoded = pd.DataFrame(
    encoder.fit_transform(X_train[categorical_cols]),
    index=X_train.index,
    columns=encoder.get_feature_names(categorical_cols)  # <- use get_feature_names here
)

X_test_encoded = pd.DataFrame(
    encoder.transform(X_test[categorical_cols]),
    index=X_test.index,
    columns=encoder.get_feature_names(categorical_cols)
)
numeric_cols = [col for col in X_train.columns if col not in categorical_cols]
X_train_final = pd.concat([X_train[numeric_cols].reset_index(drop=True),
                           X_train_encoded.reset_index(drop=True)], axis=1)
X_test_final = pd.concat([X_test[numeric_cols].reset_index(drop=True),
                          X_test_encoded.reset_index(drop=True)], axis=1)

print("X_train_final shape:", X_train_final.shape)
print("X_test_final shape:", X_test_final.shape)

# feature scaling
scaler = MinMaxScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train_final), columns=X_train_final.columns)
X_test_scaled = pd.DataFrame(scaler.transform(X_test_final), columns=X_test_final.columns)
y_train = df_train['attack_binary']
y_test = df_test['attack_binary']

#Train-test split
X_train_split, X_val_split, y_train_split, y_val_split = train_test_split(
    X_train_scaled, y_train, test_size=0.2, random_state=42, stratify=y_train
)
# PCA
pca = PCA(n_components=100, random_state=42)

X_train_pca = pca.fit_transform(X_train_split)
X_val_pca = pca.transform(X_val_split)
X_test_pca = pca.transform(X_test_scaled)

 # Cicids2017
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

dataset_file = r"C:\Users\Hp\Downloads\data\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv"
df = pd.read_csv(dataset_file)
print("Dataset shape:", df.shape)
print(df.head())

# Check for any missing values and drop them
total_missing = df.isna().sum().sum()
print(f"Total missing entries found: {total_missing}")
df = df.dropna()

# Identify and remove duplicate rows
initial_rows = df.shape[0]
df = df.drop_duplicates()
removed = initial_rows - df.shape[0]
print(f"Duplicates removed: {removed}. Updated dataset size: {df.shape}")

#Generating Target Labels and Visualizing Their Distribution
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Count target classes
label_counts = df[' Label'].value_counts()

plt.figure(figsize=(9,7))

label_counts.plot.bar(color=['#99FF99', '#FF9999'])  

# Customize x-axis to show 0 and 1
plt.xticks(ticks=[0,1], labels=[0,1], fontsize=12)

# Labels and title
plt.xlabel("Class (0 = Normal, 1 = Attack)", fontsize=12)
plt.ylabel("Number of Records", fontsize=12)
plt.title("Normal vs Attack", fontsize=14)
plt.show()

# Select all numeric columns
numeric_cols = df.select_dtypes(include='number').columns
col_to_plot = numeric_cols[0]

plt.figure(figsize=(10,6))
sns.histplot(df[col_to_plot], bins=50, kde=True, color='lightgreen')
plt.title(f"Distribution of {col_to_plot}", fontsize=16)
plt.xlabel(col_to_plot)
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Label Encoding
cat_features = [col for col in df.select_dtypes(include='object').columns 
                if col not in ['Label', 'attack_binary']]

df = pd.get_dummies(df, columns=cat_features, drop_first=True)

# Scale features
target_col = df.columns[-1]
X = df.drop(columns=[target_col])
y = df[target_col]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) 

#split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,        
    y,                
    test_size=0.3,    
    random_state=42,  
    shuffle=True)