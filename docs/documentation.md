# SentinelNet Project Documentation

## Project Statement

**SentinelNet** aims to build an AI-powered Network Intrusion Detection System (NIDS) that can intelligently monitor and secure network traffic in real time.  
## Network Intrusion Detection Datasets

### 1. NSL-KDD Dataset

**Data Source**  
- Released in 2009 as an improved version of the older KDD’99 dataset.  
- File Used: `KDDTrain+.txt`  
- Overview: Each row represents a network connection record. Duplicate records were removed to reduce bias, resulting in cleaner training/testing splits.

**Key Characteristics**  
- Built to eliminate duplicate and redundant records from KDD Cup ’99  
- Cleaner training/testing splits  
- Still older and less representative of modern traffic patterns  


**Best Use**  
- Small to medium dataset, easy to load into memory  
- Suitable for prototyping and testing basic intrusion detection models  

-----------------------------------------------------------------------------------------------
### 2. CICIDS2017 Dataset

**Data Source**  
- Released in 2017 by the Canadian Institute for Cybersecurity (CIC)  
- File Example: `DoS-Wednesday-no-metadata.parquet`  
- Overview: Simulates real-world network traffic collected over 5+ days, containing both benign and malicious flows



**Key Characteristics**  
- Modern dataset with real-world PCAP captures  
- Diverse protocols: HTTP, HTTPS, FTP, SSH, email  
- Rich flow-based metadata for fine-grained insights  
- Larger feature set and more complex attack scenarios  
- Realistic class imbalance reflecting modern networks  

**Best Use**  
- Large, realistic dataset for evaluating advanced NIDS models  
---------------------------------------------------------------------------------------------
## Summary

- **NSL-KDD**: Compact, clean, suitable for basic IDS testing and prototyping.  
- **CICIDS2017**: Large, modern, realistic, suitable for advanced intrusion detection evaluation.  

Both datasets are essential resources for building, evaluating, and comparing Network Intrusion Detection Systems (NIDS), bridging research and real-world cybersecurity needs.
