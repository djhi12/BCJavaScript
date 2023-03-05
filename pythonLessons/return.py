"""
In Python, the return statement is used to specify the value that a function should return when it is called.

"""

# For example, consider the following function:
def add_numbers(a, b):
    result = a + b
    return result

# In this function, the return statement specifies that the function should return the value of the result variable.


# When this function is called with two arguments, like this:
sum = add_numbers(2, 3)
print(sum)

# the sum variable will be assigned the value 5, because that is the value that was returned by the add_numbers function.


"""
It's important to note that a function can have multiple return statements, but only one of them will be executed. Once a return statement is executed, the function immediately stops executing and returns the specified value.

"""

# Here's an example of a function with multiple return statements:
def absolute_value(number):
    if number < 0:
        return -number
    else:
        return number

# In this function, if the number argument is less than zero, the function will return the negative value of number. Otherwise, it will return the original value of number.

