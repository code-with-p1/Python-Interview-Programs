list_data = [20, 15, 7, 7, 7, 18, 50, 50]

n = len(list_data)

for i in range(0, n):
    for j in range (0, n-i-1):
        if list_data[j] > list_data[j+1]:
            list_data[j], list_data[j+1] = list_data[j+1], list_data[j]

print(list_data)