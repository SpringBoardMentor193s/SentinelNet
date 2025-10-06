# 🚀 SentinelNet – NSL-KDD Dataset Project Summary

**SentinelNet** is an AI-powered **Network Intrusion Detection System (NIDS)** designed to detect and classify malicious network traffic in real-time. Using machine learning, the system analyzes network traffic, extracts key features, trains classification models, and raises alerts for anomalies.

The project utilizes two benchmark datasets:

- **NSL-KDD** – Classical dataset for intrusion detection research  
- **CICIDS2017** – Modern dataset with diverse and realistic cyberattacks

---

## 📊 NSL-KDD Dataset Overview

- The NSL-KDD dataset contains **42 features per record**.
- Features are grouped into:

| Feature Type | Description | Example Features |
|--------------|-------------|----------------|
| Basic Features | Core connection attributes | `duration`, `protocol_type`, `service`, `flag` |
| Content Features | Payload-related indicators | `hot`, `num_failed_logins`, `logged_in`, `root_shell` |
| Traffic/Time Features | Aggregated metrics over time | `count`, `srv_count`, `serror_rate` |
| Label | Target classification | `normal` or attack type |

---

### 🛡 Attack Categories

The dataset includes four main types of attacks:

1. **Denial of Service (DoS)** – Overloads target systems  
2. **Probe** – Reconnaissance and network scanning  
3. **User-to-Root (U2R)** – Local privilege escalation  
4. **Remote-to-Local (R2L)** – Unauthorized remote access  

---

## 🧹 Data Loading

We use two files:

- `KDDTrain+.txt` → Training data  
- `KDDTest+.txt` → Testing data  

Each file contains **41 features + 1 label + 1 difficulty column**.  
Example features: `duration`, `protocol_type`, `service`, `flag`, `src_bytes`, `dst_bytes`  

The **label** column indicates if the connection is normal or an attack.  
The **difficulty** column is removed as it is not relevant for classification.

```python
train_df, test_df = load_data("KDDTrain+.txt", "KDDTest+.txt")


🧹 Preprocessing Steps
1. Drop Unnecessary Columns

Remove difficulty column as it does not contribute to classification.

2. Handle Categorical Features

Categorical features:

protocol_type (e.g., tcp, udp, icmp)

service (e.g., http, ftp, smtp)

flag (e.g., SF, S0, REJ)

These are converted into numeric values using One-Hot Encoding:
df = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'])


3. Label Encoding

Binary classification:

normal → normal

All attacks → attack

Multi-class classification:

Preserve all unique attack labels and encode numerically using LabelEncoder.

4. Feature Scaling

Numerical features are scaled using StandardScaler to standardize ranges.


📈 Exploratory Data Analysis (EDA)
Binary Classification Visualization

Create a new column binary:
df['binary'] = df['label'].apply(lambda x: 'normal' if x == 'normal' else 'attack')
Plot protocol distribution by binary classes:
plt.figure(figsize=(5,4))
sns.countplot(x='protocol_type', data=df, hue='binary', palette='colorblind')
plt.title('Attack vs Normal Distribution - NSL-KDD (Binary)')
plt.xlabel('Protocol Type')
plt.ylabel('Count')
plt.show()
This shows how TCP, UDP, and ICMP protocols are distributed across normal and attack connections.

Multi-class Classification Visualization
plt.figure(figsize=(7,5))
sns.countplot(x='protocol_type', data=df, hue='label', palette='colorblind')
plt.title('Attack Category Distribution - NSL-KDD (Multiclass)')
plt.xlabel('Protocol Type')
plt.ylabel('Count')
plt.legend(title='Attack Types', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


🏗 Train-Test Preparation

After preprocessing:

Separate features (X) and labels (y)

Ensure consistent encoding and scaling for both train and test data

Use stratified splitting to maintain class balance
X_train, y_train = preprocess_data(train_df, binary=True)
X_test, y_test = preprocess_data(test_df, binary=True)
Example shapes:
| Dataset  | Shape         |
| -------- | ------------- |
| Training | (125973, 120) |
| Testing  | (22544, 120)  |


✅ Conclusion

Preprocessing of the NSL-KDD dataset involves:

Dropping irrelevant columns (difficulty)

Encoding categorical variables

Handling binary vs multi-class labels

Scaling numerical features

Visualizing distributions to inspect class imbalance and protocol usage

This pipeline prepares the dataset for both binary intrusion detection and multi-class attack classification.
