data  = [1,2,3,5,6,8,9,10,13,14,15,19,20]

subarrays = []
current_subarray = [data[0]]

for i in range(1, len(data)):
    if data[i] == data[i-1]+1:
        current_subarray.append(data[i])
    else:
        subarrays.append(current_subarray)
        current_subarray = [data[i]]

subarrays.append(current_subarray)
print(subarrays)


data  = [1,2,3,5,6,8,9,10,13,14,15,19,20]
sub_array = []
current_subarray = [data[0]]
n = len(data)
for i in range(0, n-1):
    if data[i+1] - data[i] == 1:
        current_subarray.extend([data[i+1]])
    else:
        sub_array.append(current_subarray)
        current_subarray = [data[i+1]]
sub_array.append(current_subarray)
print(sub_array)