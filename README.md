# 🛡️ SentinelNet

The goal of this project is to develop an AI-powered Network Intrusion Detection System (NIDS) capable of identifying malicious network traffic and cyber-attacks in real time. By leveraging machine learning techniques, the system classifies traffic as normal or suspicious based on historical data. It processes network traffic records, extracts relevant features, trains classification models, and generates alerts for detected anomalies.

---
## 🎯 Objectives

- Understand network traffic data and common types of cyberattacks.
- Apply machine learning algorithms to detect intrusions.
- Build and evaluate classification models (e.g., Decision Tree, Random Forest, SVM).
- Perform feature engineering and anomaly detection.
- Generate alerts or logs for detected threats.
- Prepare a detailed report and presentation showcasing the project.
---
## SentinelNet Presentation

You can view the project presentation below.  
If the PDF does not load on GitHub, please use the backup link provided.  

- [Presentation (PDF on GitHub)](https://github.com/SpringBoardMentor193s/SentinelNet/blob/amityadav/docs/SentinelNet.pdf)  
- [Backup Link (Google Drive)](https://drive.google.com/file/d/1p0RIC0ciI-xYFEFCfuNjSPeHeRyYmwDI/view?usp=sharing)  

---

## 📂 Project Structure

````
SENTINELNET/
├── .venv/
├── data/
│   ├── DoS-Wednesday-no-metadata.parquet
│   ├── KDDTest+.arff
│   ├── KDDTest+.txt
│   ├── KDDTrain+_processed.csv
│   ├── KDDTrain+.arff
│   ├── KDDTrain+.txt
│   └── WebAttacks-Thursday.csv
├── docs/
│   └── data_overview.md
├── notebooks/
│   ├── attack_visualization.ipynb
│   ├── cicids_model_train.ipynb
│   └── nslkdd_mode_train.ipynb
├── results/
│   └── visual plots (PNG images)
├── scripts/
│   └── main.py
├── documentation.pdf
├── LICENSE
├── README.md
└── requirements.txt

````
## 🐍 Setup & Installation

```
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

* **Training dataset:** ```https://github.com/SpringBoardMentor193s/SentinelNet/blob/amityadav/data/NSL-KDD/KDDTrain%2B.txt```
* Explore dataset via Pandas for statistics and visualizations.
---

##CICIDS2017 Dataset

Since the dataset is too large for GitHub, you can download and extract it automatically:

```
pip install gdown
python download_data.py
```

---

## 📖 Documentation

Refer to [Data Overview](https://github.com/SpringBoardMentor193s/SentinelNet/blob/10bb40432b8b25131207bacf99b0d9a88d76481c/docs/data_overview.md) for details on dataset sources, schema, and summary statistics.

---
## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn 
---
## 🧩 Modules to be Implemented

- Dataset Acquisition and Exploration – Collect and explore network traffic datasets.
- Data Cleaning and Preprocessing – Handle missing values, encode categorical data, normalize datasets.
- Feature Engineering and Selection – Extract and select relevant features.
- Model Building and Training – Implement models like Decision Tree, Random Forest, and SVM.
- Evaluation and Performance Analysis – Evaluate models using accuracy, precision, recall, F1-score.
- Alerts and Reporting – Generate alerts and summary reports.

---
## 🚀 Future Work

- Extend the system to handle **real-time traffic streams** for continuous network monitoring.  
- Explore **deep learning models** such as CNN, LSTM, and autoencoders for improved intrusion detection accuracy.  
- Integrate with **SIEM tools** for enterprise deployment and automated threat response.  
- Implement **adaptive learning** so the system can update models as new types of attacks emerge.  
- Enhance **visualization and reporting dashboards** for better insights and decision-making.  
- Optimize for **scalability** to handle large-scale network environments and high-throughput traffic.  
- Investigate **cross-dataset generalization** to ensure models perform well on diverse network datasets.  

---

## Real-World Impact
Cyber threats are constantly evolving, and organizations require proactive defenses. SentinelNet aims to **reduce the risk of data breaches, financial loss, and downtime** by providing an intelligent, adaptive intrusion detection solution that goes beyond traditional approaches.

---
## 👥 Team Members

| Name                        | Email                                         |
|-----------------------------|-----------------------------------------------|
| Amit Yadav                  | [2k23.cs2314011@gmail.com](mailto:2k23.cs2314011@gmail.com) |
| Upasana Prabhakar           | [upasanaprabhakar35@gmail.com](mailto:upasanaprabhakar35@gmail.com) |
| Shreyanshi Srivastava       | [shreyanshisrivastava19@gmail.com](mailto:shreyanshisrivastava19@gmail.com) |
| Bhavana Thota               | [bhavanathota2006@gmail.com](mailto:bhavanathota2006@gmail.com) |
| Saravanan S                 | [itssaravanan03@gmail.com](mailto:itssaravanan03@gmail.com) |
| Surya Sindhu Guthula        | [22a314408.pragati@gmail.com](mailto:22a314408.pragati@gmail.com) |
| Mehak Tripathi              | [2k22.cse.2212471@gmail.com](mailto:2k22.cse.2212471@gmail.com) |
| Anisetty Bhavitha           | [bhavithaanisetty@gmail.com](mailto:bhavithaanisetty@gmail.com) |
| Prathyay V                  | [vprathap0703@gmail.com](mailto:vprathap0703@gmail.com) |
| Vimala Reddy Tummuru        | [22501a0514@pvpsit.ac.in](mailto:22501a0514@pvpsit.ac.in) |
| Indhuja V                   | [230754.ec@rmkec.ac.in](mailto:230754.ec@rmkec.ac.in) |
| Poornitha S                 | [240061.cs@rmkec.ac.in](mailto:240061.cs@rmkec.ac.in) |
| Khushaldhia Giduthuri       | [khushaldhiagiduthuri@gmail.com](mailto:khushaldhiagiduthuri@gmail.com) |
| Bhaskar Mekala              | [bhaskarmekala209@gmail.com](mailto:bhaskarmekala209@gmail.com) |
| Chaganti Sai Sarvani        | [saisarvani.chaganti@gmail.com](mailto:saisarvani.chaganti@gmail.com) |
| Yasaswita                   | [yasaswita9@gmail.com](mailto:yasaswita9@gmail.com) |
| Sumithra G                  | [sumiad107@rmkec.ac.in](mailto:sumiad107@rmkec.ac.in) |
| Sai Sathwik Balabhadra      | [balabhadrasaisathwik@gmail.com](mailto:balabhadrasaisathwik@gmail.com) |
| Krushna Shinde              | [krushnashinde9860@gmail.com](mailto:krushnashinde9860@gmail.com) |
| Omkar Marakwar              | [omkarmarakwar5680@gmail.com](mailto:omkarmarakwar5680@gmail.com) |
| Vitesh Bhardwaj Mallibhat   | [viteshbhardwaj2186@gmail.com](mailto:viteshbhardwaj2186@gmail.com) |
| Mohan Raaj C                | [cmohanraaj0319@gmail.com](mailto:cmohanraaj0319@gmail.com) |
| Aarifa R                     | [roylamd02@gmail.com](mailto:roylamd02@gmail.com) |
| Katherine Olivia R          | [katherineolivia.r@gmail.com](mailto:katherineolivia.r@gmail.com) |
| Naga Lakshmi Durga Enugu    | [24b05a1206@svcew.edu.in](mailto:24b05a1206@svcew.edu.in) |

```
