# """
#     Great, let's build a "Guess the Number" game using a while loop in Python. Here's the basic outline of the program:

#     The computer generates a random number between 1 and 100, and the user is asked to guess the number.
    
#     The user inputs their guess, and the computer checks if it is equal to the generated number. If it is, the game ends and the user wins. If it isn't, the computer tells the user whether their guess was too high or too low, and prompts them to guess again.
    
#     The game continues until the user correctly guesses the number.
# """

# import random

# # generate a random number between 1 and 100
# number = random.randint(1, 100)

# # initialize the guess variable
# guess = None

# # start the game loop
# while guess != number:
#     # get the user's guess
#     guess = int(input("\nGuess a number between 1 and 100: "))

#     # check if the guess is too high or too low
#     if guess > number:
#         print("Too high, try again!")
#     elif guess < number:
#         print("Too low, try again!")

# # if the guess is correct, end the game and print a message
# print("Congratulations! You guessed the number {} correctly!\n".format(number))


# """
#     In this program, we start by importing the random module, which allows us to generate a random number using the randint() function. We then initialize the guess variable to None, and start the game loop using a while loop that continues until the user correctly guesses the number.

#     Within the loop, we get the user's guess using the input() function and convert it to an integer using the int() function. We then check if the guess is too high or too low using if statements, and provide feedback to the user using the print() function.

#     Once the user guesses the number correctly, the while loop ends, and we print a congratulatory message to the user using the print() function.

#     You can customize this program further by adding additional features, such as limiting the number of guesses the user can make or providing a range of numbers for the user to guess from.
# """

import random

# generate a random number between 1 and 100
number = random.randint(1, 100)
print(number)

# initialize the guess variable and guess count
guess = None
guess_count = 0

# start the game loop
while guess != number:
    # get the user's guess
    guess = int(input("\nGuess a number between 1 and 100: "))
    
    # increment the guess count
    guess_count += 1

    # check if the guess is too high or too low
    if guess > number:
        print("Too high, try again!")
    elif guess < number:
        print("Too low, try again!")

# if the guess is correct, end the game and print a message with the guess count
print("Congratulations! You guessed the number {} correctly in {} guesses!\n".format(number, guess_count))
