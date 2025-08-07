# Example 1
print("\n-----------------------------------------------------------")
# Decorator function
def decorator_func(func):
    def wrapper_func():
        print("Wrapper Function Executed where display method called.")
        return func()
    print("Before we call function this code gets executed where we wrap display function with decorator.")
    return wrapper_func

# Assiging decorator
@decorator_func
def display():
    print('Display worked')

# Calling the function
display()

print("\n-----------------------------------------------------------")

# Example 2
def show():
    print("Show")

deco = decorator_func(show)
deco()
# print("\n-------------------------------")

