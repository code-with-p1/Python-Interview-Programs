input_list = [-8, -6, -4, -3, -1, 0, 1, 2]
missing_value_list = []
for key, value in enumerate(input_list):
    if key < len(input_list) - 1:
        if input_list[key+1] - input_list[key] != 1:
            missing_value_list.append(input_list[key] + 1)

print(input_list)
print(missing_value_list)

print("*"*100)

list1 = [-9, -6, -4, -3, -1, 0, 1, 2, 5]
missing_value_list = []
for i in range(list1[0],list1[-1]):
    if i not in list1:
        missing_value_list.append(i)

print(list1)
print(missing_value_list)