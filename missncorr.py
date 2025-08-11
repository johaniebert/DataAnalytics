import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
sns.set(style="whitegrid")

file_path = r"D:\Projects\DataAnalytics\MD Python\manufacturin_G_dataset.csv"
df = pd.read_csv(file_path)

print("\n Missing Values:")
print(df.isnull().sum())

print("\n Correlation Matrix:")
print(df.corr(numeric_only=True))