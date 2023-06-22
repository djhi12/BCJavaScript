import random

# Possible options for the game
options = ["rock", "paper", "scissors"]

# Function to determine the winner


def determine_winner(player_choice, computer_choice):
    
    if player_choice == computer_choice:
        return "It's a tie!"
    
    elif player_choice == "rock":
        if computer_choice == "paper":
            return "Computer wins!"
        else:
            return "You win!"
        
    elif player_choice == "paper":
        if computer_choice == "scissors":
            return "Computer wins!"
        else:
            return "You win!"
        
    elif player_choice == "scissors":
        if computer_choice == "rock":
            return "Computer wins!"
        else:
            return "You win!"

# Function to play the game


def play_game():
    # Get player's choice
    player_choice = input("\nEnter rock, paper, or scissors: ").lower()
    
    while player_choice not in options:
        player_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()

    # Get computer's choice
    computer_choice = random.choice(options)

    # Determine winner
    result = determine_winner(player_choice, computer_choice)

    # Print result
    print(f"You chose {player_choice}. The computer chose {computer_choice}. {result}")


# Play the game
while True:
    play_game()
    play_again = input("Do you want to play again? (y/n)\n").lower()
    if play_again != "y":
        break


"""
    This code defines a options list containing the three options, rock, paper, and scissors. It then defines a function determine_winner that takes in the player's choice and the computer's choice and returns the result of the game. The play_game function prompts the user for their choice, checks if the input is valid, generates the computer's choice, determines the winner, and prints the result. Finally, the main game loop repeatedly calls play_game and asks the user if they want to play again.

    You can modify this code to add more features, such as keeping track of the score, implementing a GUI, or adding sound effects.
"""