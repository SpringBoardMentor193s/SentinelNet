# 🛡️ SentinelNet

**SentinelNet** is an AI-powered Network Intrusion Detection System (NIDS) capable of identifying malicious network traffic and cyber-attacks in real time. By leveraging machine learning techniques, the system classifies network traffic as normal or suspicious based on historical data, so organizations can detect intrusions faster and more accurately than with traditional systems.

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

##  CICIDS2017 Dataset

Since the dataset is too large for GitHub, you can download and extract it automatically:

```bash
pip install gdown
python download_data.py


---

## 📖 Documentation

Refer to [Data Overview](https://github.com/SpringBoardMentor193s/SentinelNet/blob/10bb40432b8b25131207bacf99b0d9a88d76481c/docs/data_overview.md) for details on dataset sources, schema, and summary statistics.

---

<table>

 <tr>
    <td>Amit Yadav</td>
    <td><a href="mailto:2k23.cs2314011@gmail.com">2k23.cs2314011@gmail.com</a></td>
  </tr>
  <tr>
    <td>Upasana Prabhakar</td>
    <td><a href="mailto:upasanaprabhakar35@gmail.com">upasanaprabhakar35@gmail.com</a></td>
  </tr>
  <tr>
    <td>Bhavana Thota</td>
    <td><a href="mailto:bhavanathota2006@gmail.com">bhavanathota2006@gmail.com</a></td>
  </tr>
  <tr>
    <td>Saravanan S</td>
    <td><a href="mailto:itssaravanan03@gmail.com">itssaravanan03@gmail.com</a></td>
  </tr>
  <tr>
    <td>Shreyanshi Srivastava</td>
    <td><a href="mailto:shreyanshisrivastava19@gmail.com">shreyanshisrivastava19@gmail.com</a></td>
  </tr>
  <tr>
    <td>Surya Sindhu Guthula</td>
    <td><a href="mailto:22a314408.pragati@gmail.com">22a314408.pragati@gmail.com</a></td>
  </tr>
  <tr>
    <td>Mehak Tripathi</td>
    <td><a href="mailto:2k22.cse.2212471@gmail.com">2k22.cse.2212471@gmail.com</a></td>
  </tr>
  <tr>
    <td>Anisetty Bhavitha</td>
    <td><a href="mailto:bhavithaanisetty@gmail.com">bhavithaanisetty@gmail.com</a></td>
  </tr>
  <tr>
    <td>Prathyay V</td>
    <td><a href="mailto:vprathap0703@gmail.com">vprathap0703@gmail.com</a></td>
  </tr>
  <tr>
    <td>Vimala Reddy Tummuru</td>
    <td><a href="mailto:22501a0514@pvpsit.ac.in">22501a0514@pvpsit.ac.in</a></td>
  </tr>
  <tr>
    <td>Indhuja V</td>
    <td><a href="mailto:230754.ec@rmkec.ac.in">230754.ec@rmkec.ac.in</a></td>
  </tr>
  <tr>
    <td>Poornitha S</td>
    <td><a href="mailto:240061.cs@rmkec.ac.in">240061.cs@rmkec.ac.in</a></td>
  </tr>
  <tr>
    <td>Khushaldhia Giduthuri</td>
    <td><a href="mailto:khushaldhiagiduthuri@gmail.com">khushaldhiagiduthuri@gmail.com</a></td>
  </tr>
  <tr>
    <td>Bhaskar Mekala</td>
    <td><a href="mailto:bhaskarmekala209@gmail.com">bhaskarmekala209@gmail.com</a></td>
  </tr>
  <tr>
    <td>Chaganti Sai Sarvani</td>
    <td><a href="mailto:saisarvani.chaganti@gmail.com">saisarvani.chaganti@gmail.com</a></td>
  </tr>
  <tr>
    <td>Yasaswita</td>
    <td><a href="mailto:yasaswita9@gmail.com">yasaswita9@gmail.com</a></td>
  </tr>
  <tr>
    <td>Sumithra G</td>
    <td><a href="mailto:sumiad107@rmkec.ac.in">sumiad107@rmkec.ac.in</a></td>
  </tr>
  <tr>
    <td>Sai Sathwik Balabhadra</td>
    <td><a href="mailto:balabhadrasaisathwik@gmail.com">balabhadrasaisathwik@gmail.com</a></td>
  </tr>
  <tr>
    <td>Krushna Shinde</td>
    <td><a href="mailto:krushnashinde9860@gmail.com">krushnashinde9860@gmail.com</a></td>
  </tr>
  <tr>
    <td>Omkar Marakwar</td>
    <td><a href="mailto:omkarmarakwar5680@gmail.com">omkarmarakwar5680@gmail.com</a></td>
  </tr>
  <tr>
    <td>Vitesh Bhardwaj Mallibhat</td>
    <td><a href="mailto:viteshbhardwaj2186@gmail.com">viteshbhardwaj2186@gmail.com</a></td>
  </tr>
  <tr>
    <td>Mohan Raaj C</td>
    <td><a href="mailto:cmohanraaj0319@gmail.com">cmohanraaj0319@gmail.com</a></td>
  </tr>
  <tr>
    <td>Aarifa R</td>
    <td><a href="mailto:roylamd02@gmail.com">roylamd02@gmail.com</a></td>
  </tr>
  <tr>
    <td>Katherine Olivia R</td>
    <td><a href="mailto:katherineolivia.r@gmail.com">katherineolivia.r@gmail.com</a></td>
  </tr>
  <tr>
    <td>Naga Lakshmi Durga Enugu</td>
    <td><a href="mailto:24b05a1206@svcew.edu.in">24b05a1206@svcew.edu.in</a></td>
  </tr>
</table>


