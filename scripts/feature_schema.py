import pandas as pd
import os
from scipy.io import arff

# Load ARFF file
arff_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'NSL-KDD', 'KDDTest+.arff'))
with open(arff_path, 'r', encoding='utf-8', errors='replace') as f:
    data, meta = arff.loadarff(f)
df = pd.DataFrame(data)

# Identify categorical, numerical, and binary features
categorical = []
numerical = []
binary = []
for col in df.columns:
    if meta[col][0] == 'nominal':
        # Check for binary
        if len(meta[col][1]) == 2:
            binary.append(col)
        else:
            categorical.append(col)
    elif meta[col][0] == 'numeric' or meta[col][0] == 'real':
        numerical.append(col)
    else:
        categorical.append(col)

print('Categorical features:', categorical)
print('Numerical features:', numerical)
print('Binary features:', binary)

# Check for missing values and duplicates
print('Missing values per column:')
print(df.isnull().sum())
print('Number of duplicate rows:', df.duplicated().sum())

# Create schema mapping table
schema = []
for col in df.columns:
    if col in binary:
        ftype = 'binary'
        action = 'Label encode'
    elif col in categorical:
        ftype = 'categorical'
        action = 'One-hot encode'
    elif col in numerical:
        ftype = 'numerical'
        action = 'Scale/normalize'
    else:
        ftype = 'unknown'
        action = 'Review'
    schema.append({'Feature': col, 'Type': ftype, 'Preprocessing': action})

schema_df = pd.DataFrame(schema)
print('\nSchema Mapping Table:')
print(schema_df)
