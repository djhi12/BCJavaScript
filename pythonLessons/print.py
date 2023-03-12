"""
    In Python, the print() function is used to display text or values in the console. Here are some examples:
"""

# To print a simple string:
print("Hello, world!")

# Output: Hello, world!


# To print the value of a variable:
age = 25
print("My age is", age)

# Output: My age is 25


# You can also print multiple values by separating them with commas:
name = "John"
age = 30
print("My name is", name, "and I am", age, "years old.")


# Output: My name is John and I am 30 years old.


# By default, print() adds a newline character at the end of the output. You can change this behavior by using the end parameter:
print("Hello,", end=" ")
print("world!")

# Output: Hello, world!


# You can also use formatting to control how values are printed. One common method is to use the % operator:
name = "Alice"
age = 25
print("My name is %s and I am %d years old." % (name, age))

# Output: My name is Alice and I am 25 years old.


# Another way to format output is to use f-strings (introduced in Python 3.6):
name = "Bob"
age = 40
print(f"My name is {name} and I am {age} years old.")

# Output: My name is Bob and I am 40 years old.


