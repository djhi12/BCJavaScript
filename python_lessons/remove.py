"""
In Python, the "remove" function is used to remove an element from a list. The "remove" function takes an argument that represents the element to be removed and modifies the list in-place.
"""

# Here's an example usage of the "remove" function:
fruits = ['apple', 'banana', 'orange']
fruits.remove('banana')
print(fruits)

"""
In the example above, the element 'banana' is removed from the list 'fruits' using the "remove" function. After the removal, the list contains only 'apple' and 'orange'.

It's important to note that the "remove" function removes the first occurrence of the specified element. If the element appears multiple times in the list, only the first occurrence will be removed. If the element is not found in the list, a ValueError will be raised.
"""


# Example Program
fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi']

print("Original list of fruits:", fruits)

# Remove the first occurrence of 'banana'
fruits.remove('banana')

print("After removing 'banana':", fruits)

# Try to remove an element that doesn't exist in the list
element = 'grape'
if element in fruits:
    fruits.remove(element)
    print("After removing", element + ":", fruits)
else:
    print(element, "is not present in the list.")

"""
In this program, we start with a list of fruits. We first print the original list, then use the remove() method to remove the first occurrence of the string 'banana'. After the removal, we print the updated list.

Next, we try to remove an element 'grape' that does not exist in the list. We use the in operator to check if the element is present in the list before removing it. Since 'grape' is not present, we print a message indicating that it is not present in the list.
"""