import gdown
import zipfile
import os

# Replace with your actual file ID
file_id = "1D-doLN918vJU2RrP6G1LCAEdHEdptWdl"
url = f"https://drive.google.com/uc?id={file_id}"
output = "data/CICIDS2017.zip"

os.makedirs("data", exist_ok=True)

print("⬇  Downloading CICIDS2017 dataset...")
gdown.download(url=url, output=output, quiet=False, fuzzy=True)

print("🗜 Extracting dataset...")
with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall("data/CICIDS2017")

print("✅ Done! Dataset available at data/CICIDS2017/")
