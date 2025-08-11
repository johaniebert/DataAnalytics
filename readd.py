import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r"C:\Users\CHRISTOPHER A\OneDrive\Desktop\Data Analytics\MD Python\manufacturin_G_dataset.csv"
df = pd.read_csv(file_path)
print(df.head())