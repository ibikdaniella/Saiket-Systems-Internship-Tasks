import pandas as pd

# Load the data
ts = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

# Quick check 
print(ts.head(10))
print(ts.dtypes)

# Check for missing values
print(ts.isnull().sum())

# Checking for blank spacess in TotalCharges
print('Blank TotalCharges:',
      ts['TotalCharges'].str.strip().eq('').sum())

#Checking dataset information
print(ts.info())
print(ts.shape)