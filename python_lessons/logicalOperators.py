"""
Python has three logical operators: and, or, and not.

"""

# The and operator returns True if both operands are true, and False otherwise. For example:
x = 5
y = 10
if x > 0 and y > 0:
    print("Both x and y are positive")

# In this example, the and operator is used to check if both x and y are positive. Since both are positive, the print statement will be executed.


# The or operator returns True if at least one operand is true, and False otherwise. For example:
x = 5
y = -1
if x > 0 or y > 0:
    print("At least one of x and y is positive")

# In this example, the or operator is used to check if at least one of x and y is positive. Since x is positive, the print statement will be executed.


# The not operator returns the opposite of the operand. For example:
x = 5
if not x > 0:
    print("x is not positive")
else:
    print("x is positive")


# In this example, the not operator is used to check if x is not positive. Since x is positive, the else block will be executed and the output will be "x is positive".

