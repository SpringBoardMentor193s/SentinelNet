<h1>🔐 Network Intrusion Detection Datasets Overview</h1>

<h2>1. 📂 NSL-KDD Dataset</h2>

<h3>📌 Dataset Source</h3>
<ul>
  <li><strong>File:</strong> KDDTrain+.txt</li>
  <li><strong>Description:</strong> NSL-KDD is a cleaned and improved version of the KDD Cup 1999 dataset, addressing redundancy and imbalance issues.</li>
</ul>

<h3>📊 Dataset Shape</h3>
<ul>
  <li><strong>Number of rows:</strong> 125,973</li>
  <li><strong>Number of columns:</strong> 42</li>
  <li><strong>Label column:</strong> Last column</li>
</ul>

<h3>🏷️ Labels</h3>
<ul>
  <li><strong>Unique labels:</strong> normal, neptune, smurf, satan, ipsweep, and others</li>
  <li><strong>Top 5 attack types:</strong>
    <ol>
      <li>neptune</li>
      <li>smurf</li>
      <li>normal</li>
      <li>satan</li>
      <li>ipsweep</li>
    </ol>
  </li>
</ul>

<hr>

<h2>2. 📂 CICIDS2017 Dataset</h2>

<h3>📌 Dataset Source</h3>
<ul>
  <li><strong>File:</strong> DoS-Wednesday-no-metadata.parquet</li>
  <li><strong>Description:</strong> CICIDS2017 replicates realistic network traffic, blending normal activities with diverse modern cyber-attacks for effective intrusion detection research.</li>
</ul>

<h3>📊 Dataset Shape</h3>
<ul>
  <li><strong>Rows and columns:</strong> 2,830,000+ × 80+</li>
  <li><strong>Label column:</strong> Label</li>
</ul>

<h3>🏷️ Labels</h3>
<ul>
  <li><strong>Unique attack types:</strong> DoS Hulk, DoS GoldenEye, DoS slowloris, DDoS, PortScan, FTP-Patator, SSH-Patator, Normal</li>
  <li><strong>Top 5 frequent attack types:</strong>
    <ol>
      <li>DoS Hulk</li>
      <li>DoS GoldenEye</li>
      <li>DoS slowloris</li>
      <li>DDoS</li>
      <li>PortScan</li>
    </ol>
  </li>
</ul>

<hr>

<h2>📌 Summary</h2>
<p>
  Both datasets are valuable benchmarks for intrusion detection.  
  <strong>NSL-KDD</strong>  is smaller, classical, and widely used for quick experimentation.  
  <strong>CICIDS2017</strong>  is large-scale, modern, and closely reflects real-world traffic patterns and attack behaviors.  
</p>
