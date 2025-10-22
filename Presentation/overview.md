# 🛡️ Sentinel-Net: AI-Powered Network Intrusion Detection System

**Intern Name:** Mohan Raaj C

A high-performance Network Intrusion Detection System (NIDS) built on robust Machine Learning (ML) ensemble methods, validated against modern network traffic data, and deployed via a user-friendly Streamlit web application.

---

## 💡 I. Project Overview & Motivation

The modern digital landscape demands intelligent defense systems that surpass the capabilities of traditional signature-based security tools. This project successfully addresses the critical need for a robust **Anomaly-Based Detection** solution.

| Problem Statement | Solution (Sentinel-Net) |
| :--- | :--- |
| **Zero-day & Polymorphic Attacks** evade fixed signatures. | Leverages **Ensemble Machine Learning** (Random Forest, Gradient Boosting) for adaptive pattern recognition. |
| **High False Alarm Rate (FPR)** degrades analyst trust. | Achieves near-perfect **Specificity** (correctly identifying benign traffic) through rigorous preprocessing. |
| Network data is **High-Dimensional & Imbalanced**. | Utilizes **RobustScaler** and focuses evaluation on **Macro F1-Scores** to ensure minority class detection. |

---

## 🧠 II. Methodology and Technical Depth

The Sentinel-Net pipeline follows a rigorous, data-centric methodology to ensure reliable and consistent performance.

### 2.1 Data Sourcing & Preprocessing Foundation

| Stage | Action | Rationale |
| :--- | :--- | :--- |
| **Primary Dataset** | **CICIDS 2017** | Provides comprehensive, modern attack categories relevant to today's threats. (NSL-KDD included for reference/compatibility). |
| **Data Cleaning** | Removal of **24,025 duplicate flows** and systematic handling of missing/infinite values. | Prevents training bias and ensures data integrity. |
| **Feature Scaling** | Employed **RobustScaler** (using IQR) | Made the model robust against extreme outliers inherent in network traffic (e.g., flow byte counts). |
| **Target Creation** | Mapped flows to **Binary** (Benign vs. Attack) and **Multi-Class** (specific attack types). | Supports both general threat detection and detailed classification. |

### 2.2 Proposed Method (Model Training)

A strong ensemble-based approach was implemented to maximize detection performance against the minority attack class:

* **Models Chosen:** Random Forest, Decision Tree, Logistic Regression, and Gradient Boosting.
* **Evaluation Focus:** Strict focus on **Macro-Averaged F1-Scores** and **Recall** for minority classes, acknowledging the severe imbalance (approx. 97.8% Benign).

---

## 📈 III. Results and Evaluation Highlights

The model's performance was rigorously quantified using metrics critical for a production security environment.

### Key Performance Metrics

| Metric | Model (Sampled Test Set) | Value Achieved | Significance |
| :--- | :--- | :--- | :--- |
| **Multi-Class Accuracy** | **Random Forest** | **99.88%** | Excellent overall predictive power. |
| **Macro F1-Score** | **Random Forest** | **0.9765** | Confirms balanced performance across all attack types (not just the benign majority). |
| **Specificity** | All Models (Binary) | Near-perfect (low FPR) | Crucial for minimizing false alarms and maintaining system trust. |
| **Discriminatory Power** | Ensemble Models | **ROC-AUC near 1.0** | Signifies excellent separation capability between Normal and Attack flows across thresholds. |

---

## 💻 IV. Streamlit Deployment & Real-time Operation

The final phase packaged the entire ML pipeline into a functional interface, demonstrating the solution's real-world viability.

### Deployment Architecture

* The **Streamlit application** (`streamlit_app.py`) serves as the core user interface.
* It uses the `joblib` library to load the serialized **RobustScaler** and the final **Random Forest** model, ensuring deployment accuracy matches training integrity.

### Real-time Operation

1.  **Packet Sniffing:** Integrates the **scapy** library for non-blocking packet capture on a specified interface.
2.  **Instantaneous Feature Extraction:** Packets are immediately processed and passed through the loaded **RobustScaler**.
3.  **Real-time Classification:** The active model provides **instantaneous classification** (Benign or Attack).
4.  **User Visualization:** Results are displayed in a real-time table and statistical metrics within the Streamlit interface.

---

## 🔮 V. Conclusion and Future Work

### Conclusion

The Sentinel-Net project successfully developed a high-performance NIDS, demonstrating the superiority of **Ensemble Machine Learning** over traditional methods in classifying contemporary network threats. The final product, deployed via Streamlit, is a robust and functionally viable security tool.

### Future Works (Next Steps for Research)

1.  **Deep Learning Integration:** Implement and compare models (e.g., **1D-CNNs, LSTMs**) to capture complex, non-linear dependencies in network sequences.
2.  **Advanced Anomaly Detection:** Implement **Autoencoder-based anomaly detection** for baseline drift monitoring and unsupervised discovery of truly novel threats.
3.  **Dataset Expansion:** Incorporate newer benchmarks like **UNSW-NB15** and complete **NSL-KDD** integration for broader generalization testing.
4.  **Performance Optimization:** Further optimize model hyperparameters to reduce inference latency, enabling application in ultra-high-speed network environments.
