import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\CHRISTOPHER A\OneDrive\Desktop\Data Analytics\MD Python\manufacturin_G_dataset.csv"
df = pd.read_csv(file_path)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df = df.sort_values('Timestamp')

df_sample = df.iloc[::100, :]

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Temperature_C', y='Quality Control_Defect_Rate_%', hue='Machine_ID')
plt.title('Temperature vs Defect Rate')
plt.tight_layout()
plt.show()
