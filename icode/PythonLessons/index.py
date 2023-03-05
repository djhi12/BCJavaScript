"""
Python index refers to the position of an item within a sequence such as a string, list, or tuple. The index of the first item in a sequence is always 0, while the index of the last item is always the length of the sequence minus 1. In Python, you can use indexing to access individual elements or slices of elements in a sequence.

"""

# For example, consider the following string:
my_string = "Hello, World!"


# To access the first character of the string, you would use index 0:
print(my_string[0])  # Output: "H"


# To access the fourth character of the string, you would use index 3:
print(my_string[3])  # Output: "l"


# You can also use negative indexing to access elements from the end of a sequence. For example, to access the last character of the string, you would use index -1:
print(my_string[-1])  # Output: "!"


# You can use slicing to access a range of elements in a sequence. For example, to access the first 5 characters of the string, you would use slicing:
print(my_string[0:5])  # Output: "Hello"

# Note that the first index is inclusive and the second index is exclusive, so the above example will include the characters at indices 0, 1, 2, 3, and 4, but not the character at index 5.


# You can also use slicing with a step value to skip over elements in a sequence. For example, to access every other character in the string, you would use a step value of 2:
print(my_string[::2])  # Output: "Hlo ol!"
