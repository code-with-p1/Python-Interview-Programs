# Define a sample tuple
sample_tuple = (3, 6, 2, 8, 1, 6, 4)

# cmp(tuple1, tuple2) - Compares elements of both tuples.
# Python 3 doesn't have cmp(), but you can compare tuples directly using ==
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
comparison_result = tuple1 == tuple2
print("Comparison result:", comparison_result)

# len(): total length of the tuple
length_of_tuple = len(sample_tuple)
print("Length of tuple:", length_of_tuple)

# max(): Returns item from the tuple with max value
maximum_value = max(sample_tuple)
print("Maximum value:", maximum_value)

# min(): Returns item from the tuple with min value
minimum_value = min(sample_tuple)
print("Minimum value:", minimum_value)

# tuple(seq): Converts a list into tuple
sample_list = [10, 11, 12]
converted_tuple = tuple(sample_list)
print("Converted tuple:", converted_tuple)

# sum(): returns the arithmetic sum of all the items in the tuple
sum_of_tuple = sum(sample_tuple)
print("Sum of tuple:", sum_of_tuple)

# any(): If even one item in the tuple has a Boolean value of True, it returns True.
# Otherwise, it returns False.
bool_tuple = (False, True, False)
any_result = any(bool_tuple)
print("Result of any():", any_result)

# all(): returns True only if all items have a Boolean value of True. Otherwise, it returns False.
all_result = all(bool_tuple)
print("Result of all():", all_result)

# sorted(): a sorted version of the tuple
sorted_tuple = sorted(sample_tuple)
print("Sorted tuple:", sorted_tuple)

# index(): It takes one argument and returns the index of the first appearance of an item in a tuple
index_of_6 = sample_tuple.index(6)
print("Index of 6:", index_of_6)

# count(): It takes one argument and returns the number of times an item appears in the tuple
count_of_6 = sample_tuple.count(6)
print("Count of 6:", count_of_6)
