"""
In Python, the append() method is used to add an element to the end of a list. It is a built-in function and can only be used with list objects. Here's the syntax:

list_name.append(element)

"""


"""
The list_name is the name of the list to which you want to add the element, and element is the value you want to append.

Here's an example:
"""
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
print(fruits)

"""
In this example, the string 'grape' is appended to the fruits list using the append() method. The updated list is then printed, showing that the new element has been added to the end.

It's important to note that append() modifies the original list in place and does not return a new list.
"""


# Example Program
# Create an empty list to store numbers
numbers = []

# Ask the user to enter 5 numbers and append them to the list
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Print the list of numbers
print("List of numbers:", numbers)
