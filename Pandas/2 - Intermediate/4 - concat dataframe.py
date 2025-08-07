import pandas as pd

# Concatenating DataFrames Along Rows (Axis 0):

# Creating two DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Concatenating along rows
result = pd.concat([df1, df2])
print(result)
print()
# Ignoring indexes during concatenation
result = pd.concat([df1, df2], ignore_index=True)
print(result)
print()

# Concatenating DataFrames Along Columns (Axis 1):

# Concatenating along columns
result = pd.concat([df1, df2], axis=1)
print(result)
print()

# Creating DataFrames with duplicate indices
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=[0, 1])
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]}, index=[1, 2])

# Concatenating with duplicate indices
result = pd.concat([df1, df2])
print(result)
print()

# Adding keys for identification
result = pd.concat([df1, df2], keys=['DF1', 'DF2'])
print(result)
print()

# Creating DataFrames with missing data
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})

# Concatenating with missing data
result = pd.concat([df1, df2], sort=False)
result = result.reset_index(drop=True)
print(result)
