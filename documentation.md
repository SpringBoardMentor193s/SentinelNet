<h1 style="font-size:36px;">SentinelNet – AI-Powered Network Intrusion Detection System (NIDS)</h1>

<h2 style="font-size:28px;">1. Introduction</h2>
<p style="font-size:18px;">
SentinelNet aims to build a <b>smart Network Intrusion Detection System (NIDS)</b> powered by <b>AI and machine learning</b>.<br>
The central goal is to automatically <b>identify and respond to suspicious or potentially harmful network traffic and cyber-attacks in real time</b>.
</p>

<p style="font-size:18px;">Using historical data, machine learning models will be trained to:</p>
<ul style="font-size:18px;">
  <li>Distinguish between normal and malicious activities</li>
  <li>Extract crucial features</li>
  <li>Classify threats</li>
  <li>Trigger alerts to help network defenders respond quickly and effectively</li>
</ul>

<h2 style="font-size:28px;">2. Literature</h2>
<p style="font-size:18px;">
The field of <b>Intrusion Detection Systems (IDS)</b> has evolved from rule-based methods to AI-powered frameworks. Literature highlights:
</p>
<ul style="font-size:18px;">
  <li><b>Signature-Based IDS:</b> Relies on predefined attack signatures, effective for known threats but fails on zero-day attacks.</li>
  <li><b>Anomaly-Based IDS:</b> Uses statistical models and ML to detect unusual traffic patterns, can detect unknown threats but may have higher false positives.</li>
</ul>

<p style="font-size:18px;">Benchmark datasets shaping IDS research:</p>
<ul style="font-size:18px;">
  <li><b>KDD Cup 1999:</b> Early dataset, criticized for redundancy and outdated attacks.</li>
  <li><b>NSL-KDD:</b> Improved version, duplicates removed, balanced dataset for academic evaluation.</li>
  <li><b>CICIDS2017:</b> Realistic enterprise traffic, modern attacks like DDoS, infiltration, and web exploits.</li>
</ul>

<p style="font-size:18px;">ML algorithms widely used:</p>
<ul style="font-size:18px;">
  <li>Decision Trees, Random Forests, SVMs, Neural Networks</li>
  <li>Deep learning, ensemble methods, hybrid IDS models</li>
</ul>

<p style="font-size:18px;">Insights:</p>
<ul style="font-size:18px;">
  <li>Feature selection and preprocessing are critical.</li>
  <li>Class imbalance is a challenge.</li>
  <li>Hybrid approaches combine speed of signature-based and intelligence of anomaly-based IDS.</li>
</ul>

<h2 style="font-size:28px;">3. Methodology</h2>

<h3 style="font-size:24px;">3.1 Database</h3>

<h4 style="font-size:20px;">3.1.1 NSL-KDD Dataset</h4>
<p style="font-size:18px;">A refined dataset to reduce redundancy:</p>
<ul style="font-size:18px;">
  <li>41 features: basic (protocol, service, bytes) + traffic-level (flags, errors)</li>
  <li>Training: 125,973 records</li>
  <li>Test: 22,544 records</li>
  <li>Attack types:
    <ul style="font-size:18px;">
      <li>DoS: smurf, neptune</li>
      <li>Probe: portsweep, nmap</li>
      <li>U2R: buffer_overflow, rootkit</li>
      <li>R2L: ftp_write, guess_passwd</li>
    </ul>
  </li>
</ul>

<h4 style="font-size:20px;">3.1.2 CICIDS2017 Dataset</h4>
<p style="font-size:18px;">Realistic enterprise network traffic:</p>
<ul style="font-size:18px;">
  <li>78–83 features: flow, statistical, packet-level</li>
  <li>Over 2.8 million labeled flow records across 5 days</li>
  <li>Attack types: DDoS (Hulk, GoldenEye, Slowloris), Brute Force, Web Attacks (SQLi, XSS), Botnet/Infiltration, Reconnaissance (PortScan, Heartbleed)</li>
</ul>

