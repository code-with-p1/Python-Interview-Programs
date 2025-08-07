# Detecting Missing Values:
import pandas as pd
import numpy as np

# Creating a DataFrame with missing values
data = {'A': [1, np.nan, 3, np.nan, 5],
        'B': ['a', 'b', np.nan, np.nan, 'e'],
        'C': [np.nan, 2, 3, 4, np.nan]}

df = pd.DataFrame(data)

# Detecting missing values
missing_values = df.isnull()

print("DataFrame with Missing Values:")
print(df)
print("\nMissing Values:")
print(missing_values)

# Removing Missing Values:

# Removing rows with missing values
cleaned_df = df.dropna()

print("DataFrame after removing rows with missing values:")
print(cleaned_df)

# Filling Missing Values:

# Filling missing values with a specific value in specific column
df['A'] = df['A'].fillna(0)

print("DataFrame after filling missing values:")
print(df)

# Filling missing values with a specific value
filled_df = df.fillna(0)

print("DataFrame after filling missing values:")
print(filled_df)
