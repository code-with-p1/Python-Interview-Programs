def log_decorator(level):
    # Step 2: Define the decorator function
    def decorator(func):
        # Step 3: Define the wrapper function
        def wrapper(*args, **kwargs):
            if level == "INFO":
                print(f"INFO: Calling {func.__name__}")
            elif level == "DEBUG":
                print(f"DEBUG: Arguments were {args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"{level}: {func.__name__} returned {result}")
            return result
        return wrapper
    return decorator


def new_log_decorator(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "INFO":
                print(f"INFO: Calling {func.__name__}")
            elif level == "DEBUG":
                print(f"DEBUG: Arguments were {args}, {kwargs}")
            elif level == "Error":
                print(f"Error: Arguments were {args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"{level}: {func.__name__} returned {result}")
            return result     
        return wrapper
    return decorator

@log_decorator(level="INFO")
def add(a, b):
    return a + b

@log_decorator(level="DEBUG")
def multiply(a, b):
    return a * b

@new_log_decorator(level="Error")
def substraction(a,b):
    return a - b

# Test the decorated functions
print(add(2, 3))    # INFO log level
print(multiply(4, 5)) # DEBUG log level
print(substraction(10, 5)) # DEBUG log level
