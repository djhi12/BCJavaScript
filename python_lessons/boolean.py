"""
In Python, a boolean is a data type that can have one of two possible values: True or False. Booleans are often used in conditional statements to control program flow.

Boolean values can be assigned to variables, and can also be the result of a comparison or logical operation. For example:
"""
x = True
y = False

print(x)    # Output: True
print(y)    # Output: False

print(5 < 10)   # Output: True
print(5 > 10)   # Output: False

print(True and False)   # Output: False
print(True or False)    # Output: True


# In Python, any non-zero numeric value or non-empty object is considered True, while False is equivalent to zero or an empty object.
print(bool(0))          # Output: False
print(bool(42))         # Output: True
print(bool(""))         # Output: False
print(bool("hello"))    # Output: True


# Booleans can also be used in conditional statements, such as if, elif, and else, to execute different code depending on whether a condition is true or false.
x = 5

if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10")

# Output: x is less than 10