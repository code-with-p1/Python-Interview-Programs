def bubble_sort(arr):
    arr_len = len(arr) - 1
    for i in range(0, arr_len):
        inner_arr_len = arr_len-i
        for j in range(0, inner_arr_len):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Sample list to be sorted
arr = [39, 12, 18, 85, 72, 10, 2, 18]

print("Unsorted list is:")
print(arr)

# Call bubble_sort function
bubble_sort(arr)

print("Sorted list is:")
print(arr)

