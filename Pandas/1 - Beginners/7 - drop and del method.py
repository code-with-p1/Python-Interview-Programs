# Using drop():

import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3],
        'B': ['a', 'b', 'c'],
        'C': [4, 5, 6]}
df = pd.DataFrame(data)

print("DataFrame before column removal:")
print(df)

# Removing columns using drop()
new_df = df.drop(columns=['A', 'C'])

print("\nDataFrame after column removal using drop():")
print(new_df)

# Using del:

# Removing a column using del
del df['B']

print("\nDataFrame after column removal using del:")
print(df)
