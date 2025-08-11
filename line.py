import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\CHRISTOPHER A\OneDrive\Desktop\Data Analytics\MD Python\manufacturin_G_dataset.csv"
df = pd.read_csv(file_path)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df = df.sort_values('Timestamp')

df_sample = df.iloc[::100, :]

plt.figure(figsize=(10, 5))
sns.lineplot(data=df_sample, x='Timestamp', y='Production_Speed_units_per_hr', color='green')
plt.title('Production Speed Over Time (Sampled)')
plt.xlabel('Time')
plt.ylabel('Units per Hour')
plt.tight_layout()
plt.show()
