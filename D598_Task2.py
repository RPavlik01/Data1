#Import Library
import pandas as pd

dataset_path = 'data/D598 Data Set.xlsx'

#Import the dataset
ds = pd.read_excel(dataset_path, engine='openpyxl')

#Check for duplicates and remove
if ds.duplicated().any():
    #Remove duplicates
    ds = ds.drip_duplicates()

#Group data by State
grouped_ds = ds.groupby('Business State')

#Calculate statistics (mean, median, min, max)
stats_ds = grouped_ds.agg({
    'Total Long-term Debt': ['mean', 'median', 'min', 'max'],
    'Total Equity': ['mean', 'median', 'min', 'max'],
    'Debt to Equity': ['mean', 'median', 'min', 'max'],
    'Total Liabilities': ['mean', 'median', 'min', 'max'],
    'Total Revenue': ['mean', 'median', 'min', 'max'],
    'Profit Margin': ['mean', 'median', 'min', 'max']
}).reset_index()

#Filter rows where 'Debt to Equity' is negative
negative_debt_equity_ds = ds[ds['Debt to Equity'] < 0]

#Calculate Debt-to-Income Ratio for each business
ds['Debt-to-Income Ratio'] = ds['Total Long-term Debt'] / ds['Total Revenue']

#Concatenate original dataframe with the newly calculated Debt-to-Income Ratio
final_ds = ds

#Display the final result
print(final_ds.head())