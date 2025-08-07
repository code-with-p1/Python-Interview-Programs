# Test Case
# Input = "aabbbccac"
# Output = "2a3b2c1a1c"

str_input = "aabbbccac"
str_output = ""
count = 1

for key, value in enumerate(str_input):
    arr_len = len(str_input) - 1
    if key < arr_len and str_input[key] == str_input[key + 1]:
        count = count + 1
    else:
        str_output = str_output + str(count) + str_input[key]
        count = 1

print(str_output)