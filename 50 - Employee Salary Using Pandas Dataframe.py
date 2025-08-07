import pandas as pd

# Create a larger DataFrame with some duplicate records
data = {
    'Employee Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Edward', 'Frank', 'Charlie', 'Grace', 'Helen', 'Ivy', 
                      'Jack', 'Edward', 'Kim', 'Leo', 'Mona', 'Nina', 'Oscar', 'Paul', 'Quincy', 'Rita', 'Sam', 'Tom', 
                      'Uma', 'Vivian', 'Walter', 'Xander', 'Yara', 'Zane', 'Kim', 'Leo'],
    'Department': ['HR', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 
                   'Finance', 'Marketing', 'HR', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 
                   'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'HR', 'HR', 'IT'],
    'Salary': [50000, 60000, 70000, 50000, 80000, 60000, 70000, 55000, 82000, 60000, 
               75000, 80000, 67000, 68000, 72000, 51000, 85000, 69000, 74000, 53000, 76000, 
               66000, 73000, 54000, 78000, 61000, 79000, 56000, 67000, 68000]
}

df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame with duplicates:")
print(df)

# Remove duplicates from the DataFrame
df_unique = df.drop_duplicates()

# Sort the DataFrame by salary in descending order
df_sorted = df_unique.sort_values(by='Salary', ascending=False)

# Add a rank column based on the salary
df_sorted['Rank'] = df_sorted['Salary'].rank(ascending=False, method='min').astype(int)

# Sort the DataFrame by salary in descending order
df_sorted = df_sorted.sort_values(by='Rank', ascending=True)

# Select the first 10 rows
first_10_rows = df_sorted.head(10)

# Select the 10th row only
tenth_row = df_sorted.iloc[9] if len(df_sorted) > 9 else None

print("\nDataFrame after removing duplicates:")
print(df_unique)

print("\nDataFrame sorted by Salary in descending order:")
print(df_sorted)

print("\nFirst 10 rows of the sorted DataFrame:")
print(first_10_rows)

print("\n10th row of the sorted DataFrame:")
print(pd.Series(tenth_row))
