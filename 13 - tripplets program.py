def generate_combinations(lst, k):
    if k > len(lst):
        return
    stack = [(0, [])]
    while stack:
        index, current_combination = stack.pop()
        if len(current_combination) == k:
            yield tuple(current_combination)
        for i in range(index, len(lst)):
            stack.append((i + 1, current_combination + [lst[i]]))

# Given list
lst = [1, 3, 5, 2, 8]
k = 3  # Number of values per group

# Generate combinations
combs = generate_combinations(lst, k)

# Print the combinations
for comb in combs:
    print(comb)
