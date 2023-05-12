# In Python, "islower()" is a built-in string method that returns a boolean value indicating whether all the characters in a string are lowercase or not.

string1 = "hello world"
string2 = "Hello World"
string3 = "1234"

print(string1.islower())  # True
print(string2.islower())  # False
print(string3.islower())  # False

# In the above example, string1 is all lowercase, so the islower() method returns True. However, string2 has an uppercase "H" and "W", so islower() returns False. Similarly, string3 does not contain any letters at all, so islower() also returns False.


# Example Program
# Get input string from user
input_string = input("Enter a string: ")

# Check if input string is all lowercase
if input_string.islower():
    print("The input string is all lowercase.")
else:
    print("The input string is not all lowercase.")

# This program prompts the user to enter a string, and then uses the islower() method to check whether all the characters in the input string are lowercase. If they are, the program prints "The input string is all lowercase." Otherwise, it prints "The input string is not all lowercase."