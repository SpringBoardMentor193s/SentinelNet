
# SentinelNet – AI-Powered Network Intrusion Detection System   

## Overview  
**SentinelNet** is an AI-powered **Network Intrusion Detection System (NIDS)** designed to detect and classify malicious network activities.  
It leverages **machine learning and deep learning** models to analyze traffic patterns, classify attacks, and enhance cybersecurity defense strategies.  

---
## Goal
- The goal of this project is to develop an AI-powered Network Intrusion Detection System (NIDS) capable of identifying malicious network trafic and cyber-attacks in real time. By leveraging machine learning techniques, the system will classify trafic as normal or suspicious based on historical data. 
---

## Key Features  
- **Traffic Analysis:** Preprocessing and feature engineering on NSL-KDD & CIC-IDS 2017 datasets.  
- **ML/DL Models:** Train, evaluate, and deploy models for intrusion detection.  
- **Visual Analytics:** Interactive plots for attack distribution, frequency analysis, and detection performance.  
- **Real-Time Detection (Planned):** Future support for live packet capture and classification.  
- **Attack Categorization:** Labels traffic as **normal** or **anomaly** and further groups into attack categories.  

---

## Project Structure  
SentinelNet/
│── data/ # Datasets (NSL-KDD, CIC-IDS 2017)
│ ├── nslkdd/ # Raw + processed NSL-KDD dataset files
│ └── cicids2017/ # Raw + processed CIC-IDS 2017 dataset
│
│── scripts/ # Python scripts for modular workflows
│ └── main.py # Main pipeline script
│
│── docs/ # Documentation, reports, research notes
│ ├── reflection_docs/ # Reflections & notes
│ ├── data_overview.md # Dataset summary
│ └── Dataset_Analysis.md # Detailed dataset analysis
│
│── requirements.txt # Python dependencies
│── README.md # Project documentation

---

##  Datasets  

### 1️⃣ NSL-KDD Dataset  
- Benchmark dataset for intrusion detection.  
- Contains **41 features** describing connection attributes + class label (`normal` or `anomaly`).  
- Example attributes: `duration`, `protocol_type`, `service`, `flag`, `src_bytes`, `dst_bytes`  

**Classes:**  
- `normal`  
- `anomaly` (DoS, Probe, R2L, U2R attacks)  

🔗 **Download NSL-KDD Dataset:**  
- [Kaggle Link](https://www.kaggle.com/datasets/hassan06/nslkdd)  

---

### 2️⃣ CIC-IDS 2017 Dataset  
- Real-world intrusion detection dataset created by the **Canadian Institute for Cybersecurity (CIC)**.  
- Includes diverse attack types (DDoS, Botnet, Brute-force, Infiltration, Web attacks, etc.).  
- Provides realistic traffic flow data with timestamps and **80+ features**.  

🔗 **Download CIC-IDS 2017 Dataset:**  
- [Kaggle Mirror Link](https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset)  

---
## Prerequisites  
- Python **3.8+**  
- pip / conda  
- Git  
---
## Install Dependencies
pip install -r requirements.txt
---
## Usage
1️⃣ Data Preprocessing
python scripts/preprocess.py --dataset data/nslkdd/KDDTrain+.csv
2️⃣ Train Model
python scripts/train.py --dataset data/nslkdd/KDDTrain+.csv --model models/sentinelnet.pkl
3️⃣ Evaluate Model
python scripts/evaluate.py --model models/sentinelnet.pkl --test data/nslkdd/KDDTest+.csv
4️⃣ Run Detection
python scripts/detect.py --input data/sample_traffic.csv
---
## Example Results
- •	Attack distribution (Normal vs. Anomaly)
- •	Confusion Matrix and ROC curves
- •	Per-class precision, recall, and F1-scores
---
## Attack Categories
- •	DoS (Denial of Service)
- •	Probe (Information Gathering)
- •	R2L (Remote to Local)
- •	U2R (User to Root)
- •	Others (CIC-IDS 2017): Brute-force, Botnet, DDoS, Infiltration
---
## Future Enhancements
- •	Transformer-based models for tabular traffic data
- •	Real-time packet sniffing and classification
- •	Integration with visualization dashboards (Grafana/ELK)
- •	Cloud-based deployment (AWS/GCP)
---

## Contributions are welcome!
- 1.	Fork this repo
- 2.	Create your feature branch (git checkout -b feature-name)
- 3.	Commit changes (git commit -m "Add feature")
- 4.	Push to branch (git push origin feature-name)
- 5.	Open a Pull Request
---
## License
- This project is licensed under the MIT License – see LICENSE for details.
---



