import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Exporting to CSV
df.to_csv('data.csv', index=False)  # index=False to exclude the DataFrame index

# Exporting to Excel
df.to_excel('data.xlsx', index=False)  # index=False to exclude the DataFrame index

# Exporting to JSON
df.to_json('data.json', orient='records')

# Exporting to HTML
df.to_html('data.html', index=False)

# Exporting specific columns to CSV
df[['Name', 'Age']].to_csv('specific_columns.csv', index=False)
