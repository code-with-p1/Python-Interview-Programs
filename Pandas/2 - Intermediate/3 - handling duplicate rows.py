import pandas as pd

# Sample DataFrame with duplicate rows
data = {
    'ID': [1, 2, 3, 4, 2],
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'Alice'],
    'Age': [25, 30, 35, 40, 30]
}

df = pd.DataFrame(data)

print('Dataframe')
print(df)
print()

# Identifying duplicate rows
duplicate_rows = df[df.duplicated()]
print("Duplicate Rows:\n", duplicate_rows)
print()

# Identifying unique rows
non_duplicate_rows = df[df.duplicated() == False]
print("Non Duplicate Rows:\n", non_duplicate_rows)
print()


# Removing duplicate rows
df_unique = df.drop_duplicates()
print("DataFrame after removing duplicates:\n", df_unique)
print()

# Removing duplicates based on subset of columns
df_unique_subset = df.drop_duplicates(subset=['Name', 'Age'])
print("DataFrame after removing duplicates based on subset of columns:\n", df_unique_subset)
print()

# Keeping the last occurrence of duplicate rows
df_last_occurrence = df.drop_duplicates(keep='last')
df_last_occurrence = df_last_occurrence.reset_index(drop=True)
print("DataFrame keeping the last occurrence of duplicates:\n", df_last_occurrence)
print()

# Filling duplicate values with NaN
df_filled = df.mask(df.duplicated())
print("DataFrame with duplicate values filled with NaN:\n", df_filled)
print()

# Replacing duplicate values with previous values
df_filled_previous = df.fillna(method='ffill')
print("DataFrame with duplicate values replaced with previous values:\n", df_filled_previous)
print()