<h4 style="font-size:20px;">3.1.3 Dataset Comparison</h4>
<table border="1" cellpadding="5" cellspacing="0" style="font-size:16px;">
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
<td>>2.8 million</td>
</tr>
<tr>
<td>Traffic</td>
<td>Simulated, old-generation</td>
<td>Realistic, enterprise-scale</td>
</tr>
<tr>
<td>Usage</td>
<td>Lightweight model evaluation</td>
<td>Practical deployment</td>
</tr>
<tr>
<td>Attack Variety</td>
<td>4 legacy categories</td>
<td>14+ modern attacks</td>
</tr>
</table>

<h3 style="font-size:24px;">3.2 Preprocessing</h3>
<ul style="font-size:18px;">
  <li>Handling missing values</li>
  <li>Feature scaling: MinMaxScaler, StandardScaler</li>
  <li>Encoding categorical features: One-Hot Encoding</li>
  <li>Stratified train-test split to maintain class balance</li>
</ul>

<h4 style="font-size:20px;">3.2.1 Scaling vs Normalization</h4>
<table border="1" cellpadding="5" cellspacing="0" style="font-size:16px;">
<tr>
<th>Aspect</th>
<th>Scaling (Standardization)</th>
<th>Normalization (Min-Max)</th>
</tr>
<tr>
<td>Definition</td>
<td>Transforms features to have mean=0 and standard deviation=1</td>
<td>Rescales features to a fixed range, usually [0, 1]</td>
</tr>
<tr>
<td>Purpose</td>
<td>Handles varying feature scales for better ML performance</td>
<td>Ensures features are comparable and bounded for algorithms like Neural Networks</td>
</tr>
<tr>
<td>Use Cases</td>
<td>Algorithms assuming Gaussian distribution (SVM, Logistic Regression)</td>
<td>Algorithms sensitive to feature bounds (NNs, image data)</td>
</tr>
<tr>
<td>Effect on Outliers</td>
<td>Sensitive to outliers (outliers get compressed between 0 and 1)</td>
<td>Less sensitive, but outliers can influence mean and std</td>
</tr>
<tr>
<td>Preserves Data Shape</td>
<td>Yes, but scales features to range</td>
<td>Yes, but centers around mean 0</td>
</tr>
<tr>
<td>When to Use</td>
<td>Useful for algorithms requiring bounded input (e.g., Neural Networks, KNN)</td>
<td>Useful for algorithms assuming Gaussian distribution (e.g., Logistic Regression, SVM, PCA)</td>
</tr>
</table>

<h3 style="font-size:24px;">3.3 Novelty</h3>
<ul style="font-size:18px;">
  <li>Hybrid detection combining anomaly-based intelligence with signature-based methods</li>
  <li>Advanced preprocessing and feature selection for higher performance</li>
  <li>Class imbalance handling using SMOTE and weighted losses</li>
</ul>

<h3 style="font-size:24px;">3.4 Proposed Method</h3>
<p style="font-size:18px;">Pipeline:</p>
<ul style="font-size:18px;">
  <li>Data loading and cleaning</li>
  <li>Feature scaling and encoding</li>
  <li>Model training: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting</li>
  <li>Evaluation: Confusion Matrix, Accuracy, Precision, Recall, F1-score, ROC-AUC</li>
</ul>

<h4 style="font-size:20px;">3.4.1 Why AI is Critical in Cybersecurity</h4>
<p style="font-size:18px;">
Cybersecurity is one of the most urgent challenges today, with threats growing rapidly in both complexity and scale.<br>
Traditional rule-based methods struggle against evolving attacks, but AI enables:
</p>
<ul style="font-size:18px;">
  <li>Detecting subtle attack patterns in massive data streams</li>
  <li>Continuous learning from historical + new data</li>
  <li>Identifying zero-day threats never seen before</li>
  <li>Automating detection and response for proactive defense</li>
</ul>

<h4 style="font-size:20px;">3.4.2 What Excites Me About Building SentinelNet</h4>
<ul style="font-size:18px;">
  <li>Working with advanced datasets and algorithms</li>
  <li>Building evolving, self-improving models</li>
  <li>Delivering actionable alerts that truly help defenders</li>
  <li>Contributing to the next generation of network protection</li>
</ul>

