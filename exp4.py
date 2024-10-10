import pandas as pd

data = pd.read_csv("/home/Devanshsrv/Coding/Year 2/AIML/experiments/clean_data.csv")

print(f"Number of rows: {data.shape[0]}")
print(f"Number of columns: {data.shape[1]}")
print(f"First 5 rows:\n{data.head()}")
print(f"Size of dataset: {data.size}")

print()
print(f"Number of missing values:\n{data.isnull().sum()}")

print()
print(f"Sum of numeric columns:\n{data.sum(numeric_only=True)}")

print()
print(f"Average of numeric columns:\n{data.mean(numeric_only=True)}")

print()
print(f"Minimum of numeric columns:\n{data.min(numeric_only=True)}")

print()
print(f"Maximum of numeric columns:\n{data.max(numeric_only=True)}")
