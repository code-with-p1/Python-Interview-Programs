import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [32, 75, 30, 80],
    'Humidity': [60, 55, 65, 40]
}

df = pd.DataFrame(data)

print('Dataframe')
print(df)

pivot_df = df.pivot(index='Date', columns='City', values='Temperature')

print('Pivot Dataframe')
print(pivot_df)

print()
pivot_df = df.pivot(index='Date', columns='City', values='Humidity')
print('Pivot Dataframe')
print(pivot_df)


print()
print()
print()
print()

import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [32, 75, 30, 80],
    'Humidity': [60, 55, 65, 40]
}

df = pd.DataFrame(data)

print(df)
print()

pivot_table_df = df.pivot_table(index='Date', columns='City', values='Temperature', aggfunc='mean')
print(pivot_table_df)
