@echo off
echo Testing model paths...
echo.

echo Current directory:
cd
echo.

echo Checking if models directory exists:
if exist "E:\SentinelNet\notebooks\models" (
    echo ✅ Models directory found at E:\SentinelNet\notebooks\models
    echo.
    echo Files in models directory:
    dir "E:\SentinelNet\notebooks\models\*.pkl"
) else (
    echo ❌ Models directory not found at E:\SentinelNet\notebooks\models
)

echo.
echo Checking relative paths from streamlit_app:
cd /d "E:\SentinelNet\streamlit_app"
echo Current directory: %CD%

if exist "..\notebooks\models" (
    echo ✅ Relative path ..\notebooks\models exists
    echo Files:
    dir "..\notebooks\models\*.pkl"
) else (
    echo ❌ Relative path ..\notebooks\models does not exist
)

echo.
echo Testing Python model loading:
python -c "import os, joblib; print('Python test:'); print('Model exists:', os.path.exists('E:/SentinelNet/notebooks/models/Decision_Tree.pkl')); print('Directory exists:', os.path.exists('E:/SentinelNet/notebooks/models/'))"

pause
