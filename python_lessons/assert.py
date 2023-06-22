"""
In Python, an assertion is a statement used to check whether a given condition is true. It is mainly used during development and testing to catch and handle logical errors or assumptions in the code. The assert statement takes an expression and evaluates it. If the expression is true, the program continues its execution normally. However, if the expression is false, an AssertionError exception is raised, indicating that an assumption in the code has been violated.

The syntax of the assert statement is as follows:

assert expression, message

Here, the expression is the condition that is being tested, and the message is an optional string that can be included to provide additional information about the assertion failure. The message is commonly used to explain why the assertion failed or to provide guidance on how to fix the issue.
"""


# Here's an example to illustrate the usage of the assert statement:
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

result = divide(10, 2)
print(result)  # Output: 5.0

result = divide(10, 0)  # Raises an AssertionError with the message "Divisor cannot be zero"

"""
In the above example, the assert statement is used to check if the divisor (b) is not zero before performing the division operation. If the divisor is zero, the assert statement triggers an exception with the specified message.

It's important to note that assertions can be disabled by using the -O (optimize) command-line option or by setting the PYTHONOPTIMIZE environment variable to a non-empty string. So, assertions should not be relied upon for normal error handling or input validation, but rather for checking logical conditions that should always hold true during development and testing.
"""


# Example Program
def calculate_discounted_price(price, discount):
    assert price >= 0, "Price must be a non-negative value"
    assert 0 <= discount <= 1, "Discount must be between 0 and 1"

    discounted_price = price - (price * discount)
    return discounted_price


# Test cases
print(calculate_discounted_price(100, 0.2))  # Output: 80.0
print(calculate_discounted_price(50, 0.5))  # Output: 25.0

# This will trigger an AssertionError since the price is negative
print(calculate_discounted_price(-10, 0.1))

# This will trigger an AssertionError since the discount is greater than 1
print(calculate_discounted_price(200, 1.5))

"""
In this example, we have a function calculate_discounted_price that calculates the discounted price given the original price and the discount rate. The function uses assertions to check the validity of the inputs.

The first assertion assert price >= 0, "Price must be a non-negative value" ensures that the price is a non-negative value. If the price is negative, an AssertionError is raised with the specified message.

The second assertion assert 0 <= discount <= 1, "Discount must be between 0 and 1" ensures that the discount is between 0 and 1 (inclusive). If the discount is outside this range, an AssertionError is raised with the specified message.

We then have some test cases that demonstrate the function's behavior. The first two test cases pass and print the expected discounted prices. However, the last two test cases trigger assertions because they violate the specified conditions, resulting in AssertionError exceptions being raised with the respective error messages.

Note that you can comment out the last two test cases or modify the values to see the assertions in action.
"""

