error_list = [
    "Error96, Error76, Error36, Error26, Error16, Error6", 
    "Error93, Error73, Error33, Error23, Error13, Error3",
    "Error95, Error75, Error35, Error25, Error15, Error5",
    "Error915, Error715, Error315, Error215, Error115, Error15"
]

final_list = []

for string in error_list:
    new_string = list()
    only_numbers = string.replace("Error", "").split(", ")
    new_string = sorted(only_numbers, reverse=False)
    new_string  = list(map(lambda x: f"Error{x}", new_string))
    new_string = ", ".join(new_string)
    final_list.append(new_string)

print()
print("Input  >> ", error_list)
print()
print("Output >> ", final_list)
print()