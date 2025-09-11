# Project Report - SentinelNet (Intrusion Detection System)

## 1. Introduction
With the rapid growth of the internet, **network security threats** such as DoS, probing, and unauthorized access are increasing. Traditional firewalls are insufficient to detect modern attacks.  
Hence, an **Intrusion Detection System (IDS)** like *SentinelNet* is essential to detect abnormal activities.

---

## 2. Objectives
- Detect malicious network activities using ML models
- Improve detection accuracy over traditional IDS
- Compare different ML algorithms
- Provide insights into attack patterns

---

## 3. Dataset
- Dataset: **NSL-KDD** (an improved version of the KDD’99 dataset)
- Files:
  - `KDDTrain+.txt` → Training data
  - `KDDTest+.txt` → Testing data
- Features:
  - 41 features (numerical + categorical)
  - 1 label (attack/normal)

---

## 4. Methodology
1. Data Preprocessing  
   - Clean data, encode categorical features, normalize numerical data  
2. Exploratory Data Analysis (EDA)  
   - Visualize attacks and traffic distribution  
3. Model Training  
   - Train using multiple ML algorithms  
4. Model Evaluation  
   - Accuracy, Precision, Recall, F1-score  
5. Deployment  
   - Wrap in Python script (later Flask/Streamlit for UI)

---

## 5. Results
- Models compared: Logistic Regression, Decision Tree, Random Forest, Neural Network
- Metrics showed **Random Forest & Neural Networks performed best**
- Accuracy achieved: **~85–90% depending on dataset split**

---

## 6. Conclusion
- SentinelNet provides a **machine-learning-based intrusion detection system**
- It improves upon older rule-based systems
- Future work:  
  - Real-time monitoring  
  - Deep learning approaches (RNN, LSTM)  
  - Cloud deployment for scalability  

---

## 7. References
- Tavallaee, M., Bagheri, E., Lu, W., & Ghorbani, A. A. (2009). *A detailed analysis of the KDD CUP 99 data set*.  
- NSL-KDD dataset: http://www.unb.ca/cic/datasets/nsl.html
