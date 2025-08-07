# extend_math_operations.py

import math_operations

def multiply(a, b):
    return a * b

# Monkey patching to add the multiply function to the math_operations module
math_operations.multiply = multiply
