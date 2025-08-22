### &nbsp;                        **NSL-KDD Dataset Overview**





#### **Dataset Source:**



The NSL-KDD dataset is a benchmark dataset for network intrusion detection.

Source: NSL-KDD Dataset







##### **Files Used:**



KDDTrain+.txt – Training dataset









#### **Dataset Description:**



The dataset contains 125,973 network connection records with 43 columns. Each record describes a connection with numeric and categorical features and is labeled as normal or a specific attack type.



#### **Columns / Features:**



1. **duration**
2. **protocol\_type**
3. **service**
4. **flag**
5. **src\_bytes**
6. **dst\_bytes**
7. **land**
8. **wrong\_fragment**
9. **urgent**
10. **hot**
11. **num\_failed\_logins**
12. **logged\_in**
13. **num\_compromised**
14. **root\_shell**
15. **su\_attempted**
16. **num\_root**
17. **num\_file\_creations**
18. **num\_shells**
19. **num\_access\_files**
20. **num\_outbound\_cmds**
21. **is\_host\_login**
22. **is\_guest\_login**
23. **count**
24. **srv\_count**
25. **serror\_rate**
26. **srv\_serror\_rate**
27. **rerror\_rate**
28. **srv\_rerror\_rate**
29. **same\_srv\_rate**
30. **diff\_srv\_rate**
31. **srv\_diff\_host\_rate**
32. **dst\_host\_count**
33. **dst\_host\_srv\_count**
34. **dst\_host\_same\_srv\_rate**
35. **dst\_host\_diff\_srv\_rate**
36. **dst\_host\_same\_src\_port\_rate**
37. **dst\_host\_srv\_diff\_host\_rate**
38. **dst\_host\_serror\_rate**
39. **dst\_host\_srv\_serror\_rate**
40. **dst\_host\_rerror\_rate**
41. **dst\_host\_srv\_rerror\_rate**
42. **label – Specific attack type or normal**
43. **difficulty – Detection difficulty score**



#### **Attack Categories:**



##### **Category                                Sample Attacks**                                                  

#####  	                                                                                                                                                                                          

#####  DOS	                  neptune, smurf, pod, back, teardrop                                              

#####  Probe	                  satan, ipsweep, nmap, portsweep                                                 

#####  R2L	                  ftp\_write, guess\_passwd, imap, phf, spy, multihop, warezclient, warezmaster     

#####  U2R	                  buffer\_overflow, loadmodule, perl, rootkit                                      

#####  Normal	                  normal                                                                          

&nbsp;









#### **Distribution:**



* **normal**: 67,343
* **dos**: 45,927
* **probe**: 11,656
* **r2l**: 995
* **u2r**: 52





#### **Dataset Stats:**



* **Shape**: (125973, 44) (features + label + attack category)
* **Numeric stats:** Mean, Std, Min, Max, Quartiles available for numeric features
* **No missing values** in the dataset





#### **Visualizations:**



* Bar chart of attack categories: shows count per category
* Grouped counts by **attack\_category** and **label**



#### **Notes:**



* Dataset has mixed numeric and categorical features
* Used for training ML models for network intrusion detection
