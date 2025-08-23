# 📊 Data Overview - NSL-KDD Dataset

The NSL-KDD dataset is an improved version of the original KDD Cup 1999 dataset.  
It is widely used for evaluating intrusion detection systems.

---

## 📁 Files
- `KDDTrain+.txt` → Training set
- `KDDTest+.txt` → Testing set

---

## 🔑 Features
Each record contains 41 features and 1 label (attack type).  
Features are divided into:
- **Basic Features**: Protocol type, service, flag
- **Content Features**: Number of failed logins, root access, etc.
- **Traffic Features**: Count of connections in a given time window

---

## 🎯 Target Labels
The dataset classifies network traffic as:
- `normal` (benign traffic)
- `attack` (malicious traffic), which includes:
  - **DoS** (Denial of Service)
  - **Probe** (Surveillance, scanning)
  - **R2L** (Remote to Local)
  - **U2R** (User to Root)

---

## 📐 Train/Test Split
- Training set size: ~125,973 records
- Testing set size: ~22,544 records

