"""
In Python, a tuple is an ordered collection of elements, similar to a list. However, tuples are immutable, meaning that once a tuple is created, its contents cannot be changed. This makes tuples useful for storing and passing around data that should not be modified accidentally.

"""

# To create a tuple in Python, you can use parentheses to enclose a sequence of elements, separated by commas. For example:
my_tuple = (1, 2, 3)


# You can also create a tuple using the built-in tuple() function, which takes an iterable (such as a list or another tuple) as an argument:
my_list = [4, 5, 6]
my_tuple = tuple(my_list)


# You can access individual elements of a tuple using square brackets and the index of the element:
my_tuple = (1, 2, 3)
print(my_tuple[0])  # prints 1
print(my_tuple[1])  # prints 2
print(my_tuple[2])  # prints 3


# You can also use slicing to extract a range of elements from a tuple:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # prints (2, 3, 4)


# Tuples support many of the same operations as lists, such as concatenation and repetition:
my_tuple = (1, 2, 3)
my_other_tuple = (4, 5, 6)
my_combined_tuple = my_tuple + my_other_tuple  # results in (1, 2, 3, 4, 5, 6)

my_repeated_tuple = my_tuple * 3  # results in (1, 2, 3, 1, 2, 3, 1, 2, 3)


"""
One key difference between tuples and lists is that tuples are immutable. This means that you cannot modify a tuple directly by assigning a new value to an element. However, you can create a new tuple that is a modified version of the original tuple using techniques such as slicing and concatenation.

Overall, tuples are a useful data structure in Python for storing and passing around fixed sequences of data that should not be modified accidentally.

"""

