import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r"C:\Users\CHRISTOPHER A\OneDrive\Desktop\Data Analytics\MD Python\manufacturin_G_dataset.csv"

df = pd.read_csv(file_path)

df['Timestamp'] = pd.to_datetime(
    df[['Year', 'Month', 'Day', 'Hour', 'Minutes']]
)

df.drop(columns=['Day', 'Month', 'Year', 'Hour', 'Minutes'], inplace=True)

df.to_csv(file_path, index=False)

print(" Timestamp column created and dataset updated successfully!")