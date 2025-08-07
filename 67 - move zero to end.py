# Approach 1
def move_zeros_to_end(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)

arr = [10, 0, 20, 0, 30, 40, 0, 50, 0]
print("Original List:", arr)
move_zeros_to_end(arr)
print("Modified List:", arr)

print("#"*100)

# Approach 2
def move_zeros_to_end(arr):
    pos = 0  # Position to place next non-zero
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            if i != pos:
                arr[i] = 0  # Replace old spot with 0
            pos += 1

arr = [10, 0, 20, 0, 30, 40, 0, 50, 0]
print("Original List:", arr)
move_zeros_to_end(arr)
print("Modified List:", arr)