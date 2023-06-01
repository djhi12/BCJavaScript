"""
In Python, len() is a built-in function that is used to determine the length or the number of elements in an object such as a string, list, tuple, or dictionary. It returns the count of items present in the object.

Here's the basic syntax of the len() function:
"""

len(object)

"""
The object parameter can be any iterable or sequence object. Here are some examples of using len() with different types of objects:
"""

# Strings:
string = "Hello, World!"
length = len(string)
print(length)  # Output: 13


# Lists:
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # Output: 5


# Tuples:
my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)
print(length)  # Output: 5


# Dictionaries:
my_dict = {'a': 1, 'b': 2, 'c': 3}
length = len(my_dict)
print(length)  # Output: 3


"""
Note that for dictionaries, len() returns the number of key-value pairs (i.e., the number of keys).

It's important to keep in mind that len() can be applied only to objects that support the concept of length or have a defined number of elements.
"""