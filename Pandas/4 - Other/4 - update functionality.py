# Creating new dataframe
import pandas as pd

initial_data = {
    'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],
	'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],
	'Age': [42, 52, 36, 21, 23],
	'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']
}

df = pd.DataFrame(initial_data, columns=['First_name', 'Last_name', 'Age', 'City'])

# Create new column using dictionary
new_data = {
    0:"Shyam",
	2:"Riya",
	3:"Jitender"
}

# combine this new data with existing DataFrame
df["First_name"].update(pd.Series(new_data))

print(df)
