import pandas as pd

# Creating the DataFrame
data = {'Name': ['', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
        'Boolean' : [True, True, True, False]}

df = pd.DataFrame(data)

# Aggregation operations on the 'Age' column
count = df['Age'].count()
sum_age = df['Age'].sum()
max_age = df['Age'].max()
min_age = df['Age'].min()
mean_age = df['Age'].mean()
median_age = df['Age'].median()
std_age = df['Age'].std()

print(f"Count: {count}")
print(f"Sum: {sum_age}")
print(f"Max: {max_age}")
print(f"Min: {min_age}")
print(f"Mean: {mean_age}")
print(f"Median: {median_age}")
print(f"Standard Deviation: {std_age}")

# Multiple aggregations on the 'Age' column
aggregations = df['Age'].agg(['count', 'sum', 'max', 'min', 'mean', 'median', 'std'])

print('\n\n')
print(aggregations)


print('\n\n')
# Aggregation operations on the 'Boolean' column
count = df['Boolean'].count()
sum_age = df['Boolean'].sum()
max_age = df['Boolean'].max()
min_age = df['Boolean'].min()
mean_age = df['Boolean'].mean()
median_age = df['Boolean'].median()
std_age = df['Boolean'].std()

print(f"Count: {count}")
print(f"Sum: {sum_age}")
print(f"Max: {max_age}")
print(f"Min: {min_age}")
print(f"Mean: {mean_age}")
print(f"Median: {median_age}")
print(f"Standard Deviation: {std_age}")

# Multiple aggregations on the 'Age' column
aggregations = df['Boolean'].agg(['count', 'sum', 'max', 'min', 'mean', 'median', 'std'])

print('\n\n')
print(aggregations)

print( (df['Boolean'].sum() / df['Boolean'].count()) * 100 )