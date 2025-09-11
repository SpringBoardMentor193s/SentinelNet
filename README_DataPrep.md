# SentinelNet ‒ Data Preparation & Datasets

This section describes how data is organized, preprocessed, and prepared for modeling.

---

## Datasets Description

- The `Datasets/` directory contains raw (or preprocessed) data used for training/testing.  
- `Data sets.md` and `Network Intrusion Detection Dataset.md` provide descriptions of the data fields, sources, and any preprocessing steps already done.

---

## Data Preprocessing Steps

Typical steps to prepare the data include:

1. **Loading data**  
   - Use file formats as provided (CSV, etc.).  
   - Merge / drop irrelevant columns if needed.

2. **Cleaning and Imputation**  
   - Handle missing values.  
   - Remove duplicates or corrupt rows if present.

3. **Feature Engineering**  
   - Converting categorical features (if any) into numeric (one‑hot, label encoding).  
   - Creation of derived features (if relevant e.g. time-based, traffic ratios).

4. **Normalization / Scaling**  
   - To ensure features are on similar scale for ML models.

5. **Train/Test Split**  
   - Partition dataset into training and testing (or more splits).  
   - Stratification if class imbalance is severe.

6. **Handling Imbalanced Classes** (if applicable)  
   - Oversampling / undersampling / synthetic methods (e.g. SMOTE).

---

## Dataset File References

- `Data sets.md` — describes all datasets used, columns, and metadata.  
- `Network Intrusion Detection Dataset.md` — detailed dataset specific to intrusion detection.

---

## How to Use the Datasets

- Place or ensure all dataset files are inside `Datasets/`.  
- Update any paths in scripts (in `Scripts/`) or in `main.py` to point to the correct dataset files.  
- Run preprocessing / cleaning scripts from `Scripts/` before model training.
