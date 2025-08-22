# 📌 What is NSL-KDD?

The NSL-KDD dataset is an improved version of the KDD’99 dataset, which was originally created for the 1999 DARPA Intrusion Detection Evaluation Program.
It is widely used for network intrusion detection system (NIDS) research.

The improvements over KDD’99:

Removed redundant records (avoids bias toward frequent attack types).

Provides a more balanced training and testing set.

Includes multiple test sets with different difficulty levels.

# 📂 Files in Your Dataset

KDDTrain+.txt / KDDTrain+.arff → Full training dataset.

KDDTrain+_20Percent.txt → A smaller (20%) subset for faster experiments.

KDDTest+.txt / KDDTest+.arff → Standard test dataset.

KDDTest-21.txt → A more challenging test set with attack types not present in training (to test generalization).

# 📑 Data Structure

Each record represents a network connection with 41 features + 1 level:

Basic Features (duration, protocol_type, service, src_bytes, dst_bytes, etc.)

Content Features (number of failed logins, root access, etc.)

Traffic Features (connections to same host, error rates, etc.)

Level → Either normal or an attack type.

# 🚨 Attack Categories

Attacks are grouped into 4 main categories:

DoS (Denial of Service) → e.g., smurf, neptune, teardrop.

Probe (Surveillance/Scanning) → e.g., satan, ipsweep, nmap.

R2L (Remote to Local) → e.g., guess_passwd, ftp_write.

U2R (User to Root) → e.g., buffer_overflow, rootkit.