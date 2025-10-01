# NSL-KDD Dataset Documentation

## 1. Introduction
The **NSL-KDD dataset** is a benchmark dataset created to evaluate **Intrusion Detection Systems (IDS)**.  
It was introduced in **2009** as an improved version of the **KDD Cup 1999 dataset**, which suffered from redundancy and class imbalance.  
NSL-KDD addresses these limitations, making it more suitable for **machine learning research in cybersecurity**.

---

## 2. Dataset Characteristics

- **Files:**  
  - `KDDTrain+.txt` → Training set  
  - `KDDTest+.txt` → Testing set  

- **Records:** Each row corresponds to a **network connection record**  

- **Number of Features:** **41 attributes** describing network traffic, divided into:  
  - **Basic Features**: Duration, protocol type, service, flag  
  - **Content Features**: Login attempts, failed connections  
  - **Traffic Features**: Count of connections within a time window  

- **Target Variable:**  
  - **Normal** (benign traffic)  
  - **Attack** (four major categories, see below)  

---

## 3. Attack Categories

NSL-KDD defines four broad categories of attacks:

1. **Denial of Service (DoS)**  
   - Goal: Make a service or system unavailable  
   - Examples: `neptune`, `smurf`, `teardrop`, `back`  

2. **Probe (Surveillance & Scanning)**  
   - Goal: Gather information about the system or network  
   - Examples: `portsweep`, `ipsweep`, `nmap`, `satan`  

3. **Remote to Local (R2L)**  
   - Goal: Gain local access from a remote machine without authorization  
   - Examples: `guess_passwd`, `ftp_write`, `imap`, `warezclient`  

4. **User to Root (U2R)**  
   - Goal: Escalate privileges from a normal user to root access  
   - Examples: `buffer_overflow`, `loadmodule`, `rootkit`, `perl`  

---

## 4. Preprocessing Steps

1. **Categorical Encoding**  
   - Convert features like `protocol_type`, `service`, and `flag` into numerical form (e.g., one-hot encoding).  

2. **Normalization**  
   - Scale numerical features to a common range (Min-Max or z-score normalization).  

3. **Label Mapping**  
   - Binary classification: `normal` vs `attack`  
   - Multi-class classification: Different attack categories (DoS, Probe, R2L, U2R)  

4. **Train/Test Split**  
   - Training: `KDDTrain+`  
   - Testing: `KDDTest+`  

---

## 5. Why Use NSL-KDD?

- Removes duplicate records → balanced training/testing  
- Easier to handle than larger datasets like CICIDS2017  
- Still widely cited in academic research  
- Suitable for **benchmarking ML-based intrusion detection systems**  

---

## 6. Limitations

- Considered **outdated** compared to modern network traffic  
- Attack diversity is **limited**  
- May not generalize to **real-world enterprise-level attacks**  

---

## 7. Machine Learning Models Applied

Researchers commonly apply the following ML models to NSL-KDD:

- **Decision Trees (C4.5, CART)** → Simple and interpretable  
- **Random Forests** → Ensemble method for robust classification  
- **Support Vector Machines (SVM)** → Effective with smaller feature sets  
- **K-Nearest Neighbors (KNN)** → Easy to implement but slow for large datasets  
- **Naive Bayes** → Fast probabilistic approach  
- **Artificial Neural Networks (ANNs)** → Capture nonlinear relationships  
- **Clustering (K-Means, DBSCAN)** → Used for anomaly detection (unsupervised learning)  

---

## 8. Evaluation Metrics

Because NSL-KDD is imbalanced, **accuracy alone is not sufficient**. Common metrics include:

- **Accuracy** = Correct predictions / Total predictions  
- **Precision** = True Positives / (True Positives + False Positives)  
- **Recall** = True Positives / (True Positives + False Negatives)  
- **F1-Score** = 2 × (Precision × Recall) / (Precision + Recall)  
- **Confusion Matrix** = Summarizes performance across classes  

---

## 9. Applications

- Benchmarking supervised and unsupervised intrusion detection models  
- Testing **feature selection** and **dimensionality reduction** methods  
- Academic teaching dataset for **cybersecurity & machine learning**  
- Evaluating hybrid IDS combining anomaly detection with signature-based detection  

---

## 10. Future Scope

- Use **modern datasets** (CICIDS2017, UNSW-NB15) for updated attack patterns  
- Apply **deep learning** (CNN, LSTM, GRU) for sequential traffic analysis  
- Explore **ensemble and hybrid models** for improved accuracy  
- Real-time IDS deployment with streaming data  
- Use **reinforcement learning** for adaptive intrusion response  

---
