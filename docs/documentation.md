## NSL-KDD and CICIDS2017 Datasets

### a. Number of Features
- **NSL-KDD:** 41 features 
- **CICIDS2017:** 80+ features 

### b. Types of Attacks
- **NSL-KDD:** Denial of Service (DoS), Probe, Remote to Local (R2L), User to Root (U2R).
- **CICIDS2017:** DoS, Distributed DoS (DDoS), Brute Force, Heartbleed, Botnet, PortScan, Web Attacks, Infiltration.

### c. Differences Between the Datasets
- **NSL-KDD** is an improved version of the older KDD99 dataset, with redundant records removed. It is relatively simple, with fewer features and attack types, and is considered outdated for modern network traffic.
- **CICIDS2017** is more recent, reflecting contemporary network environments and attack vectors. It contains more features, realistic traffic, and a wider variety of attacks, making it more suitable for current intrusion detection research.

---

## The Role of AI in Cybersecurity

AI is critical in cybersecurity because it enables systems to detect, analyze, and respond to threats at a scale and speed unattainable by humans alone. With the increasing complexity and volume of cyberattacks, traditional rule-based systems struggle to keep up. AI-driven solutions can learn from vast datasets, identify subtle patterns, and adapt to new attack strategies in real time. This proactive approach is essential for defending against sophisticated threats like zero-day exploits and advanced persistent threats.

**Scalability**: Human analysts cannot manually inspect millions of packets per second; AI automates and scales detection.

**Speed**: AI detects and responds faster than traditional, signature-based systems.

**Adaptability**: Machine learning can evolve with new patterns and threats, not just known signatures.

**Reduced Human Error**: AI minimizes oversight by tirelessly applying detection logic.

**Threat Intelligence**: AI uncovers hidden or novel threat patterns by learning from huge data volumes.

---


## What Excites Me About Building SentinelNet

**Innovation Potential**: Bringing together machine learning, cybersecurity, and network engineering to fight sophisticated threats.

**Social Impact**: Greater safety for orgs and individuals, potentially catching threats early and preventing major breaches.

**Continuous Challenge**: Need to outsmart attackers who constantly change tactics, driving ongoing learning and improvement.

**Real-World Value**: Seeing your tool make a difference—detecting attacks, reducing risks, and empowering defenders.

**Learning Opportunity**: Sharpening expertise in data science, security, and software engineering—all within a practical, high-impact domain.

This SentinelNet represents the fusion of cutting-edge AI with practical cybersecurity defense.SentinelNet offers the opportunity to make a tangible impact—protecting organizations and individuals from ever-evolving cyber risks. The prospect of leveraging AI to create smarter, more resilient security solutions is both intellectually stimulating and socially meaningful.

---

## What patterns do you observe in network traffic
- Websites and apps send and receive data in a predictable way.
- Most users use common protocols like **HTTP** or **HTTPS**.
- Data sizes and connection times usually stay within normal limits.
- Specific activities have expected behaviors — for example:
  - **DNS requests** are usually very small.
  - **File downloads** are much larger.

## Why is it challenging to detect intrusions

**High Volume of Data**: Networks generate massive traffic, making manual monitoring impractical.

**Evolving Attack Patterns**: Attackers constantly develop new strategies, making static rules obsolete.

**Similarity to Normal Behavior**: Some attacks mimic legitimate traffic patterns to avoid detection.

**Imbalanced Data**: Most traffic is normal, and attacks form a small fraction, making detection harder.

**Encrypted Traffic**: Increased use of HTTPS and VPNs hides payload details, reducing visibility.

**False Positives and Negatives**: Traditional systems often misclassify, leading to alert fatigue or missed threats.

---

