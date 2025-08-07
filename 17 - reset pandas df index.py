import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)
df.set_index('Name', inplace=True)  # Setting 'Name' as the index

print("Original DataFrame:")
print(df)

# Resetting the index
df_reset = df.reset_index()

print("\nDataFrame after reset_index():")
print(df_reset)
