import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

bst = BinarySearchTree(names_1[0])
for name in names_1[1:]:
    bst.insert(name)

duplicates = []
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

'''Discussion:
The original runtime was O(n^2). The outer loop cycled through all names in
the first list, and for each of those names the inner loop cycled through all
of the names in the second list. 'n' is the number of names in a single list
and we assume that the two lists are of roughly equal length for a given run.

Using a binary search tree allows a search to be completed in O(log(n)), and
we are running n searches. Total time complexity is O(n log(n)).
'''

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates_set = set(names_1).intersection(set(names_2))

end_time = time.time()
print (f"{len(duplicates_set)} duplicates_set:\n\n{', '.join(duplicates_set)}\n\n")
print (f"runtime: {end_time - start_time} seconds")