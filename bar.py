import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\CHRISTOPHER A\OneDrive\Desktop\Data Analytics\MD Python\manufacturin_G_dataset.csv"
df = pd.read_csv(file_path)
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Machine_ID', y='Production_Speed_units_per_hr', estimator='mean')
plt.title('Average Production Speed by Machine')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()