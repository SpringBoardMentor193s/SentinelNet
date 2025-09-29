import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

class DataPreprocessor:
    def __init__(self, dataset_type='nsl_kdd'):
        self.dataset_type = dataset_type
        self.scaler = StandardScaler()
        self.label_encoders = {}
        
    def preprocess_nsl_kdd(self, df, is_training=True):
        """Preprocess NSL-KDD dataset"""
        df = df.copy()
        
        # Define categorical columns for NSL-KDD
        categorical_cols = ['protocol_type', 'service', 'flag']
        
        # Encode categorical variables
        for col in categorical_cols:
            if col in df.columns:
                if is_training:
                    self.label_encoders[col] = LabelEncoder()
                    df[col] = self.label_encoders[col].fit_transform(df[col].astype(str))
                else:
                    if col in self.label_encoders:
                        df[col] = self.label_encoders[col].transform(df[col].astype(str))
        
        # Separate features and target if present
        if 'label' in df.columns:
            y = df['label']
            X = df.drop('label', axis=1)
        else:
            y = None
            X = df
        
        # Handle any remaining non-numeric columns
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        X = X[numeric_cols]
        
        # Scale features
        if is_training:
            X_scaled = self.scaler.fit_transform(X)
        else:
            X_scaled = self.scaler.transform(X)
        
        X_scaled = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
        
        return X_scaled, y
    
    def preprocess_cicids(self, df, is_training=True):
        """Preprocess CICIDS2017 dataset"""
        df = df.copy()
        
        # Remove any infinity values
        df = df.replace([np.inf, -np.inf], np.nan)
        
        # Fill NaN values with median
        df = df.fillna(df.median(numeric_only=True))
        
        # Separate features and target if present
        label_col = 'Label' if 'Label' in df.columns else 'label'
        if label_col in df.columns:
            y = df[label_col]
            X = df.drop(label_col, axis=1)
        else:
            y = None
            X = df
        
        # Select only numeric columns
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        X = X[numeric_cols]
        
        # Remove columns with zero variance
        if is_training:
            variance = X.var()
            cols_to_keep = variance[variance > 0].index
            X = X[cols_to_keep]
        
        # Scale features
        if is_training:
            X_scaled = self.scaler.fit_transform(X)
        else:
            X_scaled = self.scaler.transform(X)
        
        X_scaled = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
        
        return X_scaled, y
    
    def preprocess(self, df, is_training=True):
        """Main preprocessing method"""
        if self.dataset_type == 'nsl_kdd':
            return self.preprocess_nsl_kdd(df, is_training)
        elif self.dataset_type == 'cicids':
            return self.preprocess_cicids(df, is_training)
        else:
            raise ValueError(f"Unknown dataset type: {self.dataset_type}")
    
    def save_preprocessor(self, path):
        """Save preprocessor objects"""
        joblib.dump({
            'scaler': self.scaler,
            'label_encoders': self.label_encoders,
            'dataset_type': self.dataset_type
        }, path)
    
    def load_preprocessor(self, path):
        """Load preprocessor objects"""
        data = joblib.load(path)
        self.scaler = data['scaler']
        self.label_encoders = data['label_encoders']
        self.dataset_type = data['dataset_type']
        return self


def get_attack_category(label, dataset_type='nsl_kdd'):
    """Convert specific attack labels to categories"""
    if dataset_type == 'nsl_kdd':
        dos_attacks = ['neptune', 'smurf', 'pod', 'teardrop', 'land', 'back']
        probe_attacks = ['portsweep', 'ipsweep', 'nmap', 'satan']
        r2l_attacks = ['ftp_write', 'guess_passwd', 'imap', 'multihop', 
                      'phf', 'spy', 'warezclient', 'warezmaster']
        u2r_attacks = ['buffer_overflow', 'loadmodule', 'perl', 'rootkit']
        
        label_lower = str(label).lower()
        if label_lower == 'normal':
            return 'Normal'
        elif any(attack in label_lower for attack in dos_attacks):
            return 'DoS'
        elif any(attack in label_lower for attack in probe_attacks):
            return 'Probe'
        elif any(attack in label_lower for attack in r2l_attacks):
            return 'R2L'
        elif any(attack in label_lower for attack in u2r_attacks):
            return 'U2R'
        else:
            return 'Attack'
    
    elif dataset_type == 'cicids':
        label_lower = str(label).lower()
        if 'benign' in label_lower or 'normal' in label_lower:
            return 'Benign'
        else:
            return 'Attack'
    
    return label