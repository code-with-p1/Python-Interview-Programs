def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        result = fib_series[-1] + fib_series[-2]
        fib_series.append(result)
    return fib_series

num = 10

if num <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series with {num} terms : ", " ".join(map(str, fibonacci(num))))

print("******************************************")


def fibonacci(n):
  a, b = 0, 1
  result = []
  for _ in range(n):
    result.append(a)
    a, b = b, a + b
  return result

n = 10
print(f"Fibonacci series with {n} terms : ", " ".join(map(str, fibonacci(num))))

print("******************************************")

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        first = fibonacci_recursive(n-1)
        second = fibonacci_recursive(n-2)
        result = first + second
        print(f"{result} = {first} + {second}")
        return result

n_rec = 10
print(f"\nFibonacci series with {n_rec} terms (using recursion):")
for i in range(n_rec):
    res = fibonacci_recursive(i)
    print(res, end=" ")
print()
print("******************************************")
