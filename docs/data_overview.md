# SentinelNet Project Statement and Summarize the goals

SentinelNet aims to build an AI-powered Network Intrusion Detection System (NIDS) that can intelligently monitor and secure network traffic in real time. The project’s core goals are:

Detect Threats Early – Use advanced AI (like LLaMA models) to spot unusual or malicious patterns in network traffic before they cause harm.

Reduce False Alarms – Improve detection accuracy so that security teams aren’t overwhelmed by unnecessary alerts.

Faster Response – Provide instant notifications and insights to help organizations act quickly against cyberattacks.

Improve Resilience – Make networks more secure and reliable by automatically identifying vulnerabilities and abnormal behaviors.

Bridge Data and Defense – Leverage benchmark datasets (NSL-KDD, CICIDS2017) to train models that can handle both classic and modern cyber threats.

# NSL-KDD and CICIDS2017 Datasets

# NSL-KDD Dataset

a. Number of Features
The dataset includes 41 input features per record, plus 1–2 additional fields (such as class levels and/or a score)

b. Types of Attacks
Attack types are grouped into four main categories:
DoS (Denial of Service)
Probe (surveillance/ scanning)
U2R (User to Root) – escalating privileges from user to root
R2L (Remote to Local) – gaining local access from a remote entry
The dataset includes a total of 39 distinct attack variants, spread across those four categories

c. Key Differences / Characteristics
Quality improvements: NSL-KDD was built to eliminate duplicate and redundant records present in the original KDD Cup ’99 dataset, resulting in cleaner training and testing splits
It retains the same general structure (41 features, four attack categories) but addresses issues like redundancy and class imbalance from its predecessor
Despite improvements, it’s still older and less representative of modern, complex traffic scenarios.

# CICIDS2017 Dataset

a. Number of Features
The dataset contains approximately 79 features, based on flow-derived network metrics 
Some sources mention that feature sets can extend beyond 80; often, around 84 or more features are used depending on the feature extraction method 

b. Types of Attacks
The dataset captures a wide range of modern, realistic attacks, including:
Brute Force (FTP and SSH)
DoS and DDoS
Web attacks (like SQL injection, XSS)
Infiltration
Botnet
Heartbleed 

c. Key Differences / Characteristics Compared to NSL-KDD

Modernity: CICIDS2017 was created in 2017 with real-world PCAP captures, profiling realistic user behavior and network conditions 
Traffic richness: Includes diverse protocols (HTTP, HTTPS, FTP, SSH, email) and comprehensive flow-based metadata 
Attack diversity: Covers newer, more varied threats beyond the classic four categories of NSL-KDD 
Feature volume and granularity: Much larger feature set (circa 79–80+) with fine-grained flow-level traffic insights 
Class imbalance and complexity: Contains numerous attack classes (often up to 15 or more distinct levels), reflecting more realistic and imbalanced network conditions

## Dataset sources and schema

# NSL-KDD Dataset Overview

## 1. Dataset Source
- **Name:** NSL-KDD  
- **Description:** NSL-KDD is a refined version of the KDD’99 dataset, created for network intrusion detection research. Duplicate records have been removed to reduce bias, and training/testing splits are carefully balanced.  
- **Download Link:** [NSL-KDD Dataset](https://www.kaggle.com/datasets/hassan06/nslkdd)  
- **File Structure:**  
    data/
        NSL-KDD/
            KDDTrain+.txt # Training set


## 2. Dataset Schema
The dataset contains **42 columns**: 41 features + 1 level (attack type).  

### 2.1 Feature Types

| Feature Name                | Type        | Description |
|-----------------------------|------------|-------------|
| duration                     | numeric    | Length of connection (seconds) |
| protocol_type                | categorical| TCP, UDP, ICMP |
| service                      | categorical| Network service on destination (http, ftp, etc.) |
| flag                         | categorical| Normal or error status of the connection |
| src_bytes                     | numeric    | Bytes sent from source to destination |
| dst_bytes                     | numeric    | Bytes sent from destination to source |
| land                         | categorical| 1 if connection is from/to same host/port, else 0 |
| wrong_fragment               | numeric    | Number of wrong fragments |
| urgent                       | numeric    | Number of urgent packets |
| hot                          | numeric    | Number of “hot” indicators (suspicious activity) |
| num_failed_logins            | numeric    | Number of failed login attempts |
| logged_in                    | categorical| 1 if successfully logged in, else 0 |
| num_compromised              | numeric    | Number of compromised conditions |
| root_shell                   | numeric    | 1 if root shell is obtained, else 0 |
| su_attempted                 | numeric    | Number of `su` attempts |
| num_root                     | numeric    | Number of root accesses |
| num_file_creations           | numeric    | Number of file creation operations |
| num_shells                   | numeric    | Number of shell prompts |
| num_access_files             | numeric    | Number of sensitive files accessed |
| num_outbound_cmds            | numeric    | Number of outbound commands |
| is_host_login                | categorical| 1 if host login, else 0 |
| is_guest_login               | categorical| 1 if guest login, else 0 |
| count                        | numeric    | Connections to the same host in past 2 seconds |
| srv_count                    | numeric    | Connections to same service in past 2 seconds |
| serror_rate                  | numeric    | % of connections with SYN errors |
| srv_serror_rate              | numeric    | % of connections with SYN errors for same service |
| rerror_rate                  | numeric    | % of connections with REJ errors |
| srv_rerror_rate              | numeric    | % of connections with REJ errors for same service |
| same_srv_rate                | numeric    | % of connections to same service |
| diff_srv_rate                | numeric    | % of connections to different service |
| srv_diff_host_rate           | numeric    | % of connections to different host |
| dst_host_count               | numeric    | Connections to destination host |
| dst_host_srv_count           | numeric    | Connections to same service on destination host |
| dst_host_same_srv_rate       | numeric    | % of connections to same service on destination host |
| dst_host_diff_srv_rate       | numeric    | % of connections to different service on destination host |
| dst_host_same_src_port_rate  | numeric    | % of connections from same source port |
| dst_host_srv_diff_host_rate  | numeric    | % of connections to same service but different host |
| dst_host_serror_rate         | numeric    | % of connections to host with SYN errors |
| dst_host_srv_serror_rate     | numeric    | % of connections to host/service with SYN errors |
| dst_host_rerror_rate         | numeric    | % of connections to host with REJ errors |
| dst_host_srv_rerror_rate     | numeric    | % of connections to host/service with REJ errors |
| level                        | categorical| Attack type (`normal`, `neptune`, `smurf`, etc.) |

## 3. Notes
- The dataset includes **numeric and categorical features**. Some may need **encoding or scaling** for machine learning models.  
- **Class Imbalance:** DoS attacks dominate, while U2R and R2L are rare. Consider resampling or weighted loss during model training.  
- Visualizations such as **attack type distribution** and **category grouping** are helpful to understand dataset imbalance.  