<h4 style="font-size:20px;">3.4.3 Observed Patterns in Network Traffic</h4>
<ul style="font-size:18px;">
  <li><b>Normal traffic:</b> Predictable flows (regular request–response, consistent packet sizes, familiar IPs)</li>
  <li><b>Malicious traffic:</b> Anomalies (sudden spikes, high connection rates, port scans, repeated probes)</li>
</ul>
<p style="font-size:18px;">Examples:</p>
<ul style="font-size:18px;">
  <li>DoS floods → repetitive requests</li>
  <li>Probing → systematic service testing</li>
</ul>

<h4 style="font-size:20px;">3.4.4 Challenges in Detection</h4>
<ul style="font-size:18px;">
  <li>Attackers disguise malicious traffic as normal</li>
  <li>Massive data volume hides subtle anomalies</li>
  <li>Rare attacks (U2R, R2L) are underrepresented</li>
  <li>Encrypted traffic hides content; reliance only on metadata</li>
  <li>Balancing false positives vs false negatives is complex</li>
</ul>

<h4 style="font-size:20px;">3.4.5 Class Imbalance & Mitigation Strategies</h4>
<p style="font-size:18px;">Both NSL-KDD and CICIDS2017 suffer from imbalanced attack classes.</p>
<ul style="font-size:18px;">
  <li>Majority (DoS, DDoS) dominate</li>
  <li>Minority (U2R, R2L) are rare but critical</li>
  <li>High accuracy can still mean poor detection of rare threats</li>
</ul>

<h5 style="font-size:18px;">Mitigation Strategies</h5>
<p style="font-size:18px;">1. Data-Level Methods</p>
<ul style="font-size:18px;">
  <li>Oversampling (SMOTE): Generate synthetic rare-class samples</li>
  <li>Undersampling: Reduce majority classes</li>
  <li>Hybrid: Combine both for balance</li>
</ul>
<p style="font-size:18px;">2. Algorithm-Level Methods</p>
<ul style="font-size:18px;">
  <li>Use class weights during training</li>
  <li>Apply Focal Loss for hard-to-detect samples</li>
  <li>Use ensemble models (Random Forest, XGBoost)</li>
</ul>
<p style="font-size:18px;">3. Evaluation Metrics</p>
<ul style="font-size:18px;">
  <li>Don’t rely on accuracy alone</li>
  <li>Use Precision, Recall, F1-score</li>
  <li>Check AUC-ROC / PR curves and macro averages</li>
</ul>

<h4 style="font-size:20px;">3.4.6 Machine Learning Types</h4>
<ul style="font-size:18px;">
  <li><b>Supervised Learning:</b> Learning from labeled data where the input-output pairs are known.</li> 
  <li><b>Unsupervised Learning:</b> Learning from unlabeled data by identifying hidden patterns or groupings.</li>
  <li><b>Semi-Supervised Learning:</b> Using a small amount of labeled data with large unlabeled data.</li>
  <li><b>Reinforcement Learning:</b> Learning through trial and error using feedback/rewards.</li>
</ul>

<h4 style="font-size:20px;">3.4.7 Linear Regression Model</h4>
<p style="font-size:18px;">Linear Regression models relationships between features and target assuming linearity.</p>
<ul style="font-size:18px;">
  <li>Predicts outcome y as weighted sum of x plus bias: y = w1x1 + w2x2 + … + wnxn + b</li>
  <li>Weights learned via Ordinary Least Squares or Gradient Descent</li>
  <li>Loss: minimize Mean Squared Error</li>
</ul>
<p style="margin-left:40px; font-size:18px;"> 
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Exam_pass_logistic_curve.svg/600px-Exam_pass_logistic_curve.svg.png" alt="Logistic Curve" style="width:500px; height:400px; margin:10px 0;"> 
</p>
<p style="margin-left:40px; font-style: italic; font-size:16px; color: #555;">Logistic Curve illustrating exam pass rates</p>

<h4 style="font-size:20px;">3.4.8 Train-Test Split</h4>
<ul style="font-size:18px;">
  <li>Training Set: Train model and learn patterns</li>
  <li>Test Set: Evaluate on unseen examples</li>
  <li>Prevents overfitting, ensures reliable performance</li>
</ul>

