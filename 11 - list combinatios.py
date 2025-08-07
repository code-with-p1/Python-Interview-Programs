import itertools
import random

# Original list
my_list =[1, 2, 3, 4, 5, 6, 7, 8]

# Shuffle the list
random.shuffle(my_list)

# Define the group size
group_size = 3

# Generate all combinations of specified length
combinations = list(itertools.combinations(my_list, group_size))

# Print the combinations
for combination in combinations:
    print(combination)


def generate_combinations(lst, group_size):
    # Shuffle the list
    random.shuffle(lst)
    
    # Generate combinations
    combinations = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if j - i == group_size:
                combinations.append(lst[i:j])
    
    return combinations

# Original list
my_list =[1, 2, 3, 4, 5, 6, 7, 8]

# Define the group size
group_size = 3
    
# Generate combinations
result = generate_combinations(my_list, group_size)

print("*"*50)
# Print the combinations
for combination in result:
    print(combination)