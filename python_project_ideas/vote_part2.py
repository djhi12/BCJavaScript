# Ask the user for their age and store it in a variable
age = int(input("\nEnter your age: "))

# Check if the user is old enough to vote
if age >= 18:
    print("You are old enough to vote.")

    # Ask the user how many candidates they want to vote for
    num_candidates = int(input("How many candidates do you want to vote for? "))

    # Use a for loop to prompt the user to enter each candidate's name
    for i in range(num_candidates):
        candidate_name = input("Enter the name of candidate #" + str(i+1) + ": ")
        print("You voted for " + candidate_name + ".")

    # Check if the user is registered to vote
    registered = input("Are you registered to vote? (y/n) ")
    if registered == "y":
        print("Great, you are all set to vote!")
    elif registered == "n":
        print("You need to register to vote before you can vote.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# If the user is not old enough to vote
else:
    print("Sorry, you are not old enough to vote yet.")
