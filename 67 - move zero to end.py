def move_zeros_to_end(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)

# Example
arr = [10, 0, 20, 0, 30, 40, 0, 50, 0]
print("Original List:", arr)
move_zeros_to_end(arr)
print("Modified List:", arr)