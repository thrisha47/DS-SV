import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
np.random.seed(42)
n = 500
df = pd.DataFrame({
    "Customer_ID": range(1, n + 1),
    "Group": np.random.choice(["Old Website", "New Website"], n),
    "Region": np.random.choice(["North", "South", "East", "West"], n),
    "Sales": np.random.normal(5000, 1000, n)
})
df.loc[df["Group"] == "New Website", "Sales"] += 400
print("Dataset Preview:")
print(df.head())
print("\nBUSINESS STORY")
avg_sales_old = df[df["Group"] == "Old Website"]["Sales"].mean()
avg_sales_new = df[df["Group"] == "New Website"]["Sales"].mean()
print(f"Average Sales (Old Website): {avg_sales_old:.2f}")
print(f"Average Sales (New Website): {avg_sales_new:.2f}")
if avg_sales_new > avg_sales_old:
    print("\nInsight:")
    print("The New Website is generating higher average sales than the Old Website.")
else:
    print("\nInsight:")
    print("The Old Website is generating higher average sales.")
sales_by_group = df.groupby("Group")["Sales"].mean()
plt.figure(figsize=(8, 5))
sales_by_group.plot(kind="bar")
plt.title("Average Sales by Website Version")