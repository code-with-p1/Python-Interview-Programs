def print_reverse_list(lst):
    n = len(lst)
    for i in range(n):
        print("-----------------------------------------------")
        print("Left To Right Item : ", lst[i])
        print("Right To Left Item : ", lst[n - 1 - i])
        print("-----------------------------------------------")

# Example usage:
my_list = [11, 22, 33, 44, 55]
print_reverse_list(my_list)