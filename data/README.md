# 📂 Data Folder

This folder contains sample data files used for demonstration and testing within the **SentinelNet** project.

---

## 📌 Included Files

| File Name                        | Dataset   | Description |
|----------------------------------|-----------|-------------|
| `KDDTrain+.txt`                  | NSL-KDD   | The full training dataset used to build intrusion detection models. |
| `KDDTest+.txt`                   | NSL-KDD   | A full test subset from the NSL-KDD dataset, commonly used for evaluating model performance. |
| `KDDTrain+_20Percent.txt`        | NSL-KDD   | A 20% sample of the training data, useful for faster experimentation. |
| `Friday-WorkingHours-Afternoon-DDos.csv` | CICIDS2017 | A sample file from the CICIDS 2017 dataset, containing DDoS attack traffic captured on Friday afternoon working hours. |

These sample files are provided to keep the repository lightweight while allowing quick experimentation.

---

## 🔗 Full Dataset Sources

Due to size constraints, the complete datasets are **not included** in this repository. You can download them from the following official sources:

### 📁 NSL-KDD Dataset
- **Source**: [Kaggle - NSL-KDD by Hassan06](https://www.kaggle.com/datasets/hassan06/nslkdd)  
- **Description**: An improved version of the original KDD Cup 1999 dataset. Designed for evaluating network intrusion detection systems.  
- **Common Files**:
  - `KDDTrain+.txt` — Full training data  
  - `KDDTest+.txt` — Full test data  
  - `KDDTrain+_20Percent.txt` — 20% sample of training data  

### 📁 CICIDS 2017 Dataset
- **Source**: [Kaggle - CICIDS 2017 by sateeshkumar6289](https://www.kaggle.com/datasets/sateeshkumar6289/cicids-2017-dataset)  
- **Original Publisher**: Canadian Institute for Cybersecurity (CIC), University of New Brunswick  
- **Description**: A modern, labeled dataset containing benign and various attack traffic, including DoS, DDoS, Brute Force, Infiltration, Web Attacks, and more.  
- **Common Files**:
  - Multiple CSV files, each representing traffic for a specific day or attack scenario.  
  - E.g., `Monday-WorkingHours.pcap_ISCX.csv`, `Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`, etc.  

---
## 📂 Data Folder Structure

```plaintext
data/
├── KDDTrain+.txt               # NSL-KDD training dataset
├── KDDTest+.txt                # NSL-KDD test dataset
├── KDDTrain+_20Percent.txt     # 20% sample of NSL-KDD training dataset
└── Friday-WorkingHours-Afternoon-DDos.csv  # CICIDS2017 subset



## 📌 Notes

- Please **do not upload the full datasets** to this repository to avoid large file sizes and GitHub limitations.  
- When running notebooks or scripts that require the full dataset, download the complete data from the links above and place them in this `data/` folder.  
- Update any file paths in the code as needed to match your local setup.  

---

