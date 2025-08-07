def longest_unique_substring(s):
    # Dictionary to store the last positions of each character
    last_seen = {}
    # Starting index of the current window
    start = 0
    # Length of the longest substring
    max_length = 0
    # Starting index of the longest substring
    max_start = 0
    
    for i, char in enumerate(s):
        # If the character is found in the dictionary and its index is within the current window
        if char in last_seen and last_seen[char] >= start:
            # Move the start to one past the last occurrence of the character
            start = last_seen[char] + 1
            
        # Update the last seen index of the character
        last_seen[char] = i
        
        # Update the max_length and max_start if we found a longer substring
        if i - start + 1 > max_length:
            max_length = i - start + 1
            max_start = start
    
    # Return the longest substring
    return s[max_start:max_start + max_length]

# Example usage
input_string = "abcabcdbb"
print("Input string:", input_string)
print("Longest substring without repeating characters:", longest_unique_substring(input_string))
