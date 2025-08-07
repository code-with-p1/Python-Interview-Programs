import pandas as pd

# Creating a DataFrame from a dictionary
data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)


df['Name_Age_City'] = df.apply(lambda row : f"{row['Name']} - {row['Age']} - {row['City']}", axis=1)

print(df)