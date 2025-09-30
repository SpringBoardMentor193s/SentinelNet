# utils/preprocessing.py
import joblib
import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self, dataset_type):
        """
        dataset_type: 'cicids' or 'nsl_kdd'
        """
        self.dataset_type = dataset_type
        self.scaler = None
        self.features = None

    def load_preprocessor(self, preprocessor_path):
        bundle = joblib.load(preprocessor_path)   # should contain {'scaler':..., 'features':[...]}
        self.scaler = bundle['scaler']
        self.features = bundle['features']
        return self

    def _detect_label_col(self, df):
        for cand in ['Label', 'label', 'outcome', 'Outcome']:
            if cand in df.columns:
                return cand
        return None

    def preprocess(self, df, is_training=False):
        """
        df: raw dataframe from uploaded csv
        returns: (X_processed (pd.DataFrame), y (pd.Series or None))
        """
        df = df.copy()
        # normalize column names
        df.columns = df.columns.str.strip()

        # detect & extract label if present
        y = None
        label_col = self._detect_label_col(df)
        if label_col:
            y = df[label_col].astype(str).copy()
            df = df.drop(columns=[label_col])

            # unify labels to 0/1 for binary
            if self.dataset_type == 'cicids':
                y = y.str.upper().apply(lambda x: 0 if x == 'BENIGN' else 1)
            else:  # nsl_kdd
                y = y.str.lower().apply(lambda x: 0 if x == 'normal' else 1)

        # encode object columns:
        if self.dataset_type == 'nsl_kdd':
            cats = ['protocol_type', 'service', 'flag']
            cats_present = [c for c in cats if c in df.columns]
            if cats_present:
                df = pd.get_dummies(df, columns=cats_present)
        else:
            # for CICIDS, any object strings -> get_dummies (drop_first to reduce columns)
            obj_cols = df.select_dtypes(include='object').columns.tolist()
            if obj_cols:
                df = pd.get_dummies(df, columns=obj_cols, drop_first=True)

        # clean
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.fillna(0, inplace=True)

        # ensure saved features exist: add zero columns for missing, drop extras
        for col in self.features:
            if col not in df.columns:
                df[col] = 0
        # Keep only model features and in the same order
        X = df[self.features].copy()

        # scale using saved scaler
        X_scaled = pd.DataFrame(self.scaler.transform(X.values), columns=self.features, index=X.index)

        return X_scaled, y