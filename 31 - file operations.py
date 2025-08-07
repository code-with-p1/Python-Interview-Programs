# Read Only ('r'):
print("Read Only")
try:
    with open("filename.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found")

print("---------------------------------")

# Read and Write ('r+'):
print("Read and Write")
try:
    with open("filename.txt", "r+") as file:
        data = file.read()
        print("Before writing:", data)
        file.write("\nAppending some text.")
        file.seek(0)
        updated_data = file.read()
        print("After writing:", updated_data)
except FileNotFoundError:
    print("File not found")

print("---------------------------------")

# Write Only ('w'):
print("Write Only")
try:
    with open("filename.txt", "w") as file:
        file.write("Hello, this is a new file content.")
        print('Writing Completed')
except FileNotFoundError:
    print("File not found")

print("---------------------------------")

# Write and Read ('w+'):
print("Write and Read")
try:
    with open("filename.txt", "w+") as file:
        file.write("Hello, this is a new file content.")
        file.seek(0)
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found")

print("---------------------------------")

# Append Only ('a'):
print("Append Only")
try:
    with open("filename.txt", "a") as file:
        file.write("\nAppending some more text.")
        print('Appending Completed')
except FileNotFoundError:
    print("File not found")

print("---------------------------------")

# Append and Read ('a+'):
print("Append and Read")
try:
    with open("filename.txt", "a+") as file:
        file.write("\nAppending some more text.")
        file.seek(0)
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found")

print("---------------------------------")
