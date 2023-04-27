"""
    In Python, a lambda function is a small, anonymous function that can be defined without a name. It is also sometimes referred to as an "anonymous function" or a "function literal".

    A lambda function is defined using the keyword lambda, followed by the function parameters, a colon, and the function body. For example, the following lambda function takes two arguments and returns their sum:
"""

lambda x, y: x + y


# This lambda function can be assigned to a variable and called like any other function:
add = lambda x, y: x + y
result = add(2, 3)
print(result) # Output: 5

# Lambda functions are often used as arguments to higher-order functions like map(), filter(), and reduce(). For example, the following code uses a lambda function with map() to square each element of a list:

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared)) # Output: [1, 4, 9, 16, 25]

# Lambda functions can be useful when you need a small function for a one-time use and it is not worth defining a separate named function. However, for more complex functions or functions that will be reused, it is generally better to define a named function for clarity and maintainability.


# Example Program

# Here is an example program that demonstrates the use of lambda functions in Python. This program takes a list of integers, uses a lambda function with filter() to remove any numbers less than 5, and then uses another lambda function with map() to square each remaining number:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() with a lambda function to remove numbers less than 5
filtered_numbers = filter(lambda x: x >= 5, numbers)

# Use map() with a lambda function to square each remaining number
squared_numbers = map(lambda x: x**2, filtered_numbers)

# Print the result
print(list(squared_numbers)) # Output: [25, 36, 49, 64, 81, 100]

# In this program, the lambda function used with filter() returns True for any number greater than or equal to 5, effectively removing any numbers less than 5 from the list. The lambda function used with map() squares each remaining number in the list. The final output is a list of squared numbers greater than or equal to 25.