"""
In Python, the set() function is used to create a set, which is an unordered collection of unique elements. Sets are mutable, iterable, and can contain elements of different data types.

You can create an empty set using the set() function without any arguments:

my_set = set()

"""


# You can also create a set from an iterable, such as a list, tuple, or string:
my_set = set([1, 2, 3, 4, 5])
# or
my_set = set((1, 2, 3, 4, 5))
# or
my_set = set("hello")


"""
The resulting set will contain only the unique elements from the iterable. Duplicates are automatically removed. For example, in the set set([1, 2, 2, 3, 3]), the duplicate elements 2 and 3 are eliminated, and the resulting set is {1, 2, 3}.

Sets support a variety of operations such as union, intersection, difference, and more. Here are a few common operations:

"""


# Union (| or union()): Returns a new set that contains all the unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
# or
union_set = set1.union(set2)
# Result: {1, 2, 3, 4, 5}


# Intersection (& or intersection()): Returns a new set that contains the common elements between two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
# or
intersection_set = set1.intersection(set2)
# Result: {3}


# Difference (- or difference()): Returns a new set that contains the elements in the first set but not in the second set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
# or
difference_set = set1.difference(set2)
# Result: {1, 2}


# These are just a few examples of the operations you can perform on sets in Python. Sets are a powerful tool for handling unique collections of elements and performing various set operations efficiently.


# Example Program
# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Print the sets
print("Set 1:", set1)
print("Set 2:", set2)

# Perform set operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1 - set2

# Print the results
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set:", difference_set)

"""
In this example, we create two sets set1 and set2 containing some elements. Then we perform set operations using the union, intersection, and difference methods. Finally, we print the resulting sets.

Note that sets are unordered, so the order of elements may vary in the output. Additionally, sets only contain unique elements, so any duplicates are automatically eliminated.
"""