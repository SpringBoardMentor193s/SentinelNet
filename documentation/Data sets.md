# 🛡️ NSL-KDD Dataset

### 🔹 Background

* **Origin**: Derived from the **KDD Cup 1999** dataset (which itself was built from DARPA 1998 IDS evaluation program).
* **Motivation**: The original **KDD’99 dataset** had serious flaws:

  * Huge number of redundant and duplicate records.
  * Severe class imbalance (DoS attacks dominated).
  * Biased towards certain attack patterns.
* **NSL-KDD** was proposed as an improved version, with redundant records removed, making it a **cleaner and more balanced dataset** for training and evaluation.

---

### 🔹 Structure

* Two main subsets:

  * **KDDTrain+.txt** (training set)
  * **KDDTest+.txt** (test set)
* Each record corresponds to a **network connection** represented by **41 features + 1 label**.

---

### 🔹 Features

Features fall into **four main groups**:

1. **Basic Features** – extracted from packet headers (e.g., duration, protocol, service, src\_bytes, dst\_bytes).
2. **Content Features** – look for suspicious content (e.g., number of failed logins, shell prompts, root access).
3. **Traffic Features (time-based)** – analyze patterns in the past 2 seconds (e.g., count, serror\_rate, same\_srv\_rate).
4. **Host-based Traffic Features** – analyze connections over a larger window (e.g., dst\_host\_count, dst\_host\_srv\_rate).

* **Target Label**: Each connection is classified as:

  * `normal`
  * or one of **attack types**, grouped into categories:

    * **DoS (Denial of Service)** – e.g., smurf, neptune, back.
    * **Probe** – e.g., ipsweep, portsweep, nmap.
    * **R2L (Remote to Local)** – e.g., ftp\_write, guess\_passwd, warezclient.
    * **U2R (User to Root)** – e.g., buffer\_overflow, rootkit.

---

### 🔹 Size

* **KDDTrain+**: \~125,973 records.
* **KDDTest+**: \~22,544 records.
* Balanced compared to KDD’99 but still has **imbalances across categories** (DoS is much more frequent).

---

### 🔹 Use Cases

* Benchmark dataset for **machine learning intrusion detection research**.
* Used for **classification** (attack type prediction) and **anomaly detection**.
* Good for testing algorithms’ ability to detect **rare attacks (R2L, U2R)**.

---

---

# 🛡️ CICIDS2017 Dataset

### 🔹 Background

* **Released by**: Canadian Institute for Cybersecurity (CIC), University of New Brunswick (2017).
* **Motivation**: To provide a **realistic, modern, and comprehensive dataset** for intrusion detection, overcoming limitations of old datasets like NSL-KDD.
* **Setup**: Data was collected over **5 days (Monday–Friday)** in a **realistic testbed**:

  * Real traffic (HTTP, HTTPS, FTP, SSH, email, streaming, VoIP, etc.).
  * Attacks generated using penetration testing tools.

---

### 🔹 Structure

* Contains **PCAP files** (raw packet captures) and **CSV/Parquet versions** with extracted features.
* Each flow (connection) is described by around **80 network flow features** such as:

  * Duration, Protocol, Source/Destination IP & Port.
  * Packet/byte statistics (e.g., flow\_bytes, avg\_pkt\_size).
  * Time-based features (flow\_duration, active/idle times).

---

### 🔹 Attack Types

The dataset includes both **benign traffic** and multiple **attack categories**:

1. **DoS/DDoS Attacks** – e.g., DoS Hulk, GoldenEye, Slowloris, SlowHTTPTest.
2. **Brute Force Attacks** – FTP-Patator, SSH-Patator.
3. **Web Attacks** – XSS, SQL Injection, Command Injection.
4. **Infiltration Attacks** – malware infiltrating the network.
5. **Botnet Traffic** – e.g., ARES botnet.
6. **Port Scan / Network Reconnaissance**.

---

### 🔹 Size

* Approx. **2.8 million network flows** in total.
* Balanced **per-day subsets**:

  * **Monday**: Only benign traffic.
  * **Tuesday–Friday**: Mix of benign + different attack scenarios.

---

### 🔹 Why It’s Important

* More **realistic and modern** than NSL-KDD.
* Represents **current-day attack vectors** (e.g., web attacks, botnets, DDoS).
* Contains **labeled data**, useful for both **supervised ML** and **unsupervised anomaly detection**.
* Large scale → better for testing **deep learning** models.

---

# 🔄 NSL-KDD vs CICIDS2017

| Aspect            | **NSL-KDD**                 | **CICIDS2017**                                           |
| ----------------- | --------------------------- | -------------------------------------------------------- |
| Year Released     | 2009                        | 2017                                                     |
| Derived From      | KDD’99                      | Realistic testbed traffic                                |
| Records           | \~150K                      | \~2.8M flows                                             |
| Features          | 41                          | \~80                                                     |
| Traffic Type      | Simulated DARPA traffic     | Realistic modern traffic                                 |
| Attack Categories | DoS, Probe, R2L, U2R        | DoS/DDoS, Brute Force, Botnet, Web Attacks, Infiltration |
| Realism           | Synthetic, outdated         | Modern, realistic                                        |
| Usage             | Classic ML IDS benchmarking | Deep learning, real-world IDS evaluation                 |

---

✅ **In summary**:

* **NSL-KDD** is best for **classical ML experiments** and comparing with older studies.
* **CICIDS2017** is better for **realistic, large-scale, modern IDS research**.

---

