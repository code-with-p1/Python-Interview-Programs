def character_count(input_string):
    result = {}
    string_list = list(input_string)
    for i in string_list:
        result.update({i : string_list.count(i)})
    return result

input_string = "PawanMane"
print(character_count(input_string))
# Output :{'P': 1, 'a': 3, 'w': 1, 'n': 2, 'M': 1, 'e': 1}