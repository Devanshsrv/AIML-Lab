import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

df = pd.read_csv("/home/Devanshsrv/Coding/Year 2/AIML/experiments/bigmac.csv")

modified_data = df.copy()

random_indices = [
    random.randint(0, modified_data.shape[0])
    for _ in range(0, modified_data.shape[0] // 2)
    if random.randint(0, 1) == 0
]

for i in random_indices:
    modified_data.loc[i, "dollar_price"] = np.nan

random_indices = [
    random.randint(0, modified_data.shape[0])
    for _ in range(0, modified_data.shape[0] // 2)
    if random.randint(0, 1) == 0
]

for i in random_indices:
    modified_data.loc[i, "local_price"] = np.nan


modified_data["local_price"] = modified_data["local_price"].fillna(
    modified_data["local_price"].median()
)

modified_data["dollar_price"] = modified_data["dollar_price"].fillna(
    modified_data["dollar_price"].median()
)

q1 = modified_data[["local_price", "dollar_price"]].quantile(0.25)
q3 = modified_data[["local_price", "dollar_price"]].quantile(0.75)

iqr = q3 - q1

outliers = (modified_data[["local_price", "dollar_price"]] < (q1 - 1.5 * iqr)) | (
    modified_data[["local_price", "dollar_price"]] < (q3 - 1.5 * iqr)
)

capped_data = modified_data.copy()
for col in ["local_price", "dollar_price"]:
    lower_bound = q1[col] - 1.5 * iqr[col]
    upper_bound = q3[col] + 1.5 * iqr[col]

    capped_data[col] = np.where(
        capped_data[col] < lower_bound, lower_bound, capped_data[col]
    )

    capped_data[col] = np.where(
        capped_data[col] > upper_bound, upper_bound, capped_data[col]
    )

missing_changes = modified_data.compare(df)

outlier_changes = capped_data.compare(df)

print("Changes after handling missing values:")
print(missing_changes)

print("Changes after handling outliers:")
print(outlier_changes)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.boxplot(modified_data[["local_price", "dollar_price"]])
plt.title("Before outlier handling")

plt.subplot(1, 2, 2)
plt.boxplot(capped_data[["local_price", "dollar_price"]])
plt.title("After outlier handling")

plt.tight_layout()
plt.show()