# Define a sample list
sample_list = [5, 2, 8, 1, 6, 3]

# sort(): Sorts the list in ascending order
sorted_list = sorted(sample_list)
print("Sorted list:", sorted_list)

# append(): Adds a single element to a list
sample_list.append(4)
print("List after append:", sample_list)

# extend(): Adds multiple elements to a list
sample_list.extend([9, 7])
print("List after extend:", sample_list)

# index(): Returns the first appearance of the specified value
index_of_6 = sample_list.index(6)
print("Index of 6:", index_of_6)

# max(list): It returns an item from the list with max value
maximum_value = max(sample_list)
print("Maximum value:", maximum_value)

# min(list): It returns an item from the list with min value
minimum_value = min(sample_list)
print("Minimum value:", minimum_value)

# len(list): It gives the total length of the list
length_of_list = len(sample_list)
print("Length of list:", length_of_list)

# list(seq): Converts a tuple into a list
sample_tuple = (10, 11, 12)
converted_list = list(sample_tuple)
print("Converted list:", converted_list)

# type(list): It returns the class type of an object
type_of_list = type(sample_list)
print("Type of list:", type_of_list)
