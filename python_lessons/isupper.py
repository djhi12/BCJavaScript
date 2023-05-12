# The isupper() method is a built-in string method in Python that returns True if all characters in a string are uppercase alphabets and there is at least one character in the string, otherwise it returns False.

string1 = "HELLO"
string2 = "Hello"
string3 = "123"
string4 = ""

print(string1.isupper())  # True
print(string2.isupper())  # False
print(string3.isupper())  # False
print(string4.isupper())  # False

# In the example above, string1 consists of all uppercase letters, so string1.isupper() returns True. string2 has a lowercase letter in it, so string2.isupper() returns False. string3 contains only numbers, so string3.isupper() returns False. Finally, string4 is an empty string, so string4.isupper() returns False.


# Example Program
# Program to check if a string is all uppercase or not

string = input("Enter a string: ")

if string.isupper():
    print("The given string is all uppercase.")
else:
    print("The given string is not all uppercase.")

# In this program, the user is prompted to enter a string. The isupper() method is used to check if the entered string is all uppercase or not. If it is all uppercase, the program prints "The given string is all uppercase." Otherwise, it prints "The given string is not all uppercase."