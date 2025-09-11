# NSL-KDD Dataset
## project summary
SentinelNet is an AI-powered Network Intrusion Detection System (NIDS) designed to detect and classify malicious network traffic in real time. By leveraging machine learning techniques, the system processes network traffic data, extracts relevant features, trains classification models, and generates alerts for anomalies. The project uses two well-known datasets:

NSL-KDD – classical benchmark dataset for intrusion detection.
CICIDS2017 – modern, realistic dataset containing diverse cyberattacks.
## Number of Features:
The NSL-KDD dataset contains 42 features for each record.

## The list of features 

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/e0a78c10-d5ff-456a-bf9e-7ba9f13333b2" />


## Attack Categories:
It primarily includes four types of attacks:

Denial of Service (DoS)

Probe (reconnaissance)

User-to-Root (U2R)

Remote-to-Local (R2L)

.

# Documentation for NSL-KDD Preprocessing and Visualization
1. Introduction

The NSL-KDD dataset is an improved version of the KDD’99 dataset, widely used for network intrusion detection research. It contains both normal traffic and different categories of attacks (e.g., DoS, Probe, R2L, U2R).

Since the raw dataset contains categorical features, redundant values, and an imbalanced class distribution, preprocessing is essential to make it suitable for machine learning models.

2. Data Loading

We work with two files:

KDDTrain+.txt → Training data

KDDTest+.txt → Testing data

Columns include 41 features + 1 label + 1 difficulty column.

Example features: duration, protocol_type, service, flag, src_bytes, dst_bytes, etc.

Label column indicates whether the connection is normal or an attack type.

Difficulty column is not relevant for classification and is removed.

train_df, test_df = load_data("KDDTrain+.txt", "KDDTest+.txt")

3. Preprocessing Steps
3.1 Drop Unnecessary Columns

The difficulty column is dropped as it does not contribute to classification.

3.2 Handle Categorical Features

Three categorical features:

protocol_type (e.g., tcp, udp, icmp)

service (e.g., http, ftp, smtp)

flag (e.g., SF, S0, REJ)

Converted into numerical representation using One-Hot Encoding (pd.get_dummies).

3.3 Label Encoding

Binary classification:

normal → normal

All other attack types → attack

Multi-class classification:

Each unique attack label is preserved.

Labels are transformed using LabelEncoder.

3.4 Feature Scaling

Numerical features are scaled using StandardScaler so all features are on a similar range.

4. Exploratory Data Analysis (EDA) and Visualization
4.1 Binary Classification Visualization

We create a new column called binary:

df['binary'] = df['label'].apply(lambda x: 'normal' if x == 'normal' else 'attack')


Plot distribution of protocol types vs binary classes:

plt.figure(figsize=(5,4))
sns.countplot(x='protocol_type', data=df, palette='colorblind', hue='binary')
plt.title('Attack vs Normal Distribution - NSL-KDD (Binary)')
plt.xlabel('Protocol Type')
plt.ylabel('Count')
plt.show()


This shows how different protocols (TCP, UDP, ICMP) are distributed across normal and attack categories.

4.2 Multi-class Classification Visualization

To visualize multi-class labels:

plt.figure(figsize=(7,5))
sns.countplot(x='protocol_type', data=df, palette='colorblind', hue='label')
plt.title('Attack Category Distribution - NSL-KDD (Multiclass)')
plt.xlabel('Protocol Type')
plt.ylabel('Count')
plt.legend(title='Attack Types', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


This shows how multiple attack categories (e.g., smurf, neptune, back) vary with protocol types.

5. Train-Test Preparation

After preprocessing:

Features (X) and target (y) are separated.

Train and Test data are both encoded and scaled consistently.

Stratified splitting ensures class balance in training and testing.

X_train, y_train = preprocess_data(train_df, binary=True)
X_test, y_test   = preprocess_data(test_df, binary=True)


Output example:

Train shape: (125973, 120)

Test shape: (22544, 120)

6. Conclusion

The NSL-KDD dataset requires careful preprocessing:

Dropping difficulty column

Encoding categorical features

Handling binary vs multi-class labels

Scaling numerical features

Visualizations (countplots) reveal class imbalances and protocol distributions.

This preprocessing pipeline is suitable for both binary intrusion detection and multi-class attack classification.
