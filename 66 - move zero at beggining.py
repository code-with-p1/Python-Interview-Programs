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