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


## Future Work
- Preprocessing pipelines for both datasets
- Baseline machine learning models (Random Forest, XGBoost, etc.)
- Deep learning approaches (RNNs, CNNs for sequential flow analysis)
- Evaluation using metrics like precision, recall, F1-score, ROC curves
- Comparative study between NSL-KDD and CICIDS2017 datasets

---

## License
This project is licensed under the MIT License. See `LICENSE` file for details.

