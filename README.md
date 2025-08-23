# 🛡️ SentinelNet: AI-Powered Network Intrusion Detection System (NIDS)

---

SentinelNet is an AI-driven Network Intrusion Detection System (NIDS) designed to identify malicious network traffic and detect cyber-attacks in real time.
By leveraging machine learning techniques, SentinelNet classifies network traffic as normal or suspicious based on historical patterns, providing an intelligent defense mechanism against modern cyber threats.


# 📌 Project Statement

The goal of this project is to build an AI-powered intrusion detection system that can analyze network traffic and detect cyber-attacks in real time.
Using machine learning algorithms, the system will classify traffic as normal or malicious by learning from historical datasets. It processes network data, extracts important features, trains classification models, and generates alerts for suspicious or anomalous activity.

✨ Features

⚡ Real-time intrusion detection using ML
🧠 Multiple algorithms (Decision Tree, Random Forest, SVM)
📊 Data visualization & analysis with Jupyter notebooks
🔍 Feature engineering & preprocessing pipeline
📂 Extendable for modern datasets (NSL-KDD, CICIDS2017)


# 🏗️ Modules to be Implemented

Dataset Acquisition & Exploration – Load and examine the dataset.

Data Cleaning & Preprocessing – Handle missing values, encode labels, normalize features.

Feature Engineering & Selection – Identify relevant features that improve detection accuracy.

Model Building & Training – Train ML classifiers (Decision Tree, Random Forest, SVM).

Evaluation & Reporting – Measure performance (accuracy, precision, recall, F1) and document results.

---

# 📊 Datasets

# NSL-KDD Dataset

🎯 41 features + 1 target label
🛑 Attack Types: DoS, Probe, R2L, U2R
🔗 [NSL-KDD Dataset](https://www.kaggle.com/datasets/hassan06/nslkdd)

# CICIDS2017 Dataset (Future Extension)

⚙️ 80+ flow-based features
🛡️ Modern attacks: DDoS, Botnet, Web Attacks, Brute Force, Heartbleed
[CICIDS2017 Dataset](https://www.kaggle.com/datasets/sateeshkumar6289/cicids-2017-dataset)

---

# 📂 Project Structure
````` text 
SentinelNet
|   
|
+---analysis
|
+---data
|   \---NSL-KDD
|           KDDTrain+.txt
|
+---docs
|       data_overview.md
|       nsl_kdd_overview.md
|       reflection.md
|
+---notebooks
|       explore_nsl_kdd.ipynb
|
+---scripts│ 
|
└── README.md

`````

---

# ️ Setup & Installation

# 1️⃣ Clone the Repository

```bash

git clone https://github.com/SpringBoardMentor193s/SentinelNet.git
cd SentinelNet 


```
# 2️⃣ Install the dependencies:

```bash

pip install package_name

```

---

# 🚀 Usage

# ▶️ Open Jupyter Notebook in VS Code

Install the Jupyter extension in VS Code (if not already installed).

Open the file:

analysis/nsl_kdd_analysis.ipynb


Select your Python interpreter / virtual environment from the top-right corner (kernel).

Click "Run All" ▶️ or execute cells one by one.

---

# 📖 Documentation

Refer to these documents for more details:  

- 📄 [Data Overview](docs/data_overview.md)
- 📝 [Reflection](docs/reflection.md)