import pandas as pd

# Load Excel file
df = pd.read_excel("data/flight_data.xlsx")

print("="*60)
print("Dataset Shape")
print(df.shape)

print("\n" + "="*60)
print("Columns")
print(df.columns.tolist())

print("\n" + "="*60)
print("First 5 Rows")
print(df.head())

print("\n" + "="*60)
print("Data Types")
print(df.dtypes)

print("\n" + "="*60)
print("Missing Values")
print(df.isnull().sum())

print("\n" + "="*60)
print("Summary Statistics")
print(df.describe(include="all"))