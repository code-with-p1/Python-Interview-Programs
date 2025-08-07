import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Name': ['Alice', 'Bob', 'Charlie']})

df2 = pd.DataFrame({'ID': [2, 3, 4],
                    'Age': [25, 30, 35]})


# Performing an inner join
inner_join = pd.merge(df1, df2, on='ID', how="inner")

print("Inner Join:")
print(inner_join)


# Performing an outer join
outer_join = pd.merge(df1, df2, on='ID', how='outer')

print("\nOuter Join:")
print(outer_join)


# Performing a left join
left_join = pd.merge(df1, df2, on='ID', how='left')

print("\nLeft Join:")
print(left_join)


# Performing a right join
right_join = pd.merge(df1, df2, on='ID', how='right')

print("\nRight Join:")
print(right_join)
