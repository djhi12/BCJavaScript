"""
In Python, decorators are a way to modify the behavior of functions or classes without changing their source code directly. Decorators allow you to wrap a function or class with another function, often called a decorator function, which can add extra functionality, modify the input/output, or perform any other actions before or after the execution of the decorated function or class.

Decorators are implemented using the concept of "higher-order functions" and "function annotations" in Python. A decorator function takes in a function or class as an argument, adds some functionality, and returns the modified function or class.

Here's an example of a simple decorator that logs the execution time of a function:
"""

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper

@measure_time
def my_function():
    # ... do something ...

    my_function()

"""
In the example above, we define a decorator function measure_time that takes in a function func as an argument. Inside the decorator function, we define an inner function wrapper that measures the execution time of func using the time module. The result is then printed, and the original function's result is returned.

To apply the decorator to a function, we use the @measure_time syntax above the function definition. This is equivalent to writing my_function = measure_time(my_function). When my_function is called, it is automatically wrapped with the measure_time decorator, and the execution time is measured and printed.

Decorators are a powerful feature in Python and can be used for various purposes like logging, input validation, caching, authentication, etc. They provide a clean and concise way to modify the behavior of functions or classes without modifying their original code.
"""


# Example Program
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function
def add_numbers(a, b):
    return a + b

@log_function
def multiply_numbers(a, b):
    return a * b

# Calling the decorated functions
print(add_numbers(2, 3))
print(multiply_numbers(4, 5))

"""
In this example, we define a decorator function log_function that takes in a function func as an argument. Inside the decorator, we define an inner function wrapper that logs the function name, arguments, and then calls the original function func with the provided arguments.

The @log_function syntax is used to apply the decorator to the add_numbers and multiply_numbers functions. When these functions are called, they are automatically wrapped with the log_function decorator, which logs the function details before executing them.

"""