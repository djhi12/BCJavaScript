# Ask the user for their age and store it in a variable
age = int(input("\nEnter your age: "))

# Check if the user is old enough to vote
if age >= 18:
    print("You are old enough to vote.\n")

    # Check if the user is registered to vote
    registered = input("Are you registered to vote? (y/n) ")
    if registered == "y":
        print("Great, you are all set to vote!\n")
    elif registered == "n":
        print("You need to register to vote before you can vote.\n")
    else:
        print("Invalid input. Please enter 'y' or 'n'.\n")

# If the user is not old enough to vote
else:
    print("Sorry, you are not old enough to vote yet.\n")


"""
    In this program, we first ask the user for their age and store it in a variable. We then use a nested if statement to check if the user is old enough to vote. If they are, we ask them if they are registered to vote and provide different responses depending on their answer. If they are not old enough to vote, we let them know.
"""