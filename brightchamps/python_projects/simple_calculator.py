# Simple calculator program

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

"""
In this program, the input() function is used to prompt the user to enter two numbers, which are then stored in variables num1 and num2. The four basic arithmetic operations (+, -, *, /) are performed on these numbers using variables addition, subtraction, multiplication, and division. Finally, the results of these operations are printed using the print() function.

Note that float() is used to convert the user input from a string to a float, since the arithmetic operations require numeric values.
"""