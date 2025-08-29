# SentinelNet Project Documentation

## Project Statement

**SentinelNet** aims to build an AI-powered Network Intrusion Detection System (NIDS) that can intelligently monitor and secure network traffic in real time.  
## Network Intrusion Detection Datasets

### 1. NSL-KDD Dataset

**Data Source**  
- Released in 2009 as an improved version of the older KDD’99 dataset.  
- File Used: `KDDTrain+.txt`  
- Overview: Each row represents a network connection record. Duplicate records were removed to reduce bias, resulting in cleaner training/testing splits.

## Types of Attacks:
Attacks are grouped into four main categories:
1.Denial of Service (DoS)

2.Probe (Surveillance & Probing)

3.Remote to Local (R2L)

4.User to Root (U2R)


**Best Use**  
- Small to medium dataset, easy to load into memory  
- Suitable for prototyping and testing basic intrusion detection models  

-----------------------------------------------------------------------------------------------
### 2. CICIDS2017 Dataset

**Data Source**  
- Released in 2017 by the Canadian Institute for Cybersecurity (CIC)  
- File Example: `DoS-Wednesday-no-metadata.parquet`  
- Overview: Simulates real-world network traffic collected over 5+ days, containing both benign and malicious flows

## Types of Attacks:
The attacks represented in CICIDS2017 include:

1.Brute Force (FTP and SSH)

2.DoS and DDoS

3.Heartbleed

4.Web Attacks (including SQL Injection, XSS, HTTP Brute Force)

5.Infiltration

6.Botnet

7.Port Scans

**Best Use**  
- Large, realistic dataset for evaluating advanced NIDS models  
---------------------------------------------------------------------------------------------

## Dataset Comparison Table

| Aspect                 | **NSL-KDD**                                                                     | **CICIDS2017**                                                                                     |
| ---------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Number of Features** | 41 features                                                                     | \~80 features (flows include more detailed metadata like packet size, duration, byte counts, etc.) |
| **Types of Attacks**   | DoS, Probe, R2L (Remote to Local), U2R (User to Root)                           | DoS/DDoS, Brute Force, Heartbleed, Botnet, Web attacks, Infiltration, Port Scan                    |
| **Nature of Dataset**  | Improved version of KDD Cup ’99 (removes redundancy, better class distribution) | Modern dataset collected from real-world traffic at the Canadian Institute for Cybersecurity       |
| **Time Period**        | Created in early 2000s                                                          | Collected in 2017                                                                                  |
| **Relevance**          | Useful for academic benchmarking but considered outdated                        | More realistic representation of present-day cyberattacks                                          |
| **Strengths**          | Simpler, easy to understand, widely used for teaching and benchmarking          | Rich, diverse, and modern dataset reflecting real-world attack patterns                            |
| **Weaknesses**         | Limited attack diversity, not representative of current threats                 | Large and complex, requires more resources to process and analyze                                  |


## Summary

- **NSL-KDD**: Compact, clean, suitable for basic IDS testing and prototyping.  
- **CICIDS2017**: Large, modern, realistic, suitable for advanced intrusion detection evaluation.  

Both datasets are essential resources for building, evaluating, and comparing Network Intrusion Detection Systems (NIDS), bridging research and real-world cybersecurity needs.
