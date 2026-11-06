# Saiket-Systems-Internship-Tasks
Telco Customer Churn Dataset – Data Exploration Using Python

1. Project Overview

This project focuses on understanding and exploring a Telco Customer Churn dataset using Python and the Pandas library.
The purpose of this task is to familiarize myself with the dataset, examine its structure, identify the data types of each column, and check for missing values.
The analysis was performed using Thonny IDE.

2. Dataset Description

The dataset contains customer information from a telecommunications company. It provides details about customer demographics, subscribed services, contract types, payment methods, charges, and customer churn status.

Dataset Overview

Description	Result
Total Rows	7,043
Total Columns	21
Total Records	7,043
Duplicate Records	0
Missing Values (Pandas)	0
Blank TotalCharges Entries	11

3. Tools and Technologies

* Python
* Pandas
* Thonny IDE
* CSV Dataset

4. Project Tasks

Task 1: Understand the Dataset

The following activities were performed:

1. Load the Dataset Using Pandas

Imported the CSV file into Python using the Pandas library.
import pandas as pd
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

2. Display the First 10 Rows

Used the head() function to display the first ten records.
print(df.head(10))

3. Identify the Data Types

Used the dtypes attribute to examine the data type of each column.
print(df.dtypes)

Data Types Identified

Data Type	Number of Columns
Object	18
Integer (int64)	2
Float (float64)	1
Total	21

4. Check for Missing Values

Used the isnull() and sum() functions to identify missing values.
print(df.isnull().sum())

5. Key Findings and Observations

During the initial exploration, the following observations were made:
* The dataset contains 7,043 customer records and 21 columns.
* The dataset has 18 object columns, 2 integer columns, and 1 float column.
* No conventional missing values were detected using Pandas’ isnull() function.
* Eleven blank or whitespace-only entries were identified in the TotalCharges column.
* The TotalCharges column is stored as an object data type and requires further investigation.

Additional Check

The following code was used to identify blank entries in the TotalCharges column:
print(df["TotalCharges"].str.strip().eq("").sum())
Result: 11 blank entries.

6. Skills Demonstrated

* Data Loading
* Dataset Exploration
* Data Type Identification
* Missing Value Detection
* Data Quality Assessment
* Python Programming
* Pandas Library

7. Conclusion

This task provided practical experience in loading and exploring a real-world dataset using Python and Pandas.
The initial exploration helped me understand the dataset’s structure, identify its data types, and discover potential data quality issues that may require attention during subsequent analysis.
This serves as the foundation for further data cleaning and exploratory data analysis.

Author
Mmesoma Jennifer Ibik
