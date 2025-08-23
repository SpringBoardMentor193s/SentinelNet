📄 Dataset Description
1. Dataset Name

NSL-KDD Dataset
(Files: KDDTrain+.txt, KDDTest+.txt)

2. Source

Derived from the KDD Cup 1999 dataset, improved by the University of New Brunswick (UNB).

Designed to remove redundant records and address issues in the original dataset.

Widely used for network intrusion detection system (IDS) research.

3. Contents of the Dataset

KDDTrain+.txt → Training data (~125,973 records)

KDDTest+.txt → Testing data (~22,544 records)

Each record represents a network connection, described by 41 features and a class label (attack type or normal).

4. Features (41 Attributes)

The dataset contains continuous, discrete, and symbolic attributes.

a) Basic Features (Individual TCP Connections)

duration → length of the connection (seconds)

protocol_type → protocol used (TCP, UDP, ICMP)

service → network service on destination (e.g., http, ftp, telnet)

flag → status flag of the connection

src_bytes → number of data bytes from source to destination

dst_bytes → number of data bytes from destination to source

b) Content Features (Within a Connection)

land → 1 if connection from/to same host & port, else 0

wrong_fragment → number of wrong fragments

urgent → number of urgent packets

hot → count of suspicious activities

num_failed_logins → failed login attempts

logged_in → 1 if login successful, else 0

num_compromised → number of compromised conditions

root_shell → 1 if root shell obtained, else 0

su_attempted → 1 if “su root” command attempted, else 0

num_root → number of root accesses

num_file_creations → number of file creation operations

num_shells → number of shell prompts invoked

num_access_files → number of access control file operations

num_outbound_cmds → number of outbound FTP commands

is_host_login → 1 if host login, else 0

is_guest_login → 1 if guest login, else 0

c) Traffic Features (Same Host & Service Window)

count → connections to the same host in past 2 seconds

srv_count → connections to the same service in past 2 seconds

serror_rate → % of connections with SYN errors

srv_serror_rate → % of same service connections with SYN errors

rerror_rate → % of connections with REJ errors

srv_rerror_rate → % of same service connections with REJ errors

same_srv_rate → % of same service connections

diff_srv_rate → % of different service connections

srv_diff_host_rate → % of same service connections but to different hosts

d) Host-Based Traffic Features

dst_host_count → connections to same host

dst_host_srv_count → connections to same service

dst_host_same_srv_rate → % of connections to same service

dst_host_diff_srv_rate → % of connections to different services

dst_host_same_src_port_rate → % of connections to same source port

dst_host_srv_diff_host_rate → % of same service connections to different host

dst_host_serror_rate → % of connections with SYN errors

dst_host_srv_serror_rate → % of same service connections with SYN errors

dst_host_rerror_rate → % of connections with REJ errors

dst_host_srv_rerror_rate → % of same service connections with REJ errors

5. Labels (Target Variable)

Each record is labeled as:

normal → normal network traffic

attack → one of the following categories:

DoS (Denial of Service) → e.g., smurf, neptune

Probe → surveillance & probing (e.g., nmap, ipsweep)

R2L (Remote to Local) → e.g., guess_passwd, ftp_write

U2R (User to Root) → e.g., buffer_overflow, rootkit

6. Use in Project

This dataset is used to:

Train and evaluate machine learning / deep learning models for intrusion detection

Benchmark algorithms for cybersecurity and anomaly detection