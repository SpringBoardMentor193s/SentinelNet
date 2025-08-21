import pandas as pd

columns = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot',
    'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations',
    'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count',
    'serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
    'srv_diff_host_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
    'dst_host_rerror_rate','dst_host_srv_rerror_rate','outcome','level'
]
#load the dataset
data = pd.read_csv('../data/KDDTrain+.csv', names=columns)

#Identify types
categorical = ['protocol_type', 'service', 'flag']
binary = ['land', 'logged_in', 'is_host_login', 'is_guest_login', 'root_shell', 'su_attempted']
numerical = [col for col in columns if col not in (categorical + binary + ['label'])]

print("Categorical features:", categorical)
print("Binary features:", binary)
print("Numerical features:", numerical)

#Check for missing values and duplicates
print("\nMissing values per column:\n", data.isnull().sum())
print("\nNumber of duplicate rows:", data.duplicated().sum())

#Schema mapping table
schema_map = {
    "duration":          ("numerical", "Scale/Normalize", "traffic"),
    "protocol_type":     ("categorical", "Label Encoding", "traffic"),
    "service":           ("categorical", "Label Encoding", "traffic"),
    "flag":              ("categorical", "Label Encoding", "traffic"),
    "src_bytes":         ("numerical", "Scale/Normalize", "traffic"),
    "dst_bytes":         ("numerical", "Scale/Normalize", "traffic"),
    "land":              ("binary", "None/As-is", "behavior"),
    "wrong_fragment":    ("numerical", "None/Scale", "traffic"),
    "urgent":            ("numerical", "None/Scale", "traffic"),
    "hot":               ("numerical", "None/Scale", "behavior"),
    "num_failed_logins": ("numerical", "None/Scale", "behavior"),
    "logged_in":         ("binary", "None/As-is", "privilege"),
    "num_compromised":   ("numerical", "None/Scale", "privilege"),
    "root_shell":        ("binary", "None/As-is", "privilege"),
    "su_attempted":      ("binary", "None/As-is", "privilege"),
    "num_root":          ("numerical", "None/Scale", "privilege"),
    "num_file_creations":("numerical", "None/Scale", "behavior"),
    "num_shells":        ("numerical", "None/Scale", "privilege"),
    "num_access_files":  ("numerical", "None/Scale", "behavior"),
    "num_outbound_cmds": ("numerical", "None/Scale", "traffic"),
    "is_host_login":     ("binary", "None/As-is", "privilege"),
    "is_guest_login":    ("binary", "None/As-is", "privilege"),
    "count":             ("numerical", "Scale/Normalize", "traffic"),
    "srv_count":         ("numerical", "Scale/Normalize", "traffic"),
    "serror_rate":       ("numerical", "Scale/Normalize", "traffic"),
    "srv_serror_rate":   ("numerical", "Scale/Normalize", "traffic"),
    "rerror_rate":       ("numerical", "Scale/Normalize", "traffic"),
    "srv_rerror_rate":   ("numerical", "Scale/Normalize", "traffic"),
    "same_srv_rate":     ("numerical", "Scale/Normalize", "traffic"),
    "diff_srv_rate":     ("numerical", "Scale/Normalize", "traffic"),
    "srv_diff_host_rate":("numerical", "Scale/Normalize", "traffic"),
    "dst_host_count":    ("numerical", "Scale/Normalize", "traffic"),
    "dst_host_srv_count":("numerical", "Scale/Normalize", "traffic"),
    "dst_host_same_srv_rate":    ("numerical", "Scale/Normalize", "traffic"),
    "dst_host_diff_srv_rate":    ("numerical", "Scale/Normalize", "traffic"),
    "dst_host_same_src_port_rate":("numerical", "Scale/Normalize", "traffic"),
    "dst_host_srv_diff_host_rate":("numerical", "Scale/Normalize", "traffic"),
    "dst_host_serror_rate":      ("numerical", "Scale/Normalize", "traffic"),
    "dst_host_srv_serror_rate":  ("numerical", "Scale/Normalize", "traffic"),
    "dst_host_rerror_rate":      ("numerical", "Scale/Normalize", "traffic"),
    "dst_host_srv_rerror_rate":  ("numerical", "Scale/Normalize", "traffic"),
}

schema = []
for col in columns[:-1]:
    typ, prep, sem = schema_map.get(col, ('unknown', 'unknown', 'unknown'))
    schema.append([col, typ, prep, sem])
schema_df = pd.DataFrame(schema, columns=['Feature Name','Type','Suggested Preprocessing','Semantic Category'])

print("\nSchema Mapping Table:")
print(schema_df)