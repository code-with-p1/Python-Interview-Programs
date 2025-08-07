#Syntax >> lambda arguments: expression

add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

square = lambda x: x ** 2
print(square(5))  # Output: 25

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

pairs = [(1, 'A'), (3, 'C'), (2, 'B'), (4, 'D')]
pairs.sort(reverse=False)
print(pairs)

pairs = [(1, 'A'), (3, 'C'), (2, 'B'), (4, 'D')]
pairs.sort(key=lambda x: x[1])
print(pairs)  # Output: [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')]

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
