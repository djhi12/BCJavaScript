"""
In Python, a function is a block of reusable code that performs a specific task. It allows you to break down your code into smaller, manageable pieces, which can be called and executed whenever needed. Functions provide modularity and reusability, making your code more organized and easier to understand.

Here's the general syntax for defining a function in Python:
"""


def function_name(parameters):
    # Code block
    # Statements

    # Optional return statement
    return value

"""
Let's break down each part of the function definition:

def: This keyword is used to define a function in Python.

function_name: It is the identifier or name of the function. Choose a descriptive name that indicates the purpose of the function.

parameters: These are optional inputs to the function. You can define zero or more parameters inside the parentheses. If there are multiple parameters, they are separated by commas.

:: The colon signifies the start of the function's code block.

Code block: This is the actual body of the function, where you write the statements that perform the desired task.

return: This keyword is used to specify the value that the function should return when it is called. It is optional, and if omitted, the function will return None.

Here's an example of a simple function that adds two numbers and returns the result:
"""

def add_numbers(a, b):
    result = a + b
    return result

# You can call this function by using its name followed by parentheses, providing the required arguments:
sum_result = add_numbers(5, 3)
print(sum_result)  # Output: 8

"""
In this example, add_numbers is the function name, and a and b are the parameters. When the function is called with arguments 5 and 3, it calculates the sum and returns the result, which is then printed to the console.

Functions can have any number of statements and can perform various operations. They are an essential part of Python programming and enable you to organize and structure your code effectively.
"""


# Example Program
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for the number
number = int(input("Enter a number: "))

# Call the factorial function
result = factorial(number)

# Print the factorial result
print("The factorial of", number, "is", result)

"""
In this program, the factorial function calculates the factorial of a given number n. It uses a recursive approach where the function calls itself with a smaller value of n until it reaches the base case of n == 0. The factorial of n is calculated as n * factorial(n - 1).

The program prompts the user to enter a number and stores it in the number variable. Then, it calls the factorial function with the number as an argument and stores the result in the result variable. Finally, it prints the factorial result using the print statement.

"""


