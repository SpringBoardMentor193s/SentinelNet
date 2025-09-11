import os
import sys
import textwrap
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api import types as pdtypes


# Constants: expected NSL columns

NSL_COLUMNS = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot',
    'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations',
    'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count',
    'serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
    'srv_diff_host_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
    'dst_host_rerror_rate','dst_host_srv_rerror_rate','outcome','level'
]

# A reasonably comprehensive mapping from NSL-KDD attack names -> category
# NOTE: add/remove elements depending on your actual 'outcome' labels

ATTACK_TO_CATEGORY = {
    # DoS
    'neptune':'DoS', 'smurf':'DoS', 'back':'DoS', 'teardrop':'DoS', 'pod':'DoS', 'land':'DoS',
    # Probe
    'satan':'Probe','ipsweep':'Probe','nmap':'Probe','portsweep':'Probe','mscan':'Probe',
    # R2L
    'guess_passwd':'R2L','ftp_write':'R2L','imap':'R2L','phf':'R2L','spy':'R2L','warezclient':'R2L','warezmaster':'R2L',
    # U2R
    'buffer_overflow':'U2R','loadmodule':'U2R','rootkit':'U2R','perl':'U2R','xterm':'U2R',
    # Normal
    'normal':'Normal'
}


# Loading helpers


