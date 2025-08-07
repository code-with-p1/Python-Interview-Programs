# Iteration
num = 6
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
print("The factorial of", num, "is", factorial)

# Recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

# change the value for a different result
num = 6
# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)


def walk(steps):
    if steps == 0:
        return
    else:
        walk(steps-1)
        print(steps)

print("Walk")
walk(10)

def walk(steps):
    if steps == 11:
        return
    else:
        walk(steps+1)
        print(steps)

print("Walk")
walk(1)
