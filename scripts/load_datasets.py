import pandas as pd
import matplotlib.pyplot as plt
import os

from scipy.io import arff

# Load NSL-KDD ARFF dataset with error handling
arff_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'NSL-KDD', 'KDDTest+.arff'))
print(f"Looking for ARFF file at: {arff_path}")
try:
    with open(arff_path, 'r', encoding='utf-8', errors='replace') as f:
        data, meta = arff.loadarff(f)
    nsl_df = pd.DataFrame(data)
except Exception as e:
    print(f"Error loading ARFF file: {e}")
    nsl_df = None

# Print summary statistics
print('Number of rows:', len(nsl_df))
if 'label' in nsl_df.columns:
    print('Unique labels:', nsl_df['label'].nunique())
    print('Top 5 frequent attack types:')
    print(nsl_df['label'].value_counts().head(5))
    # Bar chart of attack type distribution
    nsl_df['label'].value_counts().plot(kind='bar', figsize=(10,4))
    plt.title('NSL-KDD Attack Type Distribution')
    plt.xlabel('Attack Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
else:
    print('"label" column not found in ARFF file.')

# Basic inspection
print(nsl_df.head())
print(nsl_df.info())
print(nsl_df.describe())

# # Load CICIDS2017 dataset (example path, update as needed)
# cic_path = os.path.join('..', 'data', 'CICIDS2017', 'Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')
# cic_df = pd.read_csv(cic_path)
# print('CICIDS2017 columns:', cic_df.columns.tolist())
# print('CICIDS2017 shape:', cic_df.shape)