<h4 style="font-size:20px;">3.4.9 StandardScaler</h4>
<ul style="font-size:18px;">
  <li>Centers features by subtracting mean</li>
  <li>Scales by dividing by standard deviation</li>
  <li>Ensures all features contribute equally for sensitive ML algorithms</li>
</ul>

<h2 style="font-size:28px;">4. Results</h2>

<h3 style="font-size:24px;">4.1 EDA</h3>

<p style="font-size:16px;">Exploratory Data Analysis (EDA) on the NSL-KDD and CICIDS2017 datasets provided valuable insights into data characteristics and potential challenges for modeling.</p>

<h4 style="font-size:18px;">4.1.1 Dataset Overview</h4>
<ul style="font-size:16px;">
  <li>NSL-KDD: 125,973 training records, 22,544 test records, 41 features</li>
  <li>CICIDS2017: ~2.8 million flow records, 78–83 features covering packet-level, flow-level, and statistical metrics</li>
</ul>

<h4 style="font-size:18px;">4.1.2 Class Distribution</h4>
<p style="font-size:16px;">Both datasets exhibit significant class imbalance:</p>
<ul style="font-size:16px;">
  <li>Normal traffic vs Attack traffic</li>
  <li>Majority attacks: DoS, DDoS</li>
  <li>Minority attacks: U2R, R2L (rare but critical)</li>
</ul>

<h4 style="font-size:18px;">4.1.3 Feature Statistics</h4>
<ul style="font-size:16px;">
  <li>Numeric features: Mean, median, min, max, standard deviation calculated</li>
  <li>Categorical features: Count of unique values, frequency distribution of protocols and services</li>
  <li>High correlation detected among some features (e.g., src_bytes & dst_bytes)</li>
</ul>

<h4 style="font-size:18px;">4.1.4 Missing Values & Data Quality</h4>
<ul style="font-size:16px;">
  <li>No missing values after preprocessing</li>
  <li>Categorical features encoded via One-Hot Encoding</li>
  <li>Numeric features standardized using StandardScaler or normalized with MinMaxScaler</li>
</ul>

<h4 style="font-size:18px;">4.1.5 Observed Patterns</h4>
<ul style="font-size:16px;">
  <li>Normal traffic shows predictable flows, consistent packet sizes, and familiar IPs</li>
  <li>Malicious traffic exhibits anomalies like spikes in connections, port scans, repeated probes</li>
  <li>Rare attacks (U2R, R2L) are underrepresented, necessitating oversampling techniques</li>
</ul>

<h3 style="font-size:24px;">4.2 Visualizations</h3>
<h3>  Attack Categories </h3>
<img width="600" height="400" alt="nsl_kdd_attack_categories" src="https://github.com/user-attachments/assets/fce586fc-2268-4cf9-8339-02030e4f8f61" />
<br/>
<h3> Top 10 Attack Types </h3>

<img width="1000" height="600" alt="nsl_kdd_attack_types" src="https://github.com/user-attachments/assets/933d7252-df0c-4e8f-bba4-6cb8cee78732" />

<h3>  Model Accuracy Comparison </h3>
<img width="691" height="613" alt="model_accracy" src="https://github.com/user-attachments/assets/43fe947c-bdbd-478b-9154-b66efa7aeea4" />


<h3 style="font-size:24px;">4.3 Confusion Matrices & Metrics Tables</h3>

<h4 style="font-size:20px;">4.3.1 Logistic Regression</h4>
<table border="1" cellpadding="5" cellspacing="0" style="font-size:16px;">
<tr>
<th>Metric</th>
<th>Normal</th>
<th>Attack</th>
</tr>
<tr><td>Precision</td><td>0.64</td><td>0.91</td></tr>
<tr><td>Recall</td><td>0.92</td><td>0.61</td></tr>
<tr><td>F1-score</td><td>0.76</td><td>0.73</td></tr>
<tr><td>Support</td><td>9711</td><td>12833</td></tr>
</table>
<p style="font-size:18px;">Accuracy: 74.38%</p>
<h4 style="font-size:20px;">4.3.2 Decision Tree</h4>
<table border="1" cellpadding="5" cellspacing="0" style="font-size:16px;">
<tr>
<th>Metric</th>
<th>Normal</th>
<th>Attack</th>
</tr>
<tr><td>Precision</td><td>0.69</td><td>0.96</td></tr>
<tr><td>Recall</td><td>0.97</td><td>0.67</td></tr>
<tr><td>F1-score</td><td>0.81</td><td>0.79</td></tr>
<tr><td>Support</td><td>9711</td><td>12833</td></tr>
</table>
<p style="font-size:18px;">Accuracy: 79.81%</p>

