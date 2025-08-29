# 🛡️ SentinelNet

SentinelNet is an AI-powered Network Intrusion Detection System (NIDS) capable of identifying malicious network traffic and cyber-attacks in real time. By leveraging machine learning techniques, the system classifies network traffic as normal or suspicious based on historical data, so organizations can detect intrusions faster and more accurately than with traditional systems.

---

## 📂 Project Structure

````text
SentinelNet/
├─ data/
│  └─ NSL-KDD/
│     └─ KDDTrain+.txt
├─ analysis/
│  └─ nsl_kdd_analysis.py
├─ notebooks/
│  └─ load_and_explore.py
├─ docs/
│  └─ data_overview.md
└─ README.md

---

## 🐍 Setup & Installation

1. **Clone the repository:**
```bash
git clone https://github.com/SpringBoardMentor193s/SentinelNet.git
cd SentinelNet
````

2. **Create and activate a virtual environment:**

```bash
python -m venv .venv
# Windows PowerShell
& .venv/Scripts/Activate.ps1
# Linux/Mac
source .venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

* **Run analysis script:**

```bash
python analysis/nsl_kdd_analysis.py
```

* **Run Jupyter notebook:**

```bash
jupyter notebook notebooks/load_and_explore.py
```

---

## 📄 Dataset

The project uses the **NSL-KDD dataset**, which includes features describing network connections and labels for attack types or normal traffic.

* **Training dataset:** `https://github.com/SpringBoardMentor193s/SentinelNet/blob/amityadav/data/NSL-KDD/KDDTrain%2B.txt`
* Explore dataset via Pandas for statistics and visualizations.

---

## 📖 Documentation

Refer to `https://github.com/SpringBoardMentor193s/SentinelNet/blob/10bb40432b8b25131207bacf99b0d9a88d76481c/docs/data_overview.md` for details on dataset sources, schema, and summary statistics.
