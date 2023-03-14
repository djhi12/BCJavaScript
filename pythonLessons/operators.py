"""
In Python, operators are used to perform various operations on values or variables. There are several types of operators available in Python:

Arithmetic Operators: These operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc. The common arithmetic operators are:

    Addition: +
    Subtraction: -
    Multiplication: *
    Division: /
    Modulo: %
    Floor Division: //
    Exponentiation: **

Comparison Operators: These operators are used to compare two values and return a Boolean value (True or False). The common comparison operators are:

    Greater than: >
    Less than: <
    Greater than or equal to: >=
    Less than or equal to: <=
    Equal to: ==
    Not equal to: !=

Logical Operators: These operators are used to combine two or more conditions and return a Boolean value. The common logical operators are:

    AND: and
    OR: or
    NOT: not

Assignment Operators: These operators are used to assign values to variables. The common assignment operators are:

    Assign: =
    Add and Assign: +=
    Subtract and Assign: -=
    Multiply and Assign: *=
    Divide and Assign: /=
    Modulo and Assign: %=
    Floor Division and Assign: //=
    Exponentiation and Assign: **=

Identity Operators: These operators are used to check if two variables refer to the same object. The common identity operators are:

    is
    is not

Membership Operators: These operators are used to check if a value is present in a sequence or not. The common membership operators are:

    in
    not in

Bitwise Operators: These operators are used to perform bitwise operations on binary numbers. The common bitwise operators are:

    Bitwise AND: &
    Bitwise OR: |
    Bitwise NOT: ~
    Bitwise XOR: ^
    Left Shift: <<
    Right Shift: >>

"""

# Example Code

# Arithmetic Operators:
x = 10
y = 3

# Addition
print(x + y)   # Output: 13

# Subtraction
print(x - y)   # Output: 7

# Multiplication
print(x * y)   # Output: 30

# Division
print(x / y)   # Output: 3.3333333333333335

# Modulo
print(x % y)   # Output: 1

# Floor Division
print(x // y)  # Output: 3

# Exponentiation
print(x ** y)  # Output: 1000


# Comparison Operators:
x = 10
y = 3

# Greater than
print(x > y)   # Output: True

# Less than
print(x < y)   # Output: False

# Greater than or equal to
print(x >= y)  # Output: True

# Less than or equal to
print(x <= y)  # Output: False

# Equal to
print(x == y)  # Output: False

# Not equal to
print(x != y)  # Output: True


# Logical Operators:
x = 5
y = 10

# AND
print(x > 0 and y > 0)   # Output: True
print(x > 0 and y < 0)   # Output: False

# OR
print(x > 0 or y > 0)    # Output: True
print(x < 0 or y < 0)    # Output: False

# NOT
print(not x > 0)         # Output: False
print(not y < 0)         # Output: True


# Assignment Operators:
x = 10

# Assign
x = 20
print(x)    # Output: 20

# Add and Assign
x += 5
print(x)    # Output: 25

# Subtract and Assign
x -= 3
print(x)    # Output: 22

# Multiply and Assign
x *= 2
print(x)    # Output: 44

# Divide and Assign
x /= 4
print(x)    # Output: 11.0

# Modulo and Assign
x %= 3
print(x)    # Output: 2.0

# Floor Division and Assign
x //= 2
print(x)    # Output: 1.0

# Exponentiation and Assign
x **= 3
print(x)    # Output: 1.0


# Identity Operators:
x = 10
y = 10
z = 5

# is
print(x is y)   # Output: True
print(x is z)   # Output: False

# is not
print(x is not y)   # Output: False
print(x is not z)   # Output: True


# Membership Operators:
my_list = [1, 2, 3, 4, 5]

# in
print(3 in my_list)     # Output: True
print(6 in my_list)     # Output: False

# not in
print(3 not in my_list) # Output: False
print(6 not in my_list) # Output: True


# Bitwise Operators:
x = 10
y = 3

# Bitwise AND
print(x & y)    # Output: 2

