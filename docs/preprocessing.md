# Data Preprocessing – NSL-KDD

## Steps Taken

1. **Handling Missing Values**  
   - Checked dataset for null values.  
   - No missing values found (expected for NSL-KDD).  

2. **Removing Duplicates**  
   - Dropped duplicate rows to reduce redundancy.  

3. **Encoding Categorical Features**  
   - Columns: `protocol_type`, `service`, `flag`.  
   - Applied **One-Hot Encoding** → converted categorical values into binary indicator variables.  

4. **Scaling Numerical Features**  
   - Used **MinMaxScaler** to scale features between 0 and 1.  
   - Ensures fair contribution of all features in distance-based or gradient-based models.  

## Outcome
- Dataset is cleaned and standardized.  
- Shape reduced after duplicate removal.  
- Dataset is ready for feature selection and model training.
