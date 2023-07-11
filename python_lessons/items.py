"""
In Python, the items() method is a built-in function for dictionaries. It returns a view object that contains a list of key-value tuples of the dictionary's elements.

The syntax for using items() is as follows:

dictionary.items()
"""


"""
Here, dictionary refers to the dictionary object for which you want to retrieve the key-value pairs.

The items() method provides a convenient way to iterate over the key-value pairs of a dictionary. It returns the elements as a view object, which can be converted into a list or used directly in a loop.

Here's an example to demonstrate the usage of items():
"""

fruits = {
    'apple': 2,
    'banana': 4,
    'orange': 3
}

for fruit, quantity in fruits.items():
    print(f"There are {quantity} {fruit}s")

# Output:
# There are 2 apples
# There are 4 bananas
# There are 3 oranges

"""
In the example, fruits.items() returns a view object containing the key-value pairs of the fruits dictionary. The loop then iterates over each item, assigning the key to the fruit variable and the value to the quantity variable, and prints the information accordingly.

Note that the order of the key-value pairs in the view object is not guaranteed to be the same as the original order of insertion in the dictionary, as dictionaries in Python are unordered.
"""


# Example Program
# Create a dictionary of students and their ages
students = {
    'Alice': 18,
    'Bob': 20,
    'Charlie': 19,
    'David': 22,
    'Eve': 21
}

# Print the key-value pairs using items()
print("Student ages:")
for name, age in students.items():
    print(f"{name}: {age}")

# Output:
# Student ages:
# Alice: 18
# Bob: 20
# Charlie: 19
# David: 22
# Eve: 21

"""
In this example, we have a dictionary named students with student names as keys and their respective ages as values. We use the items() method to iterate over the key-value pairs of the dictionary. Inside the loop, we assign the key to the name variable and the value to the age variable. Then, we print the name and age of each student.

The output of the program will display the names and ages of the students stored in the dictionary.
"""