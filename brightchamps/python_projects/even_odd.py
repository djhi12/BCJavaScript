# Ask the user for an input number
num = int(input("Enter a number: "))

# Check if the number is even
if num % 2 == 0:
    # If the number is even, print a message and double the number
    print("The number is even.")
    num *= 2
else:
    # If the number is odd, print a message and add 1 to the number
    print("The number is odd.")
    num += 1

# Print the final value of the number
print("The final value of the number is:", num)

# This program asks the user for an input number, checks if it is even using the modulus operator (%) and the logical operator (==), and then either doubles the number or adds 1 to it depending on whether it is even or odd. Finally, it prints out the final value of the number.