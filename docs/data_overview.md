# Data Overview

## NSL-KDD
- Features: The NSL-KDD dataset has 41 features related to network traffic, with an additional 42nd feature for the class label (normal or attack)
- Types of Attacks: 
        ○ DoS (Denial of Service)
        ○ U2R (User to Root)
        ○ R2L (Remote to Local)
        ○ Probe (Probing)

Schema:
- Duration, protocol_type, service, flag, src_bytes, dst_bytes, …, label.

## CICIDS2017 Dataset
- Features: The CICIDS2017 dataset contains 80-84 features, depending on the specific file and analysis method used. These features are extracted from network flows using the CICFlowMeter tool.
- Types of Attacks: 
        ○ DDoS (Distributed Denial of Service)
        ○ DoS (Denial of Service)
        ○ Brute Force (FTP/SSH)
        ○ Web Attacks (Brute Force, XSS, SQL Injection)
        ○ Infiltration
        ○ Botnet
        ○ Port Scan
        ○ Heartbleed

## Key Differences
- NSL-KDD: smaller, outdated attack types, simpler structure.  
- CICIDS2017: larger, more realistic, modern attacks, richer metadata.