def load_csv_with_validation(path, expected_columns=None, **kwargs):
    """Load CSV and optionally set column names. If column-count mismatch occurs, warn and keep raw columns.
    Returns DataFrame and a boolean whether columns were set.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path, header=None, **kwargs)
    if expected_columns is not None:
        if df.shape[1] == len(expected_columns):
            df.columns = expected_columns
            return df, True
        else:
            print(f"[warning] expected {len(expected_columns)} columns but file has {df.shape[1]} columns.\n"
                  " -> Skipping automatic renaming. Inspect file or provide correct column list.")
            return df, False
    return df, False


def load_parquet(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    df = pd.read_parquet(path)
    return df


# Analysis / plotting helpers

def top_value_counts(series, top=10):
    vc = series.value_counts().head(top)
    return vc


def plot_bar_counts(series, top=20, title=None, figsize=(10,6), rotate=45, horizontal=False, save_path=None):
    vc = series.value_counts().head(top)
    plt.figure(figsize=figsize)
    if horizontal:
        vc.sort_values().plot(kind='barh')
        plt.xlabel('Count')
    else:
        vc.plot(kind='bar')
        plt.ylabel('Count')

    if title:
        plt.title(title)
    plt.xticks(rotation=rotate)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()


def print_dataset_overview(df, name):
    print(f"--- {name} overview ---")
    print(f"Shape: {df.shape}")
    print(df.head())
    print('\nDtypes:')
    print(df.dtypes)
    print('\nNumeric summary:')
    print(df.select_dtypes(include=[np.number]).describe().T)
    print('\nNulls per column:')
    print(df.isnull().sum().sort_values(ascending=False).head(20))



# Schema generation

def create_schema(df, dataset_name, categorical_features=None):
    """Return a pandas DataFrame describing features: name, type (numerical/categorical/binary), suggested preprocessing, semantic category.

    Pass `categorical_features` detected for this dataset (list of column names). If omitted we auto-detect object columns.
    """
    if categorical_features is None:
        categorical_features = df.select_dtypes(include=['object', 'category']).columns.tolist()

    schema = []
    for col in df.columns:
        val = df[col]
        # Determine type robustly
        if col in categorical_features:
            ftype = 'categorical'
            action = 'encode (one-hot/label/target)'
        elif pdtypes.is_integer_dtype(val.dtype) or pdtypes.is_float_dtype(val.dtype):
            unique_vals = val.unique()
            # treat binary-like columns
            if pd.Series(unique_vals).dropna().shape[0] <= 2:
                ftype = 'binary'
                action = 'keep / map to {0,1}'
            else:
                ftype = 'numerical'
                action = 'scale/normalize'
        else:
            ftype = 'other'
            action = 'inspect'

        # semantic guess
        col_lower = col.lower()
        if 'bytes' in col_lower or 'count' in col_lower or 'rate' in col_lower or 'pkt' in col_lower:
            semantic = 'traffic'
        elif 'login' in col_lower or 'root' in col_lower or 'shell' in col_lower or 'priv' in col_lower:
            semantic = 'privilege'
        elif 'flag' in col_lower or 'protocol' in col_lower or 'service' in col_lower:
            semantic = 'behavior'
        elif col_lower in ['outcome', 'label', 'category']:
            semantic = 'target'
        else:
            semantic = 'other'

        schema.append([col, ftype, action, semantic])

    schema_df = pd.DataFrame(schema, columns=['Feature','Type','Suggested Preprocessing','Semantic'])
    print(f"Schema for {dataset_name} (first 20 rows):")
    print(schema_df.head(20))
    return schema_df


# Utilities and suggestions


def map_attacks_to_category(series, mapping=ATTACK_TO_CATEGORY, default='Other'):
    return series.map(lambda x: mapping.get(str(x).lower(), default))


def get_class_imbalance(df, target_col):
    vc = df[target_col].value_counts()
    pct = (vc / vc.sum()) * 100
    return pd.concat([vc, pct.round(2)], axis=1, keys=['count','percent'])


# Example main pipeline

def run_analysis(nsl_path: str, cicids_path: str, output_dir: str = './analysis_output'):
    os.makedirs(output_dir, exist_ok=True)

    # 1) Load NSL-KDD with validation
    print('\nLoading NSL-KDD...')
    try:
        nsl_df, renamed = load_csv_with_validation(nsl_path, expected_columns=NSL_COLUMNS)
    except Exception as e:
        print('Failed to load NSL-KDD:', e)
        return

    # If the user file didn't match expected number of cols, we attempt a second strategy
    
  if not renamed:
        print('[tip] You can pass a corrected column list or inspect the first few rows manually.')

    # Quick checks
    print_dataset_overview(nsl_df, 'NSL-KDD')

    # Map categories
    if 'outcome' in nsl_df.columns:
        nsl_df['category'] = map_attacks_to_category(nsl_df['outcome'])
        print('\nTop attack outcomes:')
        print(nsl_df['outcome'].value_counts().head(10))
        print('\nCategory distribution:')
        print(get_class_imbalance(nsl_df, 'category'))

        plot_bar_counts(nsl_df['category'], top=10, title='NSL-KDD: Attack categories', horizontal=False,
                        save_path=os.path.join(output_dir, 'nsl_categories.png'))

    # Schema and save
    cat_feats_nsl = nsl_df.select_dtypes(include=['object', 'category']).columns.tolist()
    schema_nsl = create_schema(nsl_df, 'NSL-KDD', categorical_features=cat_feats_nsl)
    schema_nsl.to_csv(os.path.join(output_dir, 'schema_nsl.csv'), index=False)
    with open(os.path.join(output_dir, 'schema_nsl.md'), 'w') as f:
        f.write(schema_nsl.to_markdown(index=False))

    # 2) Load CICIDS (parquet)
    print('\nLoading CICIDS2017 (parquet)...')
    try:
        cicids_df = load_parquet(cicids_path)
    except Exception as e:
        print('Failed to load CICIDS:', e)
        return

    print_dataset_overview(cicids_df, 'CICIDS2017')

    if 'Label' in cicids_df.columns:
        cicids_df['category'] = cicids_df['Label'].map(lambda x: str(x).strip())
        print('\nLabel counts:')
        print(cicids_df['Label'].value_counts().head(10))
        plot_bar_counts(cicids_df['Label'], top=15, title='CICIDS2017: Label distribution',
                        save_path=os.path.join(output_dir, 'cicids_labels.png'))

    # Schema and save for cicids
    cat_feats_cicids = cicids_df.select_dtypes(include=['object', 'category']).columns.tolist()
    schema_cicids = create_schema(cicids_df, 'CICIDS2017', categorical_features=cat_feats_cicids)
    schema_cicids.to_csv(os.path.join(output_dir, 'schema_cicids.csv'), index=False)
    with open(os.path.join(output_dir, 'schema_cicids.md'), 'w') as f:
        f.write(schema_cicids.to_markdown(index=False))

    # 3) Some additional analytical tips printed
    print('\n=== Recommendations & next steps ===')
    print(textwrap.dedent('''
        1. Handle class imbalance: consider stratified sampling, SMOTE/ADASYN for minority classes, or class-weighted models.
        2. Encode categorical features: protocol_type, service, flag. For high-cardinality fields like 'service', consider target encoding
           or frequency encoding rather than naive one-hot.
        3. Feature selection: compute correlation of numeric features with the target (if supervised) and remove near-zero-variance
           columns (num_outbound_cmds is often zero in NSL-KDD).
        4. Pipeline: build sklearn Pipeline with preprocessing (imputer -> encoder -> scaler) -> classifier (RandomForest/XGBoost).
        5. Evaluation: use precision/recall/F1 and confusion matrices, not only accuracy (due to heavy imbalance).
        6. Reproducibility: set random_state and save intermediate artifacts (schemas, label maps, encoders) to disk.
    ''').strip())

    print('\nAnalysis outputs saved to:', os.path.abspath(output_dir))



# If executed as script

if __name__ == '__main__':
    # default paths (edit these to your local files)
    DATA_PATHS = {
        'nsl_csv': './data/KDDTrain+.txt',
        'cicids_parquet': './data/DoS-Wednesday-no-metadata.parquet'
    }

    # Allow overriding via CLI arguments: nsl_path cicids_path
    if len(sys.argv) >= 3:
        DATA_PATHS['nsl_csv'] = sys.argv[1]
        DATA_PATHS['cicids_parquet'] = sys.argv[2]

    run_analysis(DATA_PATHS['nsl_csv'], DATA_PATHS['cicids_parquet'])
