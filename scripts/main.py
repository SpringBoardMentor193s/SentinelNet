import pandas as pd
import matplotlib.pyplot as plt

# Load NSL-KDD dataset (assuming CSV format)
df = pd.read_csv("C:\Users\SHREYANSHI\OneDrive\Documents\springboard\SentinelNet\datasets\KDDTest+.txt")

# Summary statistics
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Unique labels:", df['label'].unique())

# Top 5 frequent attack types
print("\nTop 5 frequent attack types:")
print(df['label'].value_counts().head(5))

