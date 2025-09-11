# STEP 1: Import libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# STEP 2: Define dataset columns (from NSL-KDD dataset)
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

# STEP 3: Load Train & Test data
train = pd.read_csv(r"D:\SpringBoard\Datasets_nslkdd\KDDTrain+.txt", names=columns)
test  = pd.read_csv(r"D:\SpringBoard\Datasets_nslkdd\KDDTest+.txt", names=columns)
print("Train shape:", train.shape)
print("Test shape:", test.shape)

# STEP 4: Map attacks into categories
dos = ['back','land','neptune','pod','smurf','teardrop']
probe = ['satan','ipsweep','nmap','portsweep']
r2l = ['guess_passwd','ftp_write','imap','phf','multihop','warezmaster','warezclient','spy']
u2r = ['buffer_overflow','loadmodule','perl','rootkit']

def map_attack_category(label):
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

train["attack_category"] = train["outcome"].apply(map_attack_category)
test["attack_category"]  = test["outcome"].apply(map_attack_category)

# STEP 5: Separate features (X) and labels (y)
X = train.drop(["outcome","level","attack_category"], axis=1)  # input features
y = train["attack_category"]                                # target labels

# STEP 6: Encode categorical columns into numbers
categorical_cols = ['protocol_type','service','flag']
encoder = LabelEncoder()
for col in categorical_cols:
    X[col] = encoder.fit_transform(X[col])

# STEP 7: Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# STEP 8: Split dataset into Train & Test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)
print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)
# Separate features (X) and labels (y)
X = train.drop(["outcome", "level", "attack_category"], axis=1)
y = train["attack_category"]

# Get categorical and numerical features
categorical_cols = X.select_dtypes(include=["object"]).columns
numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns

print("Categorical Features:", list(categorical_cols))
print("Numerical Features:", list(numerical_cols))
# ✅ STEP 1: Check Missing Values
print("\n🔹 Missing values in each column:")
print(X.isnull().sum())

# Explanation:
# .isnull() → checks if a cell is missing (NaN)
# .sum() → adds them up column-wise
# This will show how many missing values each column has.

# ✅ STEP 2: Check Duplicates
print("\n🔹 Total duplicate rows in dataset:")
print(X.duplicated().sum())

# Explanation:
# .duplicated() → returns True for duplicate rows
# .sum() → counts how many duplicate rows are there

# ✅ STEP 3: If you want, remove duplicates
X_cleaned = X.drop_duplicates()

print("\n🔹 Shape before removing duplicates:", X.shape)
print("🔹 Shape after removing duplicates:", X_cleaned.shape)
