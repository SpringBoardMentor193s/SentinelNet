import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

class DataPreprocessor:
    def __init__(self, dataset_type='nsl_kdd'):
        self.dataset_type = dataset_type
        self.scaler = StandardScaler()
        self.feature_names = None
        self.categorical_columns = ['protocol_type', 'service', 'flag']
        self.categorical_mappings = {}

    def preprocess_nsl_kdd(self, df, is_training=True):
        df = df.copy()
        nsl_cols = [
            'duration','protocol_type','service','flag','src_bytes','dst_bytes',
            'land','wrong_fragment','urgent','hot','num_failed_logins','logged_in',
            'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
            'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login',
            'count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate',
            'same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count',
            'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
            'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
            'dst_host_rerror_rate','dst_host_srv_rerror_rate'
        ]

        # Remove unwanted columns
        cols_to_remove = ['attack_binary', 'attack_category', 'Unnamed: 0']
        for col in cols_to_remove:
            if col in df.columns:
                df = df.drop(col, axis=1)

        # Check if we need to assign column names
        required_cols_present = all(col in df.columns for col in self.categorical_columns)

        if not required_cols_present:
            if df.shape[1] in [41, 42, 43]:
                num_cols = df.shape[1]
                if num_cols == 41: 
                    df.columns = nsl_cols
                elif num_cols == 42: 
                    df.columns = nsl_cols + ['label']
                elif num_cols == 43: 
                    df.columns = nsl_cols + ['label', 'difficulty']
        else:
            df.columns = df.columns.str.strip()

        # Extract label if present
        y = None
        for col in ['label', 'class', 'Label']:
            if col in df.columns:
                y = df[col]
                cols_to_drop = [c for c in ['label', 'class', 'Label', 'difficulty'] if c in df.columns]
                X = df.drop(columns=cols_to_drop)
                break
        else:
            X = df.copy()
            if 'difficulty' in X.columns:
                X = X.drop('difficulty', axis=1)

        # Clean data
        X = X.replace([np.inf, -np.inf], np.nan)
        
        # Ensure categorical columns are strings
        for col in self.categorical_columns:
            if col in X.columns:
                X[col] = X[col].astype(str).str.strip()

        if is_training:
            # Store categorical mappings during training
            for col in self.categorical_columns:
                if col in X.columns:
                    self.categorical_mappings[col] = sorted(X[col].unique().tolist())
            
            # One-hot encode
            X_encoded = pd.get_dummies(X, columns=self.categorical_columns, drop_first=False)
            X_encoded = X_encoded.fillna(0)
            
            # Store feature names
            self.feature_names = X_encoded.columns.tolist()
            
            # Scale
            X_scaled = self.scaler.fit_transform(X_encoded)
        else:
            # Prediction mode - match training encoding exactly
            non_cat_cols = [col for col in X.columns if col not in self.categorical_columns]
            X_non_cat = X[non_cat_cols].copy()
            X_non_cat = X_non_cat.fillna(0)
            
            # Build dummy columns to match training
            dummy_dfs = [X_non_cat]
            
            for col in self.categorical_columns:
                if col in X.columns:
                    training_categories = self.categorical_mappings.get(col, [])
                    col_dummies = pd.DataFrame(index=X.index)
                    
                    for category in training_categories:
                        dummy_col_name = f"{col}_{category}"
                        col_dummies[dummy_col_name] = (X[col] == category).astype(int)
                    
                    dummy_dfs.append(col_dummies)
            
            X_encoded = pd.concat(dummy_dfs, axis=1)
            
            # Ensure all training features exist
            for feature in self.feature_names:
                if feature not in X_encoded.columns:
                    X_encoded[feature] = 0
            
            # Reorder to match training
            X_encoded = X_encoded[self.feature_names]
            
            # Scale
            X_scaled = self.scaler.transform(X_encoded)

        X_scaled_df = pd.DataFrame(X_scaled, columns=self.feature_names, index=X.index)
        return X_scaled_df, y

    def preprocess_cicids(self, df, is_training=True):
        df = df.copy()
        df.columns = df.columns.str.strip()

        # Extract label
        y = None
        for col in ['Label', 'label', 'class']:
            if col in df.columns:
                y = df[col]
                X = df.drop(columns=[col])
                break
        else: 
            X = df.copy()

        # Clean data
        X = X.replace([np.inf, -np.inf], np.nan)
        X = X.select_dtypes(include=np.number)
        
        if len(X.columns) > 0:
            X = X.fillna(X.median())
        X = X.fillna(0)

        if is_training:
            # Initialize empty categorical_mappings for CICIDS
            self.categorical_mappings = {}
            
            # Remove zero variance columns
            X = X.loc[:, X.var() > 0]
            self.feature_names = X.columns.tolist()
            X_scaled = self.scaler.fit_transform(X)
        else:
            # Add missing columns
            for c in self.feature_names:
                if c not in X.columns:
                    X[c] = 0
            
            # Reorder and select only training features
            X = X[self.feature_names]
            X_scaled = self.scaler.transform(X)

        X_scaled_df = pd.DataFrame(X_scaled, columns=self.feature_names, index=X.index)
        return X_scaled_df, y

    def preprocess(self, df, is_training=True):
        if 'nsl' in self.dataset_type.lower():
            return self.preprocess_nsl_kdd(df, is_training)
        elif 'cic' in self.dataset_type.lower():
            return self.preprocess_cicids(df, is_training)
        else:
            raise ValueError(f"Unknown dataset type: {self.dataset_type}")

    def save_preprocessor(self, path):
        joblib.dump({
            'scaler': self.scaler,
            'feature_names': self.feature_names,
            'categorical_columns': self.categorical_columns,
            'categorical_mappings': self.categorical_mappings,
            'dataset_type': self.dataset_type
        }, path)

    def load_preprocessor(self, path):
        data = joblib.load(path)
        self.scaler = data.get('scaler')
        self.feature_names = data.get('feature_names')
        self.categorical_columns = data.get('categorical_columns', ['protocol_type', 'service', 'flag'])
        self.categorical_mappings = data.get('categorical_mappings', {})
        self.dataset_type = data.get('dataset_type')
        return self

