import pandas as pd
import numpy as np

# Creating the DataFrame
data = {'Name': ['', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# Using a simple condition
df['Age_Boolean'] = df['Age'] > 30

print("Using a simple condition")
print("\n", df, "\n")

# Using a lambda function for a more complex condition
df['Age_Boolean'] = df['Age'].apply(lambda x: x > 30)

print("Using a lambda function for a more complex condition")
print("\n", df, "\n")

# Using numpy.where for more flexible conditions
df['Age_Boolean'] = np.where(df['Age'] > 30, True, False)

print("Using numpy.where for more flexible conditions")
print("\n", df, "\n")

# Using .apply with a custom function
def check_age(age):
    return age > 30

df['Age_Boolean'] = df['Age'].apply(check_age)

print("Using .apply with a custom function")
print("\n", df, "\n")

# Using Series.map with a dictionary
age_map = {age: age > 30 for age in df['Age']}
df['Age_Boolean'] = df['Age'].map(age_map)

print("Using Series.map with a dictionary")
print("\n", df, "\n")

