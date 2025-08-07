my_list = [1, 2, 3, 4, 4, 5, 6, 6]
unique_list = list(set(my_list))
print(unique_list)

my_list = [1, 2, 3, 4, 4, 5, 6, 6]
unique_list = []
[unique_list.append(x) for x in my_list if x not in unique_list]
print(unique_list)

my_list = [1, 2, 3, 4, 4, 5, 6, 6]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
