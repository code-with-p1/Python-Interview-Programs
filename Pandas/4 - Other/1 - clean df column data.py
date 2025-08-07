# importing pandas as pd
import pandas as pd

# Create the dataframe
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
				'Product':[' UMbreLla', ' maTtress', 'BaDmintoN ', 'Shuttle'],
				'Updated_Price':[1250, 1450, 1550, 400],
				'Discount':[10, 8, 15, 10]})

# Print the dataframe
print(df)

def Format_data(df):
	# iterate over all the rows
	for i in range(df.shape[0]):
		# reassign the values to the product column
		# we first strip the whitespaces using strip() function
		# then we capitalize the first letter using capitalize() function
		df.iat[i, 1] = df.iat[i, 1].strip().capitalize()
		df.iat[i, 2] = f"Price : {df.iat[i, 2]}"
		df.loc[i, 'Date']= f"Date : {df.loc[i, 'Date']}"
		df.iloc[i, 3]= f"Discount : {df.iloc[i, 3]}"
		

# Let's call the function
Format_data(df)

# Print the Dataframe
print(df)
print()

# importing pandas as pd
import pandas as pd

# Create the dataframe
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
				'Product':[' UMbreLla', ' maTtress', 'BaDmintoN ', 'Shuttle'],
				'Updated_Price':[1250, 1450, 1550, 400],
				'Discount':[10, 8, 15, 10]})

# Using the df.apply() function on product column
df['Product'] = df['Product'].apply(lambda x : x.strip().capitalize())

# Print the Dataframe
print(df)
