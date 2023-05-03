print(
"""
The password is at least 8 characters long.
The password contains at least one digit.
The password contains at least one uppercase letter.
The password contains at least one lowercase letter.      
""")

# This line starts an infinite loop, meaning the code will keep running until a break statement is encountered.
while True:
    
    # This line prompts the user to enter a password by displaying the message "Enter a password: " and storing the user's input in a variable called password.
    password = input("\nEnter a password: ")
    
    # This line initializes a variable called strength to 0. This variable will keep track of how strong the password is based on certain criteria.
    strength = 0
    
    # This line checks if the length of the password is 8 characters or more. If it is, strength is incremented by 1.
    if len(password) >= 8:
        strength += 1
        
    # This line checks if there is at least one digit in the password. If there is, strength is incremented by 1.
    if any(char.isdigit() for char in password):
        strength += 1
        
    # This line checks if there is at least one uppercase letter in the password. If there is, strength is incremented by 1.
    if any(char.isupper() for char in password):
        strength += 1
        
    if any(char.islower() for char in password):
        strength += 1
        
    if strength == 4:
        print("Password is strong enough.\n")
        break
    
    else:
        print("Password is not strong enough. Please try again.\n")


"""
    This program asks the user to enter a password and then checks whether it meets the following criteria:

    The password is at least 8 characters long.
    The password contains at least one digit.
    The password contains at least one uppercase letter.
    The password contains at least one lowercase letter.
   
    If the password meets all of these criteria, the program prints "Password is strong enough" and exits the loop. Otherwise, the program prints "Password is not strong enough. Please try again." and continues the loop to ask for a new password.
    
"""

