def move_zeros_to_left(lst):
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        if lst[left] == 0:
            left += 1
        elif lst[right] != 0:
            right -= 1
        else:
            # Swap non-zero element from right with zero element from left
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
            
    return lst

# Example usage
input_list = [1, 2, 3, 4, 0, 0, 0, 4, 5, 7, 0]
result = move_zeros_to_left(input_list)
print(result)


def move_zeros_to_left_simple(lst):
    zeros_count = lst.count(0)  # Count the number of zeros in the list
    non_zeros = [x for x in lst if x != 0]  # Create a list of non-zero elements
    result = ([0] * zeros_count) + non_zeros  # Concatenate zeros and non-zero elements
    return result

# Example usage
input_list = [1, 2, 3, 4, 0, 0, 0, 4, 5, 7, 0]
result = move_zeros_to_left_simple(input_list)
print(result)
