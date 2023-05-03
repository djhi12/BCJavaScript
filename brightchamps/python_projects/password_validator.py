while True:
    password = input("\nEnter a password: ")
    strength = 0
    
    if len(password) >= 8:
        strength += 1
        
    if any(char.isdigit() for char in password):
        strength += 1
        
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