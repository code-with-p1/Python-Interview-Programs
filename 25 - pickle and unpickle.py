import pickle

# Sample dictionary
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Pickling the dictionary
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# Unpickling the dictionary
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

print("Original Data:", data)
print("Loaded Data:", loaded_data)
