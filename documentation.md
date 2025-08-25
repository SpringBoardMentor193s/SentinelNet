# 🔐 SentinelNet Project Statement – In My Own Words

SentinelNet aims to build a **smart Network Intrusion Detection System (NIDS)** powered by **AI and machine learning**.  
The central goal is to automatically **identify and respond to suspicious or potentially harmful network traffic and cyber-attacks in real time**.  

Using historical data, machine learning models will be trained to:
- Distinguish between normal and malicious activities  
- Extract crucial features  
- Classify threats  
- Trigger alerts to help network defenders respond quickly and effectively  



## 📂 **Datasets: NSL-KDD and CICIDS2017**

### 🌐 **NSL-KDD Dataset**
A refined dataset designed to reduce redundancy, widely used as a benchmark for evaluating intrusion detection models in research.

- **Removes duplicate records**, reducing bias in training and testing.  

**a) Features:**  
- Number of Features: **41**  
- Captures both basic (protocol, service, bytes) and traffic-level indicators (flags, error rates, etc.)  

**Volume:**  
- Training set: **125,973 records**  
- Test set: **22,544 records**  

**Data Format:**  
- Structured tabular format with clearly labeled classes  
- Suitable for supervised learning  

**b) Attack Types:**  
- **Denial of Service (DoS):** Overwhelming services with excessive traffic (e.g., *smurf, neptune*)  
- **Probe:** Network scanning and reconnaissance (e.g., *portsweep, nmap*)  
- **User to Root (U2R):** Privilege escalation (e.g., *buffer_overflow, rootkit*)  
- **Remote to Local (R2L):** Unauthorized local access (e.g., *ftp_write, guess_passwd*)  



### 🌐 **CICIDS2017 Dataset**
Simulates **real-world enterprise network traffic** with both normal activity and diverse cyberattacks.  

- Reflects realistic enterprise traffic combining benign and malicious flows.  

**Features:**  
- Number of Features: **78–83**  
- Includes flow, statistical, and packet-level features (packet size, timing, byte counts).  

**Volume:**  
- Over **2.8 million labeled flow records** generated across 5 consecutive days.  

**Data Format:**  
- Available as **CSV** files (ML-ready) and **PCAP** files (detailed packet analysis).  

**Attack Types:**  
- **DoS/DDoS:** Hulk, GoldenEye, Slowloris, LOIC  
- **Brute Force:** FTP, SSH, web logins  
- **Web Attacks:** SQL Injection, XSS, Web Brute Force  
- **Botnet & Infiltration:** Malicious bot activity and external break-ins  
- **Reconnaissance & Exploits:** PortScan, Heartbleed  



## 📊 **Differences Between Datasets**

<table>
<tr>
<th>Attribute</th>
<th>NSL-KDD</th>
<th>CICIDS2017</th>
</tr>
<tr>
<td>No. of Features</td>
<td>41</td>
<td>78–83</td>
</tr>
<tr>
<td>Total Records</td>
<td>~150,000</td>
<td>Over 2.8 million</td>
</tr>
<tr>
<td>Traffic</td>
<td>Simulated, old-generation</td>
<td>Realistic, large-scale enterprise</td>
</tr>
<tr>
<td>Usage</td>
<td>Lightweight model evaluation</td>
<td>Practical deployment</td>
</tr>
<tr>
<td>Attack Variety</td>
<td>4 legacy categories</td>
<td>Wide, modern attacks (14+)</td>
</tr>
</table>



## 🔐 **Why is AI Critical in Cybersecurity?**  
### 🚀 **What Excites Me About Building SentinelNet**

Cybersecurity is one of the **most urgent challenges today**, with threats growing rapidly in both complexity and scale.  
Traditional rule-based methods struggle against evolving attacks, but **AI enables:**
- Detecting subtle attack patterns in massive data streams  
- Continuous learning from historical + new data  
- Identifying zero-day threats never seen before  
- Automating detection and response for proactive defense  

What excites me is the **fusion of technical innovation with real-world impact**:  
- Working with advanced datasets and algorithms  
- Building evolving, self-improving models  
- Delivering **actionable alerts** that truly help defenders  
- Contributing to the **next generation of network protection**  



## 🔍 **Observed Patterns in Network Traffic**

- **Normal traffic:** Predictable flows (regular request–response, consistent packet sizes, familiar IPs)  
- **Malicious traffic:** Anomalies (sudden spikes, high connection rates, port scans, repeated probes)  

**Examples:**  
- DoS floods → repetitive requests  
- Probing → systematic service testing  

**Challenges in Detection:**  
- Attackers disguise malicious traffic as normal  
- Massive data volume hides subtle anomalies  
- Rare attacks (U2R, R2L) are underrepresented  
- Encrypted traffic hides content; reliance only on metadata  
- Balancing **false positives vs false negatives** is complex  



## ⚖️ **Class Imbalance & Mitigation Strategies**

Both **NSL-KDD** and **CICIDS2017** suffer from **imbalanced attack classes**.  
- Majority (DoS, DDoS) dominate  
- Minority (U2R, R2L) are rare but critical  
- High accuracy can still mean poor detection of rare threats  

### ✅ **Mitigation Strategies**

**1. Data-Level Methods**  
- **Oversampling (SMOTE):** Generate synthetic rare-class samples  
- **Undersampling:** Reduce majority classes  
- **Hybrid:** Combine both for balance  

**2. Algorithm-Level Methods**  
- Use **class weights** during training  
- Apply **Focal Loss** for hard-to-detect samples  
- Use **ensemble models** (Random Forest, XGBoost)  

**3. Evaluation Metrics**  
- Don’t rely on **accuracy** alone  
- Use **Precision, Recall, F1-score**  
- Check **AUC-ROC / PR curves** and **macro averages**  



✨ *SentinelNet represents the vision of an intelligent, flexible, and resilient intrusion detection system, built to evolve alongside modern cyber threats.*  
