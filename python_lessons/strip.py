"""
In Python, the "strip" method is used to remove leading and trailing characters from a string. It returns a new string with the specified characters removed.

The syntax for using the "strip" method is as follows:

string.strip([characters])

"""

"""
Here, string represents the original string that you want to modify, and characters (optional) specifies the characters you want to remove. If characters is not provided, the "strip" method removes leading and trailing whitespace characters (spaces, tabs, and newlines) by default.

Here are a few examples to illustrate the usage of the "strip" method:
"""

text = "   Hello, World!   "
result = text.strip()  # Removes leading and trailing whitespace
print(result)  # Output: "Hello, World!"

text = "----Hello, World!----"
result = text.strip('-')  # Removes leading and trailing dashes
print(result)  # Output: "Hello, World!"

"""
In the first example, the "strip" method removes the leading and trailing spaces from the string. In the second example, it removes the leading and trailing dashes.

It's important to note that the "strip" method does not modify the original string but instead returns a new string with the desired modifications.
"""


# Example Program
text = input("Enter a sentence: ")  # Prompt the user to enter a sentence

stripped_text = text.strip()  # Remove leading and trailing whitespace

print("Stripped Text:", stripped_text)

"""
In this program, the user is prompted to enter a sentence. The input is stored in the text variable. Then, the strip method is applied to remove any leading and trailing whitespace from the inputted sentence, and the result is stored in the stripped_text variable.

Finally, the stripped text is printed to the console using the print statement.
"""