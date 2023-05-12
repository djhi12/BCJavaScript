# In Python, isdigit() is a built-in method that is used to check whether a given string consists of only digits or not. This method returns a Boolean value, True if all the characters in the string are digits and False otherwise.

string1 = "12345"
string2 = "12A45"

print(string1.isdigit()) # Output: True
print(string2.isdigit()) # Output: False

# In the above example, isdigit() method is called on two different strings. string1 contains only digits and returns True, whereas string2 contains an alphabet character 'A' and returns False.


# Example Program
# Take input from user
string = input("Enter a string: ")

# Check if all characters in the string are digits or not
if string.isdigit():
    print("The string consists of only digits.")
else:
    print("The string does not consist of only digits.")

# In the above program, we take a string as input from the user using the input() function. Then, we call the isdigit() method on the string to check whether it consists of only digits or not. If the method returns True, we print a message saying that the string consists of only digits. Otherwise, we print a message saying that the string does not consist of only digits.