# Using slicing
def is_palindrome(s):
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")

# Test the function
# is_palindrome("radar")
# is_palindrome("hello")

# print("******************************************")

#  Using Loop
def is_palindrome(s):
    n = len(s)
    print("==================================")
    print('Length : ', n)
    print('Range : ', range(n))
    print("==================================")
    for i in range(n):
        # print('First Element : ', s[i])
        # print('Last Element : ', s[n - i - 1])
        if s[i] != s[n - i - 1]:
            return False
    return True

# Test the function
# print(is_palindrome("aaadaaa"))
# print(is_palindrome("TESSET"))


# print("******************************************")

#  Using Recursion
def is_palindrome(s):
    print(s)
    print("\n------------")
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        print(s[:])
        print(s[1:-1])
        return is_palindrome(s[1:-1])

# Test the function
print(is_palindrome("radar"))  # Output: True
# print(is_palindrome("hello"))  # Output: False
