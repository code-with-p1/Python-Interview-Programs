# Index example

import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4', 'row5'])

# Label-based indexing using .loc[]
print("Label-based indexing:")
print(df.loc['row2', 'A'])  # Accessing a single element

# Integer-based indexing using .iloc[]
print("\nInteger-based indexing:")
print(df.iloc[1, 0])  # Accessing a single element

# Boolean indexing
print("\nBoolean indexing:")
print(df[df['A'] > 2])  # Filtering rows based on a condition


# Slicing rows and columns
print("Slicing:")
print(df.loc['row2':'row4', 'A':'B'])  # Slicing rows and columns using labels
