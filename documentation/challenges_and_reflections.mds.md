# Network Traffic Patterns and Intrusion Detection Challenges

## What patterns do you observe in network traffic?
- **Normal Usage Patterns:** Regular requests such as web browsing, emails, and streaming show predictable frequencies and packet sizes.  
- **Protocol-Specific Behavior:** HTTP, HTTPS, DNS, and FTP exhibit unique traffic signatures that can be distinguished.  
- **Time-Based Trends:** Traffic volume often varies depending on time of day, peak hours, and scheduled tasks.  
- **Repetitive Flows:** Legitimate applications generate recurring communication flows with consistent endpoints.  
- **Anomalies/Spikes:** Sudden surges, unusual ports, or large data transfers may indicate potential malicious activity.  

## Why is it challenging to detect intrusions?
- **High Volume of Data:** Networks generate massive amounts of traffic, making manual inspection infeasible.  
- **Normal vs Malicious Overlap:** Malicious traffic often mimics normal traffic patterns to avoid detection.  
- **Encrypted Traffic:** Widespread use of encryption (e.g., HTTPS) makes payload inspection difficult.  
- **Evolving Threats:** Attackers continuously adapt techniques, creating zero-day exploits and new intrusion methods.  
- **False Positives/Negatives:** Balancing sensitivity and accuracy is challenging — too strict causes false alarms, too lenient misses real threats.  
- **Distributed Attacks:** Intrusions may occur from multiple sources or in low-volume distributed patterns, making them harder to spot.  
