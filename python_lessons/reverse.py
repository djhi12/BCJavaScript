"""
In Python, the reverse() method is used to reverse the order of elements in a list. It modifies the list in-place, meaning it changes the original list without creating a new one. Here's how you can use the reverse() method:
"""

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]

"""
In the above example, the reverse() method is called on the my_list list, reversing its order. After calling reverse(), the list is modified, and when we print it, the elements are displayed in reverse order.

Note that the reverse() method is specific to lists and doesn't work with other sequence types like tuples or strings. To reverse a string, you can use slicing with a step value of -1. For example:
"""

my_string = "Hello, World!"
reversed_string = my_string[::-1]
print(reversed_string)  # Output: "!dlroW ,olleH"

# In this case, my_string[::-1] creates a new string that starts from the last character and goes backward with a step of -1, effectively reversing the string.