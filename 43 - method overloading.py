class MathOperations:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c

# Create an object
math = MathOperations()

# The below line will throw an error because Python doesn't support method overloading directly.
# It only recognizes the latest definition of the method.
# print(math.add(2, 3))  

# Instead, we can define a method that accepts variable-length arguments
class MathOperations:
    def add(self, *args):
        return sum(args)

# Now, we can call the add method with different numbers of arguments
math = MathOperations()
print(math.add(2, 3))  # Output: 5
print(math.add(2, 3, 4))  # Output: 9
