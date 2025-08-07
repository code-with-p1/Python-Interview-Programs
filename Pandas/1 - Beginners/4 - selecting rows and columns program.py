# Using .loc[] and .iloc[]:

import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Selecting specific rows and columns using .loc[]
selected_rows_columns_loc = df.loc[[0, 2], ['Name', 'Age']] 

# Selecting specific rows and columns using .loc[] with the help of slicing
# selected_rows_columns_loc = df.loc[0:3, ['Name', 'Age']]

# Selecting specific rows and columns using .iloc[]
selected_rows_columns_iloc = df.iloc[[0, 2], [0, 1]]

# Selecting specific rows and columns using .loc[] with the help of slicing
# selected_rows_columns_iloc = df.iloc[0:3, 1:2]

print("DF")
print(df)

print("Using .loc[]:")
print(selected_rows_columns_loc)

print("\nUsing .iloc[]:")
print(selected_rows_columns_iloc)

# Using boolean indexing:

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Using boolean indexing to select rows based on condition
selected_rows = df[df['Age'] > 30]

print("Selected rows based on condition:")
print(selected_rows)

# Using .loc[] with boolean conditions:

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Using .loc[] with boolean conditions to select rows based on condition
selected_rows_loc_boolean = df.loc[df['Age'] > 30, ['Name', 'Age']]

print("Using .loc[] with boolean conditions:")
print(selected_rows_loc_boolean)
