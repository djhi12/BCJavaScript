"""
The index() method in Python is used to find the index of the first occurrence of a specified element in a list, tuple, or string. Its syntax is as follows:

index(element, start, end)
"""

"""
element: The element to search for in the sequence.

start (optional): The index from which the search starts. If not provided, the search starts from the beginning of the sequence.

end (optional): The index at which the search ends. If not provided, the search continues until the end of the sequence.

The index() method returns the index of the first occurrence of the element. If the element is not found, it raises a ValueError.
"""


# Here are a few examples to illustrate its usage:
# Example with a list
fruits = ['apple', 'banana', 'orange', 'banana']
index = fruits.index('banana')
print(index)  # Output: 1

# Example with a tuple
numbers = (10, 20, 30, 20)
index = numbers.index(20)
print(index)  # Output: 1

# Example with a string
message = "Hello, world!"
index = message.index('o')
print(index)  # Output: 4

# In the examples above, the index() method is used to find the index of the first occurrence of the specified element ('banana', 20, and 'o') in the given sequences.


# Example Program
# Example program using index()

fruits = ['apple', 'banana', 'orange', 'banana']

# Find the index of 'banana'
index = fruits.index('banana')
print("Index of 'banana':", index)  # Output: Index of 'banana': 1

# Find the index of 'banana' starting from index 2
index = fruits.index('banana', 2)
print("Index of 'banana' (starting from index 2):", index)  # Output: Index of 'banana' (starting from index 2): 3

# Find the index of 'grape' (element not present)
try:
    index = fruits.index('grape')
    print("Index of 'grape':", index)
except ValueError:
    print("Element 'grape' not found")  # Output: Element 'grape' not found

"""
In this example, we have a list called fruits containing various fruits. We use the index() method to find the index of 'banana' in the list. Additionally, we demonstrate finding the index of 'banana' starting from index 2. Finally, we handle the case where 'grape' is not present in the list by catching the ValueError exception and displaying an appropriate message.

When you run this program, it will output the respective results of the index() method calls.
""" 