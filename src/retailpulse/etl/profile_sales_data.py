from pathlib import Path
import pandas as pd

# File path
DATA_FILE = Path("data/raw/sales/online_retail_II.csv")

print("=" * 60)
print("RETAILPULSE AI - SALES DATA PROFILE")
print("=" * 60)

# Read data
df = pd.read_csv(DATA_FILE)

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nFirst Five Rows")
print(df.head())

print("\nQuantity Statistics")
print(df["Quantity"].describe())

print("\nPrice Statistics")
print(df["Price"].describe())

print("\nNegative Quantity Count")
print((df["Quantity"] < 0).sum())

print("\nNegative Price Count")
print((df["Price"] < 0).sum())