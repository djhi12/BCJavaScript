"""
In Python, a float is a data type that represents a decimal number with a fractional component, while an integer is a data type that represents a whole number without a fractional component.

"""

# Here's an example of how to create a float and an integer in Python:
# creating a float
x = 3.14

# creating an integer
y = 42


"""
You can perform various mathematical operations on both floats and integers in Python. When you perform an operation between a float and an integer, Python will automatically convert the integer to a float before performing the operation.

"""

# adding two floats
a = 2.5 + 3.7
print(a)  # output: 6.2

# adding an integer and a float
b = 5 + 2.3
print(b)  # output: 7.3

# dividing an integer by a float
c = 10 / 3.0
print(c)  # output: 3.3333333333333335


"""
Keep in mind that when you perform division between two integers in Python 2.x, the result will be truncated to an integer. To avoid this, you can cast one of the integers to a float before dividing.

"""

# integer division in Python 2.x
d = 10 / 3
print(d)  # output: 3

# floating-point division in Python 2.x
e = 10 / float(3)
print(e)  # output: 3.33333333333


"""
In Python 3.x, division between two integers will automatically result in a float, so this is not an issue.

"""

