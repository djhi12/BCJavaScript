"""
In Python, *args is a special syntax used in function definitions to allow the passing of a variable number of arguments to a function. The term "args" is short for "arguments," and the preceding asterisk (*) indicates that the arguments will be collected into a tuple within the function.

Here's how you use *args in a function definition:
"""
def my_function(*args):
    # 'args' is now a tuple containing all the arguments passed to the function
    for arg in args:
        print(arg)

# Example usage of the function
my_function(1, 2, 3)

"""
In this example, my_function takes any number of arguments when it's called. When you call my_function(1, 2, 3), the arguments 1, 2, and 3 are collected into a tuple within the function, and the loop prints each argument on a separate line:
"""


"""
You can pass as many arguments as you like to a function that uses *args. If you call the function with no arguments, the args tuple will be empty, but the function will still execute without any issues.

Keep in mind that *args is just a convention, and you can use any other name instead of args. The asterisk (*) before the parameter name is what makes it collect the arguments into a tuple.
"""


# Example Program
def calculate_average(*args):
    if not args:
        return 0.0

    total = sum(args)
    return total / len(args)

# Example usage of the function
print(calculate_average(1, 2, 3, 4, 5))  # Output: 3.0 (average of 1, 2, 3, 4, 5 is 3.0)
print(calculate_average(10, 20, 30))    # Output: 20.0 (average of 10, 20, 30 is 20.0)
print(calculate_average(2))             # Output: 2.0 (average of 2 is 2.0)
print(calculate_average())              # Output: 0.0 (no arguments, so the average is 0.0)

"""
In this example, we define the calculate_average function with *args, allowing us to pass any number of arguments when calling the function. Inside the function, we first check if there are no arguments (if not args:), in which case we return 0.0 to avoid a division by zero error.

If there are arguments, we calculate the sum of all the arguments using sum(args) and then divide the sum by the number of arguments (len(args)) to get the average. Finally, we return the calculated average.

When we call the function with different sets of arguments, it calculates and prints the corresponding averages. If you try to call the function without any arguments, it will return an average of 0.0.
"""