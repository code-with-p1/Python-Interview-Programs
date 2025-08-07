import pandas as pd

# Creating a DataFrame
data = {'Old_Name1': [1, 2, 3],
        'Old_Name2': ['a', 'b', 'c']}
df = pd.DataFrame(data)

print("DataFrame before column renaming:")
print(df)

# Renaming columns using rename() method
df = df.rename(columns={'Old_Name1': 'New_Name1', 'Old_Name2': 'New_Name2'})

print("\nDataFrame after column renaming:")
print(df)
