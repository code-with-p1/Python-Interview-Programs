my_list = [1,2,3,4]

my_list.append(5)
my_list.append([6,7])

print(my_list)

my_list.extend([8])
my_list.extend([9, 10, 11, 12])

print(my_list)

my_list.remove(10)
del my_list[6]

print(my_list)

pop = my_list.pop()
print(f"popped item : {pop}")

index = my_list.index(5)
print("Index of value ", 5, "is:", index)

print("*"*20)
print(my_list)

#Reverse the list: This is a common one. Use [::-1] to reverse the list.
print(my_list[::-1])

#Select every second element in reverse order: Combine two slicing operations.
print(my_list[::-2])

#Select every second element: Use [::2] to select every second element.
print(my_list[::2])

#Get the first five elements: Use [:5] to get the first five elements.
print(my_list[:5])

# Get the last five elements: Use [-3:] to get the last five elements.
print("Here >>>>>>>>>", my_list[-3:])

# Get the middle element: Use [len(my_list)//2] to get the middle element.
print(my_list[len(my_list)//2])


print("*"*20)

print("*"*20)

my_list = [1,2,3,4,5,6,7,8,9]

print("List : ", my_list)

print("Left To Right (Positive Start & End Values) = my_list[0:9] : ", my_list[0:9])
print("Left To Right (Negative Start & End Values) = my_list[-9:] : ", my_list[-9:])


print("Right To Left (Positive Start & End Values) = my_list[5::-1] : ", my_list[5::-1])
print("Right To Left (Negative Start & End Values) = my_list[-1:-10:-1] : ", my_list[-1:-10:-1])

print("*"*20)
print('Sorting - start')
my_list.sort()  # Sorts the list in ascending order
print(my_list)
my_list.sort(reverse=False)  # Sorts the list in ascending order
print(my_list)
my_list.sort(reverse=True)  # Sorts the list in descending order
print(my_list)
my_list.reverse()  # Reverses the list

print(my_list)
print('Sorting - end')

count = my_list.count(3)  # Counts occurrences of 3

print(count)

my_list.clear()  # Removes all elements from the list

print(my_list)

#with all true values
samplelist1 = [1,1,True]
print("any() True values ::",any(samplelist1))

#with one false
samplelist2 = [0,1,True,1]
print("any() One false value ::",any(samplelist2))


#with all false
samplelist3 = [0,0,False]
print("any() all false values ::",any(samplelist3))

#empty list
samplelist4 = []
print("any() Empty list ::",any(samplelist4))


print("*"*100)

my_tuple = (1, 2, 3, 'a', 'b', 'c')
print(my_tuple)

print("*"*20)

print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

print("List : ", my_tuple)

print("Left To Right (Positive Start & End Values) = my_tuple[0:9] : ", my_tuple[0:6])
print("Left To Right (Negative Start & End Values) = my_tuple[-6:] : ", my_tuple[-6:])

print("Right To Left (Positive Start & End Values) = my_tuple[5::-1] : ", my_tuple[5::-1])
print("Right To Left (Negative Start & End Values) = my_tuple[-1:-7:-1] : ", my_tuple[-1:-7:-1])

new_tuple = my_tuple + (5, 6)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)

repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 4, 1, 2, 3, 4)

print(len(my_tuple))  # Output: 4

print(3 in my_tuple)  # Output: True
print(5 in my_tuple)  # Output: False

count = my_tuple.count(3)
print(count)  # Output: 1

index = my_tuple.index(3)
print(index)  # Output: 2


print("*"*20)
