"""
    Recursion is a technique in programming where a function calls itself in order to solve a problem. This technique can be very useful for solving problems that can be broken down into smaller, similar sub-problems.

    In Python, a recursive function is defined in a similar way to a regular function, with the addition of a call to itself within the function body. Here's an example of a recursive function to calculate the factorial of a number:
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial_num = factorial(4)
print(factorial_num)

"""
    In this example, the function factorial takes an argument n and returns the factorial of that number. If n is equal to zero, the function returns one (the base case). Otherwise, the function multiplies n by the result of calling itself with n-1 as the argument (the recursive case).

    It's important to note that recursive functions can be inefficient, especially when dealing with large inputs, as they can require a lot of memory and stack space. It's also possible to accidentally create an infinite loop if the base case is not properly defined, so it's important to be careful when using recursion.
"""

