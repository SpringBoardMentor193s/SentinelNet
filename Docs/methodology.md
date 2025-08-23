# 🛠️ Methodology - SentinelNet

---

## 🔄 Workflow
1. **Data Collection**  
   Load NSL-KDD dataset for training and testing.

2. **Data Preprocessing**  
   - Handle missing values  
   - Encode categorical features (e.g., protocol type)  
   - Normalize numerical features  

3. **Feature Engineering**  
   Select important features to reduce dimensionality and improve model performance.

4. **Model Training**  
   Train multiple machine learning models:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - Support Vector Machine (SVM)

5. **Model Evaluation**  
   Evaluate using metrics:
   - Accuracy
   - Precision
   - Recall
   - F1-Score
   - Confusion Matrix

6. **Deployment (Future Work)**  
   - Real-time traffic capture using `scapy`
   - Flask/Django API for prediction
   - Web dashboard for monitoring

---

## 📈 Tools & Libraries
- **Python**: Data analysis & ML
- **Pandas, NumPy**: Data processing
- **Matplotlib, Seaborn**: Visualization
- **Scikit-learn**: Machine learning

