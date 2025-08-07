import copy

# Shallow Copy
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)

# Modify the shallow copy
shallow_copied_list[0][0] = 100

print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

print("ID of Original List : ", id(original_list))
print("ID of Shallow Copied List : ", id(shallow_copied_list))


# Deep Copy
original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

# Modify the deep copy
deep_copied_list[0][0] = 100

print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

print("ID of Original List : ", id(original_list))
print("ID of Shallow Copied List : ", id(deep_copied_list))