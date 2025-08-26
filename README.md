# SentinelNet: AI-Powered Intrusion Detection

## Overview
# SentinelNet
The goal of this project is to develop an AI-powered Network Intrusion Detection System (NIDS) capable of identifying malicious network trafic and cyber-attacks in real time. By leveraging machine learning techniques, the system will classify trafic as normal or suspicious based on historical data. 

The project is structured for collaborative development, reproducibility, and scalability. It integrates data analysis, visualization, and model development through well-organized folders and modular scripts.

---

## Mentor
**Dr. N Jagan Mohan** – Experienced Data Scientist guiding the project with expertise in AI, data engineering, and network security.

---

## Project Structure
```
SentinelNet/
├── data/                # Datasets (raw and processed)
│   ├── nsl-kdd/
│   └── cicids2017/
├── notebooks/           # Jupyter notebooks for exploration & experiments
├── scripts/             # Python scripts for preprocessing, training, evaluation
├── docs/                # Documentation files
│   └── data_overview.md
├── README.md            # Project summary and details
```

---

## Setup Instructions

1. Clone the repository (from your fork):
   ```bash
   git clone https://github.com/your-username/sentinelnet.git
   cd sentinelnet
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Place datasets inside the `data/` folder:
   - NSL-KDD dataset → `data/nsl-kdd/`
   - CICIDS2017 dataset → `data/cicids2017/`

---

## Datasets

### 1. NSL-KDD Dataset
- Source: [NSL-KDD dataset](https://www.unb.ca/cic/datasets/nsl.html)
- Description: Improved version of KDD'99 dataset; removes redundancy and imbalance.
- Features: ~41 features + label (attack/normal).
- Attack categories: DoS, Probe, U2R, R2L, Normal.

### 2. CICIDS2017 Dataset
- Source: [CICIDS2017 dataset](https://www.unb.ca/cic/datasets/ids-2017.html)
- Description: Realistic modern network traffic with timestamped flows.
- Features: ~80+ flow-based features.
- Attack types: Brute Force, Botnet, DDoS, Infiltration, Web attacks, etc.

---

## Tasks Completed

✔ Created personal fork of the repo  
✔ Set up project folder structure (`data/`, `notebooks/`, `scripts/`, `docs/`)  
✔ Added README with full project summary and mentor info  
✔ Loaded NSL-KDD dataset with Pandas  
✔ Printed dataset summary statistics  
✔ Visualized attack type distribution with bar chart  
✔ Performed dataset inspection using `.head()`, `.info()`, `.describe()`  
✔ Documented dataset sources and schema in `docs/data_overview.md`  
✔ Written reflection on challenges in intrusion detection  

---

## Reflection (200 Words)

When analyzing the NSL-KDD dataset, clear patterns emerge in network traffic. Normal traffic often shows consistent usage of well-known services such as HTTP, SMTP, and FTP, while attacks are characterized by irregular patterns like repeated connections, abnormal port access, and unusually high traffic volumes. For instance, DoS attacks can be identified through floods of packets, while probing attempts involve scanning multiple IPs or ports.

However, detecting intrusions is challenging due to several reasons. First, many attack patterns are subtle and mimic legitimate behavior, making them hard to distinguish. Second, the datasets themselves are highly imbalanced, with far fewer examples of rare attacks such as U2R and R2L compared to common attacks like DoS. This creates difficulty in training models that can generalize well across all attack types. Additionally, the evolution of cyberattacks means that static datasets often become outdated, as attackers continuously adapt and find new vulnerabilities. Finally, network traffic data is high-dimensional, and extracting meaningful features without losing critical information requires domain knowledge and careful preprocessing.

These challenges highlight the importance of AI and machine learning in building adaptive, intelligent intrusion detection systems that go beyond rule-based detection to learn complex patterns in real-world network traffic.

---

## Future Work
- Preprocessing pipelines for both datasets
- Baseline machine learning models (Random Forest, XGBoost, etc.)
- Deep learning approaches (RNNs, CNNs for sequential flow analysis)
- Evaluation using metrics like precision, recall, F1-score, ROC curves
- Comparative study between NSL-KDD and CICIDS2017 datasets

---

## License
This project is licensed under the MIT License. See `LICENSE` file for details.

