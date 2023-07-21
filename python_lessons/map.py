"""
In Python, the map() function is a built-in function that applies a given function to each item in an iterable (such as a list or a tuple) and returns an iterator that yields the results. The general syntax of the map() function is as follows:

map(function, iterable)

"""


"""
Here's a breakdown of the parameters:

function: This is the function that you want to apply to each element in the iterable. It can be a built-in function, a lambda function, or a custom function.

iterable: This is the iterable object (e.g., list, tuple) that you want to apply the function to.

The map() function takes each item from the iterable, applies the function to it, and returns an iterator that yields the results. You can convert the iterator to other iterable types like a list or tuple using the list() or tuple() functions, respectively.

Here's an example to illustrate how map() works:
"""
# Define a function
def square(x):
    return x ** 2

# Define an iterable
numbers = [1, 2, 3, 4, 5]

# Apply the function to each element in the iterable using map()
result = map(square, numbers)

# Convert the iterator to a list
squared_numbers = list(result)

print(squared_numbers)

"""
In the example above, we define a function called square() that calculates the square of a number. We have a list of numbers, and we use map() to apply the square() function to each element in the numbers list. The result is an iterator, which we convert to a list using list(). Finally, we print the squared numbers.
"""


# Example Program
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# List of temperatures in Celsius
celsius_temperatures = [23, 15, 30, 12, 19]

# Convert Celsius temperatures to Fahrenheit using map()
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))

# Print the converted temperatures
for c, f in zip(celsius_temperatures, fahrenheit_temperatures):
    print(f"{c}°C = {f}°F")

"""
In this example, we define a function celsius_to_fahrenheit() that takes a temperature in Celsius and converts it to Fahrenheit. We have a list of temperatures in Celsius called celsius_temperatures. We use map() to apply the celsius_to_fahrenheit() function to each temperature in the list. The result is an iterator, which we convert to a list using list(). Then, we iterate over the original Celsius temperatures and the converted Fahrenheit temperatures using the zip() function, and print them out in a formatted way.
"""