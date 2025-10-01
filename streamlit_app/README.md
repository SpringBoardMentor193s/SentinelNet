# SentinelNet Streamlit Application

## 🚀 Quick Start

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   streamlit run Home.py
   ```

3. **Access the App:**
   - Open your browser to `http://localhost:8501`

## 📁 Project Structure

```
SentinelNet/
├── notebooks/
│   └── models/           # Pre-trained models
│       ├── Decision_Tree.pkl
│       ├── Decision_Tree_Multiclass.pkl
│       ├── Decision_Tree_CIC_IDS.pkl
│       ├── Logistic_Regression.pkl
│       ├── Logistic_Regression_Multiclass.pkl
│       ├── Logistic_Regression_CIC_IDS.pkl
│       ├── Random_Forest.pkl
│       ├── Random_Forest_Multiclass.pkl
│       └── Random_Forest_CIC_IDS.pkl
└── streamlit_app/
    ├── Home.py           # Main entry point
    ├── pages/            # Application pages
    │   ├── Classification_Type.py
    │   ├── Model_Selection.py
    │   ├── File_Upload.py
    │   ├── Prediction.py
    │   └── Results.py
    └── requirements.txt
```

## 🔧 Troubleshooting

### Model Loading Issues

If you get "Model file not found" errors:

1. **Check Model Path:** The app looks for models in `E:\SentinelNet\notebooks\models\`
2. **Verify Models Exist:** Run the test script:
   ```bash
   test_model_paths.bat
   ```
3. **Check Debug Info:** In the app, expand "🔍 Debug Information" to see path details

### Common Issues

1. **File Not Found:** Ensure models are in the correct directory
2. **Permission Errors:** Run as administrator if needed
3. **Python Path Issues:** Make sure you're running from the correct directory

## 📊 Model Mapping

The app automatically selects the correct model based on your choices:

| Dataset | Classification | Model | File Name |
|---------|---------------|--------|-----------|
| NSL-KDD | Binary | Any | `ModelName.pkl` |
| NSL-KDD | Multiclass | Any | `ModelName_Multiclass.pkl` |
| CIC-IDS | Binary | Any | `ModelName_CIC_IDS.pkl` |

## 🎯 Usage Flow

1. **Select Dataset** (NSL-KDD or CIC-IDS)
2. **Choose Classification Type** (Binary/Multiclass for NSL-KDD)
3. **Select Model** (Logistic Regression, Decision Tree, Random Forest)
4. **Upload CSV File** (Drag & drop or browse)
5. **Run Prediction** (Automatic preprocessing and prediction)
6. **View Results** (Detailed analysis and visualizations)

## 📝 Data Requirements

### NSL-KDD Dataset
- **Format:** CSV file
- **Features:** 41 columns
- **Required columns:** All standard NSL-KDD features

### CIC-IDS Dataset  
- **Format:** CSV file
- **Features:** 78 columns
- **Required columns:** All standard CIC-IDS features

## 🆘 Support

If you encounter issues:
1. Check the debug information in the app
2. Verify your data format matches requirements
3. Ensure all dependencies are installed
4. Check that model files exist and are accessible
