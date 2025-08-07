# Map() Function
fruit = ["Apple", "Banana", "Pear"]
map_object = map(lambda s: s == "Apple", fruit)
print(list(map_object)) 

# Map() Function
fruit = ["Apple", "Banana", "Pear"]
lambda_func = lambda s: f"Fruit : {s}"
map_object = map(lambda_func, fruit)
print(list(map_object)) 

# Filter() Function
fruit = ["Apple", "Banana", "Pear"]
filter_object = filter(lambda s: s[0] == "A", fruit)
print(list(filter_object)) 

# Reduce() Function
from functools import reduce
numbers = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, numbers))
print("With an initial value: " + str(reduce(lambda x, y: x + y, numbers, 10)))




# Map() Function
numbers = [1, 2, 3, 4, 5]
# Define a function to square a number
def square(x):
    return x * x
# Use map to square each number in the list
squared_numbers = map(square, numbers)
# Convert the result to a list
squared_numbers = list(squared_numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]




# Filter() Function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Define a function to check if a number is even
def is_even(x):
    return x % 2 == 0
# Use filter to get only even numbers from the list
even_numbers = filter(is_even, numbers)
# Convert the result to a list
even_numbers = list(even_numbers)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]



# Reduce() Function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Define a function to multiply two numbers
def multiply(x, y):
    return x * y
# Use reduce to find the product of all numbers in the list
product = reduce(multiply, numbers)
print(product)  # Output: 120 (1 * 2 * 3 * 4 * 5)
