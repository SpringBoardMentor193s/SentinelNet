# 🔐 Network Intrusion Detection Datasets Overview

This document provides an overview of two widely used benchmark datasets for evaluating **Intrusion Detection Systems (IDS)**: **NSL-KDD** and **CIC-IDS-2017**.

---

## 📂 1. NSL-KDD Dataset

**Description**  
The NSL-KDD dataset is a cleaned and improved version of the KDD Cup 1999 dataset. It resolves redundancy and imbalance issues, making it more reliable for benchmarking intrusion detection models.

- **Training rows**: 125,973  
- **Testing rows**: 22,254  
- **Features (excluding label)**: 41  
- **Label column**: Last column  

**Categories of Attacks**  
- **DoS** (Denial of Service)  
- **R2L** (Remote to Local)  
- **U2R** (User to Root)  
- **Probe** (Probing attacks)  

**Notable Attack Types**  
`neptune`, `smurf`, `satan`, `ipsweep`, and others.  
In total, the dataset contains **24 attack types** in training and an additional **14 in testing**, plus the `normal` class.

---

## 📂 2. CIC-IDS-2017 Dataset

**Description**  
Developed by the Canadian Institute for Cybersecurity (CIC), CIC-IDS-2017 replicates realistic modern network traffic, blending benign activity with diverse cyber-attacks. It is highly valuable for research on real-world intrusion detection systems.

- **Records**: ~2.5M to 2.83M  
- **Features**: 78 (ML version), up to 85 (with metadata)  
- **Label column**: `Label`  
- **Attack proportion**: ~19.7% of the dataset  

**Categories of Attacks**  
- DoS (Hulk, GoldenEye, slowloris, SlowHTTPTest, etc.)  
- DDoS  
- PortScan  
- Brute Force (FTP, SSH)  
- Heartbleed  
- Botnet  
- Web Attacks (XSS, SQL Injection, Brute Force)  
- Infiltration  
- Normal (benign traffic)  

**Most Frequent Attack Types**  
`DoS Hulk`, `DoS GoldenEye`, `DoS slowloris`, `DDoS`, `PortScan`

---

## 📊 Summary Comparison

| Dataset        | Training Rows | Testing Rows | Features (Excl. Label) | Attack Proportion | Common Attack Types / Categories |
|----------------|---------------|--------------|-------------------------|------------------|----------------------------------|
| **NSL-KDD**    | 125,973       | 22,254       | 41                      | —                | DoS, R2L, U2R, Probe; includes neptune, smurf, satan, ipsweep, etc. |
| **CIC-IDS-2017** | ~2.5–2.83M    | —            | 78 (up to 85)           | ~19.7%           | DoS Hulk, DoS GoldenEye, slowloris, DDoS, PortScan, Brute Force, Botnet, Web Attacks, Infiltration |

---

## ✅ Key Takeaways
- **NSL-KDD** is **smaller, classical, and widely used** for quick experimentation and academic benchmarks.  
- **CIC-IDS-2017** is **large-scale, modern, and realistic**, reflecting contemporary network traffic patterns and attack behaviors.  

Both datasets are valuable benchmarks and are commonly used together for developing and evaluating robust intrusion detection models.

---
