# Global variable
global_var = 10

def my_function():
    # Modifying global variable
    global global_var

    # Local variable
    local_var = 5
    print("Inside the function - local_var:", local_var)  # Accessing local variable
    print("Inside the function - global_var:", global_var)  # Accessing global variable

    # Modifying local variable
    local_var += 1
    print("Inside the function after modification - local_var:", local_var)

    global_var += 1
    print("Inside the function after modification - global_var:", global_var)

# Accessing global variable outside the function
print("Outside the function - global_var:", global_var)

# Accessing local variable outside the function - this will raise an error because local_var is not defined outside the function
# print("Outside the function - local_var:", local_var)

my_function()

# Accessing global variable after function call
print("Outside the function after function call - global_var:", global_var)
