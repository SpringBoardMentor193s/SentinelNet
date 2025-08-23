# 📊 SentinelNet Dataset Documentation

- [NSL-KDD Dataset on Kaggle](https://www.kaggle.com/datasets/hassan06/nslkdd)  

## 📌 Dataset Overview
The **NSL-KDD dataset** is an improved version of the **KDD Cup 1999 dataset**, widely used for **Network Intrusion Detection (NID)** research.  
It addresses several issues in the original dataset such as redundant records and imbalance.  

Each record represents a **network connection** with features describing its properties, and a label indicating whether the connection is **normal** or an **attack**.

---

## 📂 Files Used
- **`KDDTrain+.txt`** → Training dataset  
- **`KDDTest+.txt`** → Testing dataset  

Both files contain:
- **41 features** (basic, content, traffic, and host-based)  
- **1 label column** (normal or specific attack type)  

---

## 📐 Dataset Statistics
| Dataset      | Records | Features | Labels |
|--------------|---------|----------|--------|
| KDDTrain+    | 125,973 | 41       | 1      |
| KDDTest+     | 22,544  | 41       | 1      |

---

## 🧩 Feature Categories
The features are grouped into 4 main categories:

1. **Basic Features**  
   - Duration, protocol type, service, flag, etc.  

2. **Content Features**  
   - Number of failed login attempts, number of file creations, etc.  

3. **Traffic Features (same host)**  
   - Count of connections to the same host within a time window.  

4. **Traffic Features (same service)**  
   - Count of connections to the same service within a time window.  

---

## 🎯 Label Information
The dataset has **binary** and **multi-class labels**.

- **Normal**: Legitimate traffic  
- **Attack types** (examples):  
  - **DoS (Denial of Service)** → `neptune`, `smurf`, `back`  
  - **Probe** → `satan`, `ipsweep`, `nmap`  
  - **R2L (Remote to Local)** → `guess_passwd`, `ftp_write`, `multihop`  
  - **U2R (User to Root)** → `buffer_overflow`, `loadmodule`, `rootkit`  

👉 Attacks can be mapped into **4 categories**: DoS, Probe, R2L, U2R.  

---

## 🔎 Example Record
- `0` → duration  
- `tcp` → protocol type  
- `http` → service  
- `SF` → flag  
- `181` → source bytes  
- `5450` → destination bytes  
- `normal` → label  

---

## 🧮 Preprocessing Steps
Before using the dataset for ML:
1. **Assign column names** (41 features + label)  
2. **Convert categorical features** (protocol, service, flag) → one-hot encoding  
3. **Normalize numeric values** (min-max scaling / standardization)  
4. **Handle duplicates** → remove redundancy  
5. **Balance labels** → optional (undersampling/oversampling)  

---


