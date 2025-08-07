import pandas as pd

# Creating a sample DataFrame
data = {'A': ['foo', 'foo', 'foo', 'bar'],
        'B': ['one', 'one', 'two', 'two'],
        'C': [1, 2, 3, 4],
        'D': [5, 6, 7, 8]}
df = pd.DataFrame(data)

print('Before Grouping')
print(df)

# Grouping by columns 'A' and 'B' and performing sum
df_grouped = df.groupby(['A', 'B']).sum()

print('After Grouping')
print(df_grouped)

# Resetting index to flatten the hierarchical index
df_reset = df_grouped.reset_index()

print('After Reseting Index')
print(df_reset)


import pandas as pd

# Creating a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': ['X', 'Y', 'Z', 'X', 'Y']}
df = pd.DataFrame(data)

print('Before Filtering')
print(df)

# Filtering DataFrame based on condition
df_filtered = df[df['C'] == 'X']

print('After Filtering')
print(df_filtered)

# Resetting index to re-establish sequential index
df_reset = df_filtered.reset_index(drop=True)  # Use drop=True to drop old index

print('After Reseting Index')
print(df_reset)


import pandas as pd

# Creating sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6]})
df2 = pd.DataFrame({'C': [7, 8, 9],
                    'D': [10, 11, 12]})

# Merging DataFrames
merged_df = pd.merge(df1, df2, left_index=True, right_index=True)

print('After Merging')
print(merged_df)

# Resetting index to flatten hierarchical index
merged_df_reset = merged_df.reset_index(drop=True)

print('After Reseting Index')
print(merged_df_reset)


import pandas as pd

# Assuming df is a DataFrame

# Resetting index before exporting
df_reset = df.reset_index(drop=True)

# Exporting DataFrame to CSV file without index
df_reset.to_csv('output.csv', index=False)


import pandas as pd

# Assuming df is a DataFrame

# Resetting index for better readability
df_reset = df.reset_index(drop=True)

print(df_reset)
