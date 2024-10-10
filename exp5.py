import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("/home/Devanshsrv/Coding/Year 2/AIML/experiments/bigmac.csv")


df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["local_price"], label="Local Price", color="blue")
plt.plot(df["date"], df["dollar_price"], label="Dollar Price", color="green")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Local Price vs Dollar Price Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
correlation = df[["local_price", "dollar_ex", "dollar_price"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap")
plt.show()