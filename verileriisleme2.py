import pandas as pd
df = pd.read_csv("fethiye.txt", header = None)
df.head()
df = pd.melt(df)
df.head()
df["value"] = pd.to_numeric(df.value, errors='coerce').fillna(0).astype(int)
import statistics
print(statistics.median(df["value"]))
import seaborn as sns
import matplotlib.pyplot as plt

ax = sns.boxplot(y="value", data=df)
ax.set(xlim=(0, 100))
plt.show()


