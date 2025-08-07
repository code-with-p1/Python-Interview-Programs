# Define sample sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# add(): Adds an element to the set
set1.add(4)
print("Set after adding element:", set1)

# clear(): Removes all the elements from the set
set1.clear()
print("Set after clear:", set1)

# Re-populate the set for further demonstrations
set1 = {1, 2, 3}

# copy(): Returns a copy of the set
copied_set = set1.copy()
print("Copied set:", copied_set)

# difference(): Returns a set containing the difference between two or more sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print("Difference set:", difference_set)

# difference_update(): Removes the items in this set that are also included in another, specified set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print("Set after difference_update:", set1)

# discard(): Remove the specified item
set1.discard(1)
print("Set after discard:", set1)

# intersection(): Returns a set that is the intersection of two or more sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print("Intersection set:", intersection_set)

# intersection_update(): Removes the items in this set that are not present in other, specified set(s)
set1.intersection_update(set2)
print("Set after intersection_update:", set1)

# isdisjoint(): Returns whether two sets have an intersection or not
set1 = {1, 2, 3}
set2 = {3, 4, 5}
is_disjoint = set1.isdisjoint(set2)
print("Are sets disjoint?", is_disjoint)

# issubset(): Returns whether another set contains this set or not
set1 = {1, 2, 3}
set2 = {3, 4, 5}
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

# issuperset(): Returns whether this set contains another set or not
set1 = {1, 2, 3}
set2 = {3, 4, 5}
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)

# pop(): Removes an element from the set
set1 = {1, 2, 3}
popped_element = set1.pop()
print("Popped element:", popped_element)
print("Set after pop:", set1)

# remove(): Removes the specified element
set1 = {1, 2, 3}
set1.remove(3)
print("Set after remove:", set1)

# symmetric_difference(): Returns a set with the symmetric differences of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference set:", symmetric_difference_set)

# symmetric_difference_update(): Inserts the symmetric differences from this set and another
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print("Set after symmetric_difference_update:", set1)

# union(): Return a set containing the union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union set:", union_set)

# update(): Update the set with another set, or any other iterable
set1 = {1, 2, 3}
set1.update({5, 6, 7})
print("Set after update:", set1)
