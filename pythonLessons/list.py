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