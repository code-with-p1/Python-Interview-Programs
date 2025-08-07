list_data = [20, 15, 7, 7, 7, 18, 50, 50]

# Initialize variables
max_num = list_data[0]  # Assume the first element is the maximum
max_count = 0
counts = {}

# Iterate through the list to find the maximum number and count its occurrences
for num in list_data:
    if num > max_num:
        max_num = num
        max_count = 1  # Reset count since we found a new maximum
    elif max_num == num:
        max_count += 1  # Increment count if we find another occurrence of the current maximum

    if num in counts:
        counts[num] += 1  # Increment count if the element is already in the dictionary
    else:
        counts[num] = 1  # Initialize count to 1 if the element is not in the dictionary

print("*"*100)
# Output the result
print(f"Max Number : {max_num} and Its Count :  {max_count}")
# Output the result
print(f"Counts : {counts}")
print("*"*100)

list_data = [20, 15, 7, 7, 7, 18, 50, 50]

# Initialize variables
min_num = list_data[0]  # Assume the first element is the maximum
min_count = 0
counts = {}

# Iterate through the list to find the maximum number and count its occurrences
for num in list_data:
    if num < min_num:
        min_num = num
        min_count = 1  # Reset count since we found a new maximum
    elif min_num == num:
        min_count += 1  # Increment count if we find another occurrence of the current maximum

    if num in counts:
        counts[num] += 1  # Increment count if the element is already in the dictionary
    else:
        counts[num] = 1  # Initialize count to 1 if the element is not in the dictionary

# Output the result
print(f"Min Number : {min_num} and Its Count :  {min_count}")
# Output the result
print(f"Counts : {counts}")
print("*"*100)
