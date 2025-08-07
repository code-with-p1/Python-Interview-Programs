# def generate_combinations(arr, r):
#     # Initialize an empty list to store the combinations
#     combinations_list = []
#     n = len(arr)
    
#     # Initialize a list of indices to keep track of the current combination
#     indices = list(range(r))
    
#     while indices[0] < n - r + 1:
#         # Append the current combination to the combinations_list
#         combinations_list.append([arr[i] for i in indices])
        
#         # Find the rightmost index that can be incremented
#         i = r - 1
#         while i >= 0 and indices[i] == i + n - r:
#             i -= 1
            
#         # If no such index is found, we have generated all combinations
#         if i == -1:
#             break
        
#         # Increment the rightmost index that can be incremented
#         indices[i] += 1
#         for j in range(i + 1, r):
#             indices[j] = indices[j - 1] + 1
    
#     return combinations_list

# def find_good_triplets(N, arr):
#     good_triplets = []
#     # Generate all unique combinations of three numbers from the list
#     for triplet in generate_combinations(arr, 3):
#         # Check if the sum of the triplet is a three-digit number
#         if 100 <= sum(triplet) <= 999:
#             # Check if the triplet is unique
#             if triplet not in good_triplets:
#                 good_triplets.append(triplet)
#     return good_triplets

# # Example usage:
# N = 8
# arr = [1, 98, 1, 98, 1, 98, 1, 1]
# result = generate_combinations(arr, 3)
# print(result)
# exit()

# result = find_good_triplets(N, arr)
# print("Good triplets:")
# for triplet in result:
#     print(triplet)


def countGoodTriplets(arr, a, b, c):
    count = 0
    n = len(arr)
    data = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                first = abs(arr[i] - arr[j])
                second = abs(arr[j] - arr[k])
                third = abs(arr[i] - arr[k])
                if first <= a and second <= b and third <= c:
                    data.append([arr[i],arr[j],arr[k]])
                    count += 1
    return count, data

# Test Case 1
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

# Test Case 2
# arr = [1,1,2,2,3]
# a = 0
# b = 0
# c = 1

count, data = countGoodTriplets(arr, a, b, c)
print(f"Good Triplets : {count, data}")