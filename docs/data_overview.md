# Network Intrusion Detection Datasets Overview

## 1. NSL-KDD Dataset

### Dataset Source
- File: `KDDTrain+.txt`
- Description: NSL-KDD is a refined version of the original KDD Cup 1999 dataset.

### Dataset Shape
- Number of rows: 125,973
- Number of columns: 42
- Label column: Last column

### Labels
- Unique labels: normal, neptune, smurf, satan, ipsweep, and others
- Top 5 attack types:
  1. neptune
  2. smurf
  3. normal
  4. satan
  5. ipsweep

## 2. CICIDS2017 Dataset

### Dataset Source
- File: `DoS-Wednesday-no-metadata.parquet`
- Description: CICIDS2017 captures realistic network traffic including normal and attack flows.

### Dataset Shape
- Rows and columns: 2,830,000+ × 80+ 
- Label column: `Label`

### Labels
- Unique attack types: DoS Hulk, DoS GoldenEye, DoS slowloris, DDoS, PortScan, FTP-Patator, SSH-Patator, Normal
- Top 5 frequent attack types:
  1. DoS Hulk
  2. DoS GoldenEye
  3. DoS slowloris
  4. DDoS
  5. PortScan

## Summary
Both datasets provide labeled network traffic data for evaluating intrusion detection systems. NSL-KDD is smaller and classical, while CICIDS2017 is large-scale and more realistic.
