import string

def is_palindrome(input_string):
    # Remove all spaces and punctuation marks
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))
    input_string = input_string.replace(" ", "")
    
    # Convert the string to lowercase
    input_string = input_string.lower()
    
    # Reverse the string using slicing
    reversed_string = input_string[::-1]
    
    # Compare the original string with the reversed string
    if input_string == reversed_string:
        print(f"{input_string} is a palindrome!")
    else:
        print(f"{input_string} is not a palindrome.")

user_input = input("Enter a word or phrase: ")

is_palindrome(user_input)
