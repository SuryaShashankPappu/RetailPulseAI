from pathlib import Path
import pandas as pd

DATA_FILE = Path("data/raw/sales/online_retail_II.csv")

df = pd.read_csv(DATA_FILE)

print("\nUnique Countries")
print(df["Country"].nunique())

print("\nUnique Products")
print(df["StockCode"].nunique())

print("\nUnique Customers")
print(df["Customer ID"].nunique())

print("\nUnique Invoices")
print(df["Invoice"].nunique())