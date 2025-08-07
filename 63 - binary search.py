def binary_search(arr,target):
    left_index, right_index = 0,len(arr)-1
    while left_index<=right_index:
        mid_index = (left_index+right_index)//2
        if arr[mid_index]==target:
            return mid_index
        elif arr[mid_index]<target:
            left_index=mid_index+1
        else:
            right_index=mid_index-1
    return -1

target = 100
input_data = sorted([10,4,8,50,25,777,100])

print("Output Index : " , binary_search(input_data,target))
#Output:2