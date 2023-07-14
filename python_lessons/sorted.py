"""
The sorted() function in Python is used to sort an iterable object such as a list, tuple, or string, and returns a new sorted list. It does not modify the original object; instead, it creates a new sorted version of the object.

The general syntax of the sorted() function is as follows:

sorted(iterable, key=None, reverse=False)

"""


"""
Here's a breakdown of the parameters:

iterable: This is the iterable object (e.g., a list, tuple, or string) that you want to sort.

key (optional): This parameter specifies a function that is used to generate a key for each item in the iterable. The items are then sorted based on the keys. If not provided, the items are sorted based on their natural order.

reverse (optional): By default, the reverse parameter is set to False, which sorts the iterable in ascending order. If you set reverse to True, the iterable will be sorted in descending order.

Here are some examples to illustrate how the sorted() function works:
"""

# Example 1: Sorting a list in ascending order
numbers = [5, 2, 8, 1, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 6, 8]


# Example 2: Sorting a list in descending order
numbers = [5, 2, 8, 1, 6]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [8, 6, 5, 2, 1]


# Example 3: Sorting a list of strings based on the length of the strings
fruits = ['apple', 'banana', 'kiwi', 'orange']
sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits)  # Output: ['kiwi', 'apple', 'banana', 'orange']

"""
In this example, the key=len parameter is used to specify that the items should be sorted based on their lengths.

Note that the sorted() function returns a new list, so if you want to modify the original list, you can assign the sorted result back to the original variable. For example:
"""

numbers = [5, 2, 8, 1, 6]
numbers = sorted(numbers)
print(numbers)  # Output: [1, 2, 5, 6, 8]
