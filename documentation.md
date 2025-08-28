# NSL-KDD Dataset
# project summary
SentinelNet is an AI-powered Network Intrusion Detection System (NIDS) designed to detect and classify malicious network traffic in real time. By leveraging machine learning techniques, the system processes network traffic data, extracts relevant features, trains classification models, and generates alerts for anomalies. The project uses two well-known datasets:

NSL-KDD – classical benchmark dataset for intrusion detection.
CICIDS2017 – modern, realistic dataset containing diverse cyberattacks.
# Number of Features:
The NSL-KDD dataset contains 42 features for each record.

# The list of features 

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/e0a78c10-d5ff-456a-bf9e-7ba9f13333b2" />


# Attack Categories:
It primarily includes four types of attacks:

Denial of Service (DoS)

Probe (reconnaissance)

User-to-Root (U2R)

Remote-to-Local (R2L)

# Key Characteristics:

NSL-KDD is a refined and cleaned version of the older KDD-99 dataset, with redundant records removed to reduce bias.

While smaller and simpler, it still faces limitations such as outdated attack scenarios and traffic that is simulated rather than real.

CICIDS2017 Dataset

# Number of Features:
CICIDS2017 provides over 80 features per network flow, extracted using tools like CICFlowMeter.

# Attack Categories:
It covers a wider and more modern range of cyber-attacks, including:

Brute Force (FTP and SSH)

Denial of Service (DoS) and Distributed DoS (DDoS)

Infiltration attacks

Web-based attacks (e.g., XSS, SQL Injection)

Heartbleed

Botnets

Port scanning

# Key Characteristics:

Captures realistic traffic generated over a 5-day period, blending normal user behavior with planned attack scenarios.

Offers greater diversity, with labeled flows, multiple protocols (HTTP, HTTPS, FTP, SSH, email), and rich metadata.

Much larger and more comprehensive than NSL-KDD, making it highly relevant to modern cybersecurity research.

