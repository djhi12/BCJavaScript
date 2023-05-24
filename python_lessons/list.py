# Video: https://www.youtube.com/watch?v=9OeznAkyQz4

"""
In Python, a list is a collection of items that are ordered and changeable. It is one of the built-in data types and is very versatile. Lists are denoted by square brackets [] and can contain any data type, including other lists. Each item in a list has an index, starting from 0 for the first item, and can be accessed using square brackets with the index number.

"""

# Here is an example of creating a list:
my_list = [1, 2, 3, "hello", "world"]


# You can access the elements of a list using indexing like this:
print(my_list[0])   # prints 1
print(my_list[3])   # prints "hello"


# You can also use negative indexing to access elements from the end of the list, like this:
print(my_list[-1])  # prints "world"
print(my_list[-2])  # prints "hello"


# You can add elements to a list using the append() method like this:
my_list.append(4)


# You can also insert elements at a specific index using the insert() method:
my_list.insert(1, "new item")


# You can remove elements from a list using the remove() method like this:
my_list.remove(2)


# And you can check if an item is in a list using the in keyword:
if "hello" in my_list:
    print("hello is in the list")


"""
Lists are very useful in Python and are used in many applications.

"""


# Example Program
# Creating a list
fruits = ['apple', 'banana', 'cherry', 'date']

# Accessing elements
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing a list
print("Sliced list:", fruits[1:3])

# Modifying elements
fruits[0] = 'avocado'
print("Modified fruits:", fruits)

# Adding elements
fruits.append('elderberry')
print("After append:", fruits)

# Removing elements
removed_fruit = fruits.pop(2)
print("Removed fruit:", removed_fruit)
print("After pop:", fruits)

# Length of a list
print("Length of the list:", len(fruits))

# Checking existence of an element
print("Is 'banana' in the list?", 'banana' in fruits)

# Looping through a list
print("Looping through the list:")
for fruit in fruits:
    print(fruit)

# Sorting a list
fruits.sort()
print("Sorted list:", fruits)

# Reversing a list
fruits.reverse()
print("Reversed list:", fruits)

# Clearing a list
fruits.clear()
print("Cleared list:", fruits)

# This program demonstrates how to create a list, access elements by index, slice a list, modify elements, add and remove elements, get the length of a list, check the existence of an element, loop through a list, sort and reverse a list, and clear a list. Feel free to run the code and observe the output!