# name = input("Type your name: ")

"""
Python exceptions are errors that occur during the execution of a Python program. When an exception occurs, the program stops executing and raises an exception. If the exception is not handled, it will terminate the program.

There are several built-in exceptions in Python, such as:

    SyntaxError: Raised when there is a syntax error in the code.
    TypeError: Raised when an operation or function is applied to an object of inappropriate type.
    NameError: Raised when a local or global name is not found.
    IndexError: Raised when an index is out of range.
    ValueError: Raised when an operation or function receives an argument of the right type but an inappropriate value.
    KeyError: Raised when a dictionary key is not found.
    ZeroDivisionError: Raised when a division or modulo operation is performed on zero.

To handle exceptions, you can use a try and except block. The try block contains the code that may raise an exception, and the except block contains the code that is executed if the exception occurs. You can also use finally block to execute a code regardless of whether an exception was raised or not.

"""

# The "try" block contains the code that may raise an exception,
# the "except" block contains the code that is executed if the exception occurs.
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    
    print("The result is:", y)
    
# Raised when a division or modulo operation is performed on zero.
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Raised when an operation or function receives an argument of the right type but an inappropriate value.
except ValueError:
    print("Invalid input. Please enter a valid number.")

# to capture the exception instance as a variable. 
except Exception as e:
    print("An error occurred:", e)

# to execute a code regardless of whether an exception was raised or not.
finally:
    print("Program execution completed.")
