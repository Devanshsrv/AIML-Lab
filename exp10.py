# Importing necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
# Assuming the file name is 'currency_data.csv'
data = pd.read_csv("/home/Devanshsrv/Coding/Year 2/AIML/experiments/bigmac.csv")

# Display the first few rows of the data to understand its structure
print(data.head())

# 1. Line Plot: Local Price of items over Time
plt.figure(figsize=(10, 6))
for currency in data['currency_code'].unique():
    subset = data[data['currency_code'] == currency]
    plt.plot(subset['date'], subset['local_price'], marker='o', label=currency)
plt.title('Local Price Over Time by Currency', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Local Price')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# 2. Scatter Plot: Dollar Price vs Local Price
plt.figure(figsize=(10, 6))
plt.scatter(data['local_price'], data['dollar_price'], color='g', alpha=0.6)
plt.title('Scatter Plot: Local Price vs Dollar Price', fontsize=16)
plt.xlabel('Local Price')
plt.ylabel('Dollar Price')
plt.grid(True)
plt.show()

# 3. Histogram: Distribution of Dollar Prices
plt.figure(figsize=(10, 6))
plt.hist(data['dollar_price'], bins=15, color='blue', alpha=0.7)
plt.title('Histogram: Distribution of Dollar Prices', fontsize=16)
plt.xlabel('Dollar Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 4. Boxplot: Local Price across different Currencies
plt.figure(figsize=(10, 6))
sns.boxplot(x='currency_code', y='local_price', data=data)
plt.title('Boxplot: Local Prices across Currencies', fontsize=16)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 5. Heatmap: Correlation between Numeric Variables
plt.figure(figsize=(10, 6))
corr = data[['local_price', 'dollar_ex', 'dollar_price']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=1, linecolor='black')
plt.title('Heatmap: Correlation between Prices and Exchange Rate', fontsize=16)
plt.show()

# 6. Bar Plot: Mean Dollar Price per Currency
plt.figure(figsize=(10, 6))
sns.barplot(x='currency_code', y='dollar_price', data=data, estimator=sum)
plt.title('Bar Plot: Total Dollar Price by Currency', fontsize=16)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
