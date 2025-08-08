def find_two_sum(data, target):
    first_index = 0
    second_index = len(data)-1
    for num in range(0, len(data)):
        current_sum = data[second_index] + data[first_index]
        if current_sum == target:
            # print(f"Found index ({first_index},{second_index}) and values ({data[first_index]},{data[second_index]})")
            return [data[first_index], data[second_index]]
            break
        elif current_sum > target:
            second_index-=1
        else:
            first_index+=1

data = [1, 2, 3, 4, 5, 7, 11]
target = 12
result = find_two_sum(data, target)
print(result)