def get_attack_category(label, dataset_type='nsl_kdd'):
    if dataset_type == 'nsl_kdd':
        dos = ['neptune', 'smurf', 'pod', 'teardrop', 'land', 'back', 'apache2', 'mailbomb', 'processtable', 'udpstorm']
        probe = ['portsweep', 'ipsweep', 'nmap', 'satan', 'saint', 'mscan']
        r2l = ['ftp_write', 'guess_passwd', 'imap', 'multihop', 'phf', 'spy', 'warezclient', 'warezmaster', 'xlock', 'xsnoop', 'snmpguess', 'snmpgetattack', 'httptunnel', 'sendmail', 'named']
        u2r = ['buffer_overflow', 'loadmodule', 'perl', 'rootkit', 'ps', 'sqlattack', 'xterm']

        if isinstance(label, str):
            l = label.lower().strip()
            if 'normal' in l: 
                return 'Normal'
            elif any(a in l for a in dos): 
                return 'DoS'
            elif any(a in l for a in probe): 
                return 'Probe'
            elif any(a in l for a in r2l): 
                return 'R2L'
            elif any(a in l for a in u2r): 
                return 'U2R'
            else: 
                return 'Attack'
        else:
            mapping = {0: 'Normal', 1: 'DoS', 2: 'Probe', 3: 'R2L', 4: 'U2R'}
            return mapping.get(label, 'Attack')
    elif dataset_type == 'cicids':
        if isinstance(label, str):
            l = label.lower().strip()
            if 'benign' in l or 'normal' in l: 
                return 'Benign'
            else: 
                return 'Attack'
        else:
            return 'Benign' if label == 0 else 'Attack'
    return str(label)