
AI-Powered Network Intrusion Detection System (NIDS)

SentinelNet is an AI-driven Network Intrusion Detection System designed to detect malicious network traffic and cyber-attacks in real time. Using machine learning techniques, the system classifies network connections as normal or suspicious based on historical data from the NSL-KDD dataset.

🔹 Features

Real-time detection of network intrusions

Classifies traffic as normal or attack

Supports multiple attack categories: DoS, Probe, R2L, U2R

Utilizes ML/DL algorithms for accurate classification

Dataset preprocessing and feature extraction included

🔹 Dataset

NSL-KDD Dataset (KDDTrain+.txt, KDDTest+.txt)

Contains network connection records with 41 features per record

Features include:

Basic connection info: duration, protocol, service, bytes sent/received

Content features: failed logins, root access attempts, file creations

Traffic-based stats: connection counts, error rates, same host/service rates

Each record is labeled as normal or an attack type (DoS, Probe, R2L, U2R)

🔹 Project Structure
SentinelNet/
│
├─ Dataprepossing/          # Preprocessing scripts
├─ Dataset/                 # NSL-KDD dataset files
├─ Attackcategory/          # Attack classification scripts and resources
├─ emotion_detector.py      # Main detection script (if applicable)
└─ README.md                # Project documentation