def is_valid_parenthesis(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():  # Opening brackets
            stack.append(char)
        elif char in mapping.keys():  # Closing brackets
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # Ignore non-bracket characters if required
            pass

    return not stack  # True if stack is empty (all matched)

# Example usage:
print(is_valid_parenthesis("()[]{}"))       # True
print(is_valid_parenthesis("([{}])"))       # True
print(is_valid_parenthesis("({[)]}"))       # False
print(is_valid_parenthesis("(((()"))        # False
