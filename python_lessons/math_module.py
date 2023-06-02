"""
The Python math module provides a set of functions for mathematical operations. It doesn't operate directly on lists, but rather on individual values. However, you can use these functions with list comprehension or loops to perform mathematical operations on a list. Here's an overview of some commonly used math functions from the math module along with examples of how you can use them with lists:
"""

# math.sqrt(x): Returns the square root of x.
import math

numbers = [4, 9, 16]
roots = [math.sqrt(x) for x in numbers]
print(roots)  # Output: [2.0, 3.0, 4.0]


# math.pow(x, y): Returns x raised to the power of y.
import math

numbers = [2, 3, 4]
exponents = [math.pow(x, 2) for x in numbers]
print(exponents)  # Output: [4.0, 9.0, 16.0]


# math.sin(x): Returns the sine of x (in radians).
import math

angles = [0, math.pi / 2, math.pi]
sines = [math.sin(x) for x in angles]
print(sines)  # Output: [0.0, 1.0, 1.2246467991473532e-16]


# math.cos(x): Returns the cosine of x (in radians).
import math

angles = [0, math.pi / 2, math.pi]
cosines = [math.cos(x) for x in angles]
print(cosines)  # Output: [1.0, 6.123233995736766e-17, -1.0]


# math.radians(x): Converts the angle x from degrees to radians.
import math

degrees = [0, 30, 45, 60, 90]
radians = [math.radians(x) for x in degrees]
print(radians)  # Output: [0.0, 0.5235987755982988, 0.7853981633974483, 1.0471975511965976, 1.5707963267948966]


# These are just a few examples of how you can use the math module functions with lists. You can explore the math module's documentation for more available functions and their usages: https://docs.python.org/3/library/math.html