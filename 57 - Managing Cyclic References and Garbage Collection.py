import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a circular reference
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

# Remove references to the nodes
del node1
del node2

# Manually run garbage collection
collected = gc.collect()
print(f"Garbage collector: collected {collected} objects.")

# Print garbage collector statistics
print(gc.get_stats())
