"""
In Python, the "pop" method is used to remove and return an element from a list or a dictionary. The specific usage and behavior of the "pop" method depends on the data structure being used.
"""


"""
Pop from a list:
In a list, the "pop" method removes and returns the element at a specified index. If no index is provided, it removes and returns the last element of the list. The syntax for popping an element from a list is as follows:
"""

my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop()  # Removes and returns the last element
print(popped_element)  # Output: 5
print(my_list)  # Output: [1, 2, 3, 4]

popped_element = my_list.pop(2)  # Removes and returns the element at index 2
print(popped_element)  # Output: 3
print(my_list)  # Output: [1, 2, 4]


"""
Pop from a dictionary:
In a dictionary, the "pop" method removes and returns the value associated with a specified key. The syntax for popping a value from a dictionary is as follows:
"""

my_dict = {'a': 1, 'b': 2, 'c': 3}
popped_value = my_dict.pop('b')  # Removes and returns the value associated with key 'b'
print(popped_value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}

"""
Note that when popping a value from a dictionary, you need to provide the key as an argument to the "pop" method.

It's important to mention that the "pop" method modifies the original list or dictionary it is called on. If you don't need the returned value, you can simply use the "del" statement to remove an element from a list or a dictionary without returning it.
"""


# Difference between "remove" and "pop"
"""
In Python, both the "remove" and "pop" methods are used to remove elements from a list, but they differ in their functionality:

"remove" method:
The "remove" method is used to remove the first occurrence of a specified value from a list. It searches for the value in the list and removes it if found. If the value is not present, it raises a ValueError. The syntax for using the "remove" method is as follows:
"""
my_list = [1, 2, 3, 4, 5, 4]
my_list.remove(4)  # Removes the first occurrence of 4
print(my_list)  # Output: [1, 2, 3, 5, 4]

# In this example, the first occurrence of the value 4 is removed from the list.


"""
"pop" method:
The "pop" method, as explained in the previous response, is used to remove and return an element from a list based on its index. If no index is provided, it removes and returns the last element of the list. The syntax for using the "pop" method is as follows:
"""

my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop(2)  # Removes and returns the element at index 2
print(popped_element)  # Output: 3
print(my_list)  # Output: [1, 2, 4, 5]

"""
In this example, the element at index 2 (which is 3) is removed from the list and assigned to the "popped_element" variable.

To summarize:

The "remove" method removes the first occurrence of a specified value from a list, but it requires knowing the value itself.

The "pop" method removes an element from a list based on its index. It can also return the removed element, allowing you to use it if needed.

Both methods modify the original list. If you want to remove an element without returning it, you can use the "del" statement.
"""