<h4 style="font-size:20px;">4.3.3 Random Forest</h4>
<table border="1" cellpadding="5" cellspacing="0" style="font-size:16px;">
<tr>
<th>Metric</th>
<th>Normal</th>
<th>Attack</th>
</tr>
<tr><td>Precision</td><td>0.66</td><td>0.97</td></tr>
<tr><td>Recall</td><td>0.97</td><td>0.61</td></tr>
<tr><td>F1-score</td><td>0.78</td><td>0.75</td></tr>
<tr><td>Support</td><td>9711</td><td>12833</td></tr>
</table>
<p style="font-size:18px;">Accuracy: 76.91%</p>

<h4 style="font-size:20px;">4.3.4 Gradient Boosting</h4>
<table border="1" cellpadding="5" cellspacing="0" style="font-size:16px;">
<tr>
<th>Metric</th>
<th>Normal</th>
<th>Attack</th>
</tr>
<tr><td>Precision</td><td>0.68</td><td>0.97</td></tr>
<tr><td>Recall</td><td>0.97</td><td>0.66</td></tr>
<tr><td>F1-score</td><td>0.80</td><td>0.79</td></tr>
<tr><td>Support</td><td>9711</td><td>12833</td></tr>
</table>
<p style="font-size:18px;">Accuracy: 79.44%</p>

<h3 style="font-size:24px;">4.4 ROC-AUC Curves</h3>
<img width="613" height="470" alt="roc_curve" src="https://github.com/user-attachments/assets/84cb2be1-f6db-4eaa-94a9-43e311809777" />

<h3 style="font-size:18px;">4.5 Confusion Matrix & Accuracy Overview</h3>
<p style="font-size:16px;">
The Confusion Matrix (CNF) provides a detailed view of model performance by comparing predicted labels against actual labels. It helps identify which classes are correctly classified and where misclassifications occur.
</p>

<p style="font-size:16px;">
For SentinelNet's evaluation on the NSL-KDD dataset, the overall accuracy was <b>76.90%</b>. This indicates that approximately 77 out of 100 instances were correctly classified, balancing detection of both normal and attack traffic.
</p>

<p style="font-size:16px;">
The confusion matrix also highlights the trade-offs between detecting majority attacks (DoS, DDoS) and rare attack types (U2R, R2L). Using metrics like Precision, Recall, and F1-score alongside accuracy ensures a more holistic assessment of the model's effectiveness.
</p>

<h3> Confusion Matrix for NSL-KDD </h3>
<img width="518" height="393" alt="confusion_metrics" src="https://github.com/user-attachments/assets/8f0280d2-1d75-46a8-878d-21a2f2b34e36" />


<h2 style="font-size:28px;">5. Discussion</h2>
<ul style="font-size:18px;">
  <li>Random Forest and ensemble methods achieved strong performance.</li>
  <li>Feature scaling and one-hot encoding improved accuracy.</li>
  <li>SMOTE reduced bias toward majority classes.</li>
  <li>F1-score preferred in imbalanced settings.</li>
</ul>

<h2 style="font-size:28px;">6. Conclusion</h2>
<p style="font-size:18px;">
SentinelNet demonstrates that <b>AI/ML-driven NIDS</b> can effectively detect cyber threats using historical data.<br>
Integration of <b>preprocessing, feature engineering, and ML</b> is key for robust intrusion detection.
</p>

<h2 style="font-size:28px;">7.Future Work</h2>
<ul style="font-size:18px;">
  <li>Deep learning approaches (CNN, RNN, Transformers)</li>
  <li>Real-time deployment</li>
  <li>IoT and cloud security expansion</li>
  <li>Explainable AI for transparent attack reasoning</li>
</ul>
