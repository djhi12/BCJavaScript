"""
The "in" keyword in Python is used to check if a value exists in a sequence or collection, such as a list, tuple, string, or set.

The syntax for using "in" is as follows:

value in sequence


Here, "value" is the item we want to check for existence, and "sequence" is the collection we want to search.

The "in" operator returns a boolean value - True if the value is present in the sequence, and False otherwise.

"""

# For example:
# Using "in" with a list
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # Output: True
print("orange" in fruits)   # Output: False

# Using "in" with a string
message = "Hello, World!"
print("Hello" in message)   # Output: True
print("Python" in message)  # Output: False

# We can also use the "not in" operator to check if a value does not exist in a sequence. For example:
# Using "not in" with a list
fruits = ["apple", "banana", "cherry"]
print("orange" not in fruits)   # Output: True
print("banana" not in fruits)   # Output: False


# Example Program
# Example program using "in" keyword

# Define a list of fruits
fruits = ["apple", "banana", "cherry"]

# Check if "banana" is in the list
if "banana" in fruits:
    print("Yes, banana is in the list of fruits!")

# Check if "orange" is in the list
if "orange" in fruits:
    print("Yes, orange is in the list of fruits!")
else:
    print("No, orange is not in the list of fruits.")

# Define a string
message = "Hello, World!"

# Check if "World" is in the string
if "World" in message:
    print("Yes, 'World' is in the message.")

# Check if "Python" is in the string
if "Python" in message:
    print("Yes, 'Python' is in the message.")
else:
    print("No, 'Python' is not in the message.")

# In this example program, we define a list of fruits and a string, and then use the "in" keyword to check if certain values are present in the list or string. The program then prints a message indicating whether or not each value was found.




