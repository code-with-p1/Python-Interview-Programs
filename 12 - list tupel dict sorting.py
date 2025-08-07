list_of_tuples = [('c', 45), ('b', 95), ('a', 35)]
list_of_tuples = sorted(list_of_tuples, key=lambda x: x[0], reverse=False)
print(list_of_tuples)

tuple_of_lists = (['c', 45], ['b', 95], ['a', 35])
tuple_of_lists = sorted(tuple_of_lists, key=lambda x: x[0], reverse=False)
print(tuple_of_lists)

list_of_tuples = [('c', 45), ('b', 95), ('a', 35)]
list_of_tuples = sorted(list_of_tuples, key=lambda x: x[1], reverse=False)
print(list_of_tuples)

tuple_of_lists = (['c', 45], ['b', 95], ['a', 35])
tuple_of_lists = sorted(tuple_of_lists, key=lambda x: x[1], reverse=False)
print(tuple_of_lists)

dict1 = {'c': 45, 'b': 95, 'a': 35}
sorted_items = dict(sorted(dict1.items(), key=lambda x: x[0], reverse=False))
print(sorted_items)

dict1 = {'c': 45, 'b': 95, 'a': 35}
sorted_items = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=False))
print(sorted_items)
