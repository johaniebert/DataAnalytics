import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\CHRISTOPHER A\OneDrive\Desktop\Data Analytics\MD Python\manufacturin_G_dataset.csv"
df = pd.read_csv(file_path)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df = df.sort_values('Timestamp')

df_sample = df.iloc[::100, :]

plt.figure(figsize=(10, 5))
plt.fill_between(df['Timestamp'], df['Power_Consumption_kW'], color='skyblue', alpha=0.4)
plt.plot(df['Timestamp'], df['Power_Consumption_kW'], color='Slateblue', alpha=0.8)
plt.title('Power Consumption Over Time')
plt.tight_layout()
plt.show()
