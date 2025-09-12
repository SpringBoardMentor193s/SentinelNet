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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team Information</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #333;
            line-height: 1.6;
            padding: 20px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            font-size: 2.5rem;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        
        .description {
            font-size: 1.1rem;
            color: #7f8c8d;
            max-width: 800px;
            margin: 0 auto;
        }
        
        .table-container {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            overflow-x: auto;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 600px;
        }
        
        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }
        
        th {
            background-color: #3498db;
            color: white;
            font-weight: 600;
            position: sticky;
            top: 0;
        }
        
        tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        
        tr:hover {
            background-color: #e8f4fc;
        }
        
        .email {
            color: #2980b9;
            text-decoration: none;
        }
        
        .email:hover {
            text-decoration: underline;
        }
        
        .team-size {
            margin-top: 20px;
            text-align: center;
            font-size: 1.2rem;
            color: #7f8c8d;
        }
        
        @media (max-width: 768px) {
            th, td {
                padding: 12px 10px;
            }
            
            h1 {
                font-size: 2rem;
            }
        }
        
        @media (max-width: 480px) {
            th, td {
                padding: 10px 8px;
                font-size: 0.9rem;
            }
            
            h1 {
                font-size: 1.8rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>👥 Team Information</h1>
            <p class="description">Here is the list of our project team members along with their email addresses:</p>
        </header>
        
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>Amit Yadav</td><td><a href="mailto:2k23.cs2314011@gmail.com" class="email">2k23.cs2314011@gmail.com</a></td></tr>
                    <tr><td>Upasana Prabhakar</td><td><a href="mailto:upasanaprabhakar35@gmail.com" class="email">upasanaprabhakar35@gmail.com</a></td></tr>
                    <tr><td>Bhavana Thota</td><td><a href="mailto:bhavanathota2006@gmail.com" class="email">bhavanathota2006@gmail.com</a></td></tr>
                    <tr><td>Saravanan S</td><td><a href="mailto:itssaravanan03@gmail.com" class="email">itssaravanan03@gmail.com</a></td></tr>
                    <tr><td>Shreyanshi Srivastava</td><td><a href="mailto:shreyanshisrivastava19@gmail.com" class="email">shreyanshisrivastava19@gmail.com</a></td></tr>
                    <tr><td>Surya Sindhu Guthula</td><td><a href="mailto:22a314408.pragati@gmail.com" class="email">22a314408.pragati@gmail.com</a></td></tr>
                    <tr><td>Mehak Tripathi</td><td><a href="mailto:2k22.cse.2212471@gmail.com" class="email">2k22.cse.2212471@gmail.com</a></td></tr>
                    <tr><td>Anisetty Bhavitha</td><td><a href="mailto:bhavithaanisetty@gmail.com" class="email">bhavithaanisetty@gmail.com</a></td></tr>
                    <tr><td>Prathyay V</td><td><a href="mailto:vprathap0703@gmail.com" class="email">vprathap0703@gmail.com</a></td></tr>
                    <tr><td>Vimala Reddy Tummuru</td><td><a href="mailto:22501a0514@pvpsit.ac.in" class="email">22501a0514@pvpsit.ac.in</a></td></tr>
                    <tr><td>Indhuja V</td><td><a href="mailto:230754.ec@rmkec.ac.in" class="email">230754.ec@rmkec.ac.in</a></td></tr>
                    <tr><td>Poornitha S</td><td><a href="mailto:240061.cs@rmkec.ac.in" class="email">240061.cs@rmkec.ac.in</a></td></tr>
                    <tr><td>Khushaldhia Giduthuri</td><td><a href="mailto:khushaldhiagiduthuri@gmail.com" class="email">khushaldhiagiduthuri@gmail.com</a></td></tr>
                    <tr><td>Bhaskar Mekala</td><td><a href="mailto:bhaskarmekala209@gmail.com" class="email">bhaskarmekala209@gmail.com</a></td></tr>
                    <tr><td>Chaganti Sai Sarvani</td><td><a href="mailto:saisarvani.chaganti@gmail.com" class="email">saisarvani.chaganti@gmail.com</a></td></tr>
                    <tr><td>Yasaswita</td><td><a href="mailto:yasaswita9@gmail.com" class="email">yasaswita9@gmail.com</a></td></tr>
                    <tr><td>Sumithra G</td><td><a href="mailto:sumiad107@rmkec.ac.in" class="email">sumiad107@rmkec.ac.in</a></td></tr>
                    <tr><td>Sai Sathwik Balabhadra</td><td><a href="mailto:balabhadrasaisathwik@gmail.com" class="email">balabhadrasaisathwik@gmail.com</a></td></tr>
                    <tr><td>Krushna Shinde</td><td><a href="mailto:krushnashinde9860@gmail.com" class="email">krushnashinde9860@gmail.com</a></td></tr>
                    <tr><td>Omkar Marakwar</td><td><a href="mailto:omkarmarakwar5680@gmail.com" class="email">omkarmarakwar5680@gmail.com</a></td></tr>
                    <tr><td>Vitesh Bhardwaj Mallibhat</td><td><a href="mailto:viteshbhardwaj2186@gmail.com" class="email">viteshbhardwaj2186@gmail.com</a></td></tr>
                    <tr><td>Mohan Raaj C</td><td><a href="mailto:cmohanraaj0319@gmail.com" class="email">cmohanraaj0319@gmail.com</a></td></tr>
                    <tr><td>Aarifa R</td><td><a href="mailto:roylamd02@gmail.com" class="email">roylamd02@gmail.com</a></td></tr>
                    <tr><td>Katherine Olivia R</td><td><a href="mailto:katherineolivia.r@gmail.com" class="email">katherineolivia.r@gmail.com</a></td></tr>
                    <tr><td>Naga Lakshmi Durga Enugu</td><td><a href="mailto:24b05a1206@svcew.edu.in" class="email">24b05a1206@svcew.edu.in</a></td></tr>
                </tbody>
            </table>
        </div>
        
        <div class="team-size">
            <p>Total Team Members: <strong>26</strong></p>
        </div>
    </div>
</body>
</html>
