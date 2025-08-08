def perfect_square(data, target):
    first_index = 0
    last_index = len(data)-1
    for index in range(len(data)):
        mid_index = (first_index + last_index) // 2
        square = data[mid_index] * data[mid_index]
        if square == target:
            return data[mid_index]
        elif square < target:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1
    return False
data = [0,1,2,3,4,5,6,7,8,9]
target = 64
result = perfect_square(data,target)
print(f"Value : {result} is having square {target}")