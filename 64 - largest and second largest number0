def find_largest_and_second_largest(numbers):
    if len(numbers) < 2:
        return "List must contain at least two elements."  # Ensures valid input

    largest = second_largest = None  # Initialize both to None

    for num in numbers:
        if largest is None or num > largest:
            # Update second largest before replacing largest
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num != largest):
            # Update second largest if it's None or a better candidate is found
            second_largest = num

    if second_largest is None:
        return "There is no second largest element."  # Handles cases with duplicates only

    return largest, second_largest  # Return as a tuple

# Example usage
numbers = [12, 35, 1, 10, 34, 1]
result = find_largest_and_second_largest(numbers)

# Check if the result is a tuple before printing
if isinstance(result, tuple):
    print(f"Largest element: {result[0]}, Second largest element: {result[1]}")
else:
    print(result)