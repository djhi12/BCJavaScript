"""
In Python, the "sort" function is used to sort elements in a list in ascending order. It modifies the original list in place and does not create a new sorted list. The syntax for using the "sort" function is as follows:
"""

list.sort(key=None, reverse=False)

"""
Here's a breakdown of the parameters:

list: The list that you want to sort.
key (optional): A function that takes an element from the list and returns a value on which the sorting should be based. By default, it uses the elements themselves for comparison.

reverse (optional): A boolean value indicating whether the list should be sorted in descending order. By default, it's set to False, which means the list is sorted in ascending order.
"""


# Here's an example usage of the "sort" function:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

"""
In this example, the "sort" function is used to sort the list of numbers in ascending order. The resulting sorted list is then printed.

Note that the "sort" function is specific to lists. If you want to sort other iterable types like tuples or sets, you can convert them to a list using the "list" function and then use the "sort" function. Alternatively, you can use the "sorted" function, which returns a new sorted list without modifying the original iterable.
"""


# Example Program
# Define a list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Print the original list
print("Original list:", numbers)

# Sort the list in ascending order
numbers.sort()

# Print the sorted list
print("Sorted list (ascending):", numbers)

# Sort the list in descending order
numbers.sort(reverse=True)

# Print the sorted list in descending order
print("Sorted list (descending):", numbers)

# In this example, we start with an unsorted list of numbers. First, we print the original list. Then, we use the sort function to sort the list in ascending order. After sorting, we print the sorted list. Finally, we use the sort function with the reverse=True parameter to sort the list in descending order, and print the resulting list.