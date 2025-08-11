Raw Data: manufacturing_6G_dataset
Excel_file: Manufacturing_Excel
Power BI: Manufacturing Dataset Dashboard
Project Overview
This project analyzes a manufacturing dataset to measure and visualize production performance, defect rates, and efficiency scores.

1. Excel Analysis
- Cleaned and prepared data.
- Created pivot tables for:
  - Production Overview
  - Quality vs Production
  - Error vs Downtime Analysis
  - Coorrelation Analysis
- Built an Excel dashboard with KPIs and charts.

2. Python EDA
- Loaded dataset using Pandas.
- Performed statistical summary and descriptive analytics.
- Converted date/time columns to a single `Timestamp`.
- Generated charts:
  - Bar chart
  - Line chart
  - Area chart
  - Scatter plot
  - Violin plot
  - Outlier Detection
- Saved updated dataset with `Timestamp` column.

3. Power BI Dashboard
- Created interactive dashboard with:
  - KPI Cards (Avg Defect Rate, Avg Packet Loss, Avg Production Speed, Avg Efficiency Score)
  - Bar chart: Avg Defect Rate by Machine ID
  - Scatter plot: Defect Rate vs Production Speed
  - Stacked area chart: Production Speed over Time
  - Machine ID slicer

How to Run
1. Open `MD Excel` for raw and processed Excel files.
2. Run `MD Python` scripts in VS Code.
3. Open `.pbix` file in `MD Power BI` to view interactive dashboard.


Key Insights
- Machines with higher production speed tend to have slightly higher defect rates.
- Certain time ranges showed increased packet loss, affecting efficiency.
- Efficiency score variation highlights scope for process optimization.


Tools Used
- Excel:  Data cleaning, pivot tables, dashboard
- Python (Pandas, Matplotlib, Seaborn): EDA and visualization
- Power BI: Interactive dashboards


Author
CHRISTOPHER A
