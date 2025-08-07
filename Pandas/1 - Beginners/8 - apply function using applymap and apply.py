import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}
df = pd.DataFrame(data)

print("DataFrame before applying function:")
print(df)

# Applying a function to each element using applymap()
modified_df = df.applymap(lambda x: x * 2)

print("\nDataFrame after applying function using applymap():")
print(modified_df)


# Using apply():

# Applying a function to each element along the columns using apply()
modified_df_apply = df.apply(lambda x: x * 2)

print("\nDataFrame after applying function using apply():")
print(modified_df_apply)

# apply() function along a specific axis of a DataFrame

# Creating a DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

print()
print("DataFrame before applying function:")
print(df)

# Applying a function to each row using apply along axis 1
modified_df_apply_axis1 = df.apply(lambda x: x.sum(), axis=1)

print()
print("\nResult after applying function using apply along axis 1:")
print(modified_df_apply_axis1)

def test(val):
    return val + 10

df['A'] = df['A'].apply(test)

print()
print("\nResult after applying function using apply on a single column")
print(df)