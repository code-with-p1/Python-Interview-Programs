import pandas as pd
import numpy as np

# Creating the DataFrame
data = {'Name': [np.nan, np.nan, 'pawan', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# Total number of rows
total_rows = len(df)

# Number of rows where the 'Name' column is empty
num_empty_rows = df['Name'].isnull().sum()

# Calculate the percentage of empty rows
empty_percentage = (num_empty_rows / total_rows) * 100

print(df)
print()
print("Empty Rows ", num_empty_rows)
print("Total Rows ", total_rows)
print(f"Percentage of empty 'Name' rows: {empty_percentage}%")
