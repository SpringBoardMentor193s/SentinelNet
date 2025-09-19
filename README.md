# SentinelNet – AI-Powered Network Intrusion Detection System
## Overview

SentinelNet is an intelligent Network Intrusion Detection System (NIDS) that harnesses the power of machine learning (ML) and deep learning (DL) to secure networks against malicious activity. It analyzes traffic flows, identifies anomalies, and classifies cyber threats to strengthen modern defense mechanisms.


## Project Goal

The main objective of SentinelNet is to build a next-generation NIDS capable of detecting cyber-attacks and abnormal traffic in real time. By applying ML algorithms to historical and live data, the system learns to distinguish between legitimate traffic and suspicious activity, supporting proactive cybersecurity.

## Key Features

Traffic Processing: Data cleaning, preprocessing, and feature engineering on benchmark datasets (NSL-KDD & CIC-IDS 2017).

Model Development: Training and evaluation of ML/DL models for multi-class intrusion detection.

Visual Insights: Dashboards and plots showing attack trends, distribution, and model performance.

Planned Real-Time Module: Future integration for live packet capture and streaming classification.

Attack Categorization: Classifies connections as normal or anomalous, and further categorizes anomalies into attack families.

## Project Structure


SentinelNet/
│── data/ # Datasets (NSL-KDD, CIC-IDS 2017)
│ ├── nslkdd/ # Raw + processed NSL-KDD dataset files
│ └── cicids2017/ # Raw + processed CIC-IDS 2017 dataset
│
│── scripts/ # Python scripts for modular workflows
│ └── main.py # Main pipeline script
│
│── notebooks/ # Colab notebooks
│
│── docs/ # Documentation, reports, research notes
│ ├── reflection_docs/ # Reflections & notes
│ ├── linear_regression.md
│ ├── mlmodels.md
│ └── documentation.md
│
│── LICENSE
│── requirements.txt # Python dependencies
│── README.md # Project documentation


## Datasets Used
The project uses well-known public network intrusion datasets for training and testing:

NSL-KDD Dataset: https://www.unb.ca/cic/datasets/nsl.html

CICIDS2017 Dataset: https://www.unb.ca/cic/datasets/ids-2017.html

## 🔧 Tools & Technologies

Language: Python

Libraries: Pandas, NumPy, Matplotlib, Scikit-learn, Seaborn


## Future Work
Real-Time Intrusion Detection – Extend the system to analyze live network traffic using packet sniffing for on-the-fly attack detection.

Deep Learning Models – Integrate advanced models (LSTM, CNN, Transformers) to improve detection accuracy for complex attack patterns.

Visualization Dashboard – Build an interactive dashboard to display attack trends, detection results, and system performance in real time.

## License
This project is licensed under the MIT License – see LICENSE for details.
