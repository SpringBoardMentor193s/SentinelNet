
# SentinelNet Internship Actionable Items

## 1. SentinelNet Project Goals
SentinelNet is an AI-powered Network Intrusion Detection System (NIDS) designed to monitor and analyze network traffic in real time. It uses machine learning to extract meaningful features, build classification models, detect anomalies, and promptly alert security teams about potential cyber-attacks or suspicious activities for proactive defense.

---

## 2. Dataset Exploration: NSL-KDD vs. CICIDS2017

### a. Number of Features & Dataset Size
- **NSL-KDD**:  
  - Contains 41 features plus one for the target label (totaling 42). There are four categorical, four binary, and 33 numerical features.

- **CICIDS2017**:  
  - One version includes **83 features** (plus one label). Another common version used for ML has **78 features plus the label**, making 79 in total.

### b. Types of Attacks Included
- **NSL-KDD**:  
  - Categories: Denial of Service (DoS), Probe, Remote-to-Local (R2L), and User-to-Root (U2R). Includes normal traffic.

- **CICIDS2017**:  
  - Covers a wide variety of modern attacks: Brute Force (e.g., FTP-Patator, SSH-Patator), Web attacks (e.g., XSS, SQL Injection), DoS/DDoS, Heartbleed, Infiltration, Botnet, Port Scan, and standard benign traffic.

### c. Key Differences Between Datasets
- **Modernity & Realism**:  
  - *NSL-KDD* is derived from the much older KDD’99 dataset and is useful for general classifications.  
  - *CICIDS2017* represents more recent real-world threat scenarios, using modern protocols and diverse attack types.

- **Feature Depth**:  
  - NSL-KDD offers a simpler feature set (41 numeric/categorical features).  
  - CICIDS2017 offers richer, flow-based features (78–83), including statistics like packet sizes, time intervals, protocol flags, etc.

- **Dataset Size & Imbalance**:  
  - NSL-KDD is relatively smaller and simpler.  
  - CICIDS2017 is extensive (millions of samples across multiple days) and exhibits significant class imbalance—especially between benign traffic and rare attacks like infiltration.

- **Use Case Suitability**:  
  - NSL-KDD is good for baseline model development.  
  - CICIDS2017 is ideal for evaluating IDS performance on modern, complex, real-world traffic with a larger feature set and varied attack types.

---

## 3. Reflection 

**Why AI is Critical in Cybersecurity, and What Excites Me About Building SentinelNet**

In an evolving digital landscape, cyber threats grow steadily in both sophistication and volume. Traditional signature‑based security systems struggle to keep pace with fast‑evolving or unseen attack patterns, leaving networks vulnerable. Artificial intelligence offers transformative advantages in cybersecurity. AI-powered systems—like SentinelNet—can learn from large datasets, uncover subtle patterns, generalize to recognize new threats, and adapt continuously. They enable proactive detection rather than reactive defense, offering crucial speed and accuracy in responding to breaches.

SentinelNet excites me because it embodies this potential: a real-time, machine learning–driven system that monitors network traffic, distinguishes anomalies, and generates alerts autonomously. The notion of building a system that uses advanced modeling to sift through massive data flows and surface malicious behavior before harm occurs is powerful. What’s thrilling is how SentinelNet can evolve—leveraging feature extraction, classification algorithms, anomaly detection, and alerting mechanisms—to support a resilient, intelligent defense posture. Working on SentinelNet means contributing to a tool that bridges the gap between raw data and actionable security insights, reinforcing trust in digital infrastructure. It’s an opportunity to blend applied AI with meaningful impact in cybersecurity—a challenge I’m truly excited about.
