import pandas as pd

data = {
    'Store': ['A', 'B', 'A', 'B', 'C'],
    'Product': ['Apple', 'Banana', 'Apple', 'Banana', 'Apple'],
    'Sales': [100, 150, 200, 250, 300]
}

df = pd.DataFrame(data)

# Single Column
grouped = df.groupby('Store')
total_sales = grouped['Sales'].sum()
print(total_sales)

print("*"*50)

# Multiple Column
grouped = df.groupby(['Store', 'Product'])
total_sales = grouped['Sales'].sum()
print(total_sales)

print("*"*50)

# Applying Aggregation Functions
grouped = df.groupby('Store')
summary = grouped['Sales'].agg(['sum', 'mean', 'count'])
summary = summary.reset_index()
print(summary)

print("*"*50)

grouped = df.groupby(['Store', 'Product']).agg(['sum', 'mean', 'count'])
grouped = grouped.reset_index()
print(grouped)

print("*"*50)

for group_name, group_data in df.groupby('Store'):
    print(group_name)
    print(group_data)

print("*"*50)