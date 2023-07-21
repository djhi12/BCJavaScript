"""
The round() function in Python is used to round a number to a specified number of decimal places. It takes two arguments: the number you want to round, and the number of decimal places to round to. Here's the general syntax:

round(number, ndigits)

"""


"""
number: The number you want to round.
ndigits (optional): The number of decimal places to round to. If not provided, the function will round to the nearest whole number.

Here are a few examples of using the round() function:

"""
round(3.14159)  # Output: 3
round(3.14159, 2)  # Output: 3.14
round(3.14159, 3)  # Output: 3.142

"""
In the first example, since ndigits is not provided, the function rounds the number 3.14159 to the nearest whole number, which is 3.

In the second example, the function rounds the number 3.14159 to 2 decimal places, resulting in 3.14.

In the third example, the function rounds the number 3.14159 to 3 decimal places, resulting in 3.142.

It's important to note that the round() function uses "round half to even" rounding, also known as "banker's rounding." This means that when rounding a number that is exactly halfway between two possible rounded values, it rounds to the nearest even number. For example:
"""
round(2.5)  # Output: 2
round(3.5)  # Output: 4

"""
In both cases, the numbers are exactly halfway between 2 and 3, and 3 and 4, respectively. However, the round() function follows the "round half to even" rule, so it rounds 2.5 down to 2 and 3.5 up to 4.

Keep in mind that the round() function returns a float, even if the input is an integer.
"""


# Example Program
def round_number(number, decimal_places):
    rounded = round(number, decimal_places)
    print(f"The rounded value of {number} to {decimal_places} decimal places is: {rounded}")

# Example usage
round_number(3.14159, 2)
round_number(2.71828, 3)
round_number(5.6789, 0)

"""
In this example, we define a function round_number that takes a number and the desired number of decimal places to round to. It uses the round() function to perform the rounding and then prints the result.

We then demonstrate the usage of the round_number function by calling it three times with different inputs. It rounds 3.14159 to 2 decimal places, 2.71828 to 3 decimal places, and 5.6789 to 0 decimal places, respectively. The rounded values are then printed to the console.

Feel free to modify the inputs and decimal places in the round_number function to experiment with different values.
"""