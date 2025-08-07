# Define a sample dictionary
sample_dict = {'a': 1, 'b': 2, 'c': 3}

# clear(): Removes all the elements from the dictionary
sample_dict.clear()
print("Dictionary after clear:", sample_dict)

# Re-populate the dictionary for further demonstrations
sample_dict = {'a': 1, 'b': 2, 'c': 3}

# copy(): Returns a copy of the dictionary
copied_dict = sample_dict.copy()
print("Copied dictionary:", copied_dict)

# fromkeys(): Returns a dictionary with the specified keys and value
keys = ['x', 'y', 'z']
value = 0
new_dict = dict.fromkeys(keys, value)
print("Dictionary from keys:", new_dict)

# get(): Returns the value of the specified key
value_of_a = sample_dict.get('a')
print("Value of 'a':", value_of_a)

# items(): Returns a list containing a tuple for each key-value pair
items_list = sample_dict.items()
print("Items list:", items_list)

# keys(): Returns a list containing the dictionary's keys
keys_list = sample_dict.keys()
print("Keys list:", keys_list)

# pop(): Removes the element with the specified key
removed_element = sample_dict.pop('b')
print("Removed element:", removed_element)
print("Dictionary after pop:", sample_dict)

# popitem(): Removes the last inserted key-value pair
removed_item = sample_dict.popitem()
print("Removed item:", removed_item)
print("Dictionary after popitem:", sample_dict)

# setdefault(): Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
default_value = sample_dict.setdefault('d', 4)
print("Value of 'd':", default_value)
print("Dictionary after setdefault:", sample_dict)

# update(): Updates the dictionary with the specified key-value pairs
sample_dict.update({'e': 5, 'f': 6})
print("Updated dictionary:", sample_dict)

# values(): Returns a list of all the values in the dictionary
values_list = sample_dict.values()
print("Values list:", values_list)

# cmp(): compare two dictionaries
# Python 3 doesn't have cmp(), but you can compare dictionaries directly using ==
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2}
comparison_result = dict1 == dict2
print("Comparison result:", comparison_result)
