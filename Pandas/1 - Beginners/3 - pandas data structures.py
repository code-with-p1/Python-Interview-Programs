import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print("\nData types:")
print(df.dtypes)
print("\nIndex:")
print(df.index)
print("\nColumns:")
print(df.columns)

# Creating a Series
series_data = [10, 20, 30, 40, 50]
s = pd.Series(series_data, name='Numbers')

print("\nSeries:")
print(s)
print("\nData type:")
print(s.dtype)
print("\nIndex:")
print(s.index)
