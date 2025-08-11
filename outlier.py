import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\CHRISTOPHER A\OneDrive\Desktop\Data Analytics\MD Python\manufacturin_G_dataset.csv"
df = pd.read_csv(file_path)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df = df.sort_values('Timestamp')

df_sample = df.iloc[::100, :]

metrics = ['Temperature_C', 'Vibration_Hz', 'Power_Consumption_kW',
           'Quality Control_Defect_Rate_%', 'Production_Speed_units_per_hr']

for col in metrics:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col], color='lightblue')
    plt.title(f"Outlier Detection - {col}")
    plt.tight_layout()
    plt.show()