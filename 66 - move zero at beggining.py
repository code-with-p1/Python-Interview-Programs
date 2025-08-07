def move_zeros_to_beginning(arr):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == 0:
            arr.pop(i)
            arr.insert(0,0)

# Example
arr = [0, 1, 0, 2, 0, 3, 4, 0, 5]
print("Original List:", arr)
move_zeros_to_beginning(arr)
print("Modified List:", arr)

print("#"*100)

# Approach 2
def move_zeros_to_beginning(arr):
    n = len(arr)
    pos = n - 1  # Pointer to place non-zero elements

    # Traverse from end to start
    for i in range(n-1, -1, -1):
        if arr[i] != 0:
            arr[pos] = arr[i]
            if pos != i:
                arr[i] = 0  # Replace original non-zero with 0
            pos -= 1

# Example
arr = [0, 1, 0, 2, 0, 3, 4, 0, 5]
print("Original List:", arr)
move_zeros_to_beginning(arr)
print("Modified List:", arr)