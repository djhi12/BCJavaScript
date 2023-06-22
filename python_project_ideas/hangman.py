import random


def choose_word():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    return random.choice(words)


def initialize_game():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6
    return word, guessed_letters, attempts_left


def get_guess():
    guess = input("Guess a letter: ").lower()
    return guess


def update_game_state(word, guessed_letters, attempts_left, guess):
    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        attempts_left -= 1
        print("Wrong guess!")

    return guessed_letters, attempts_left


def display_word(word, guessed_letters):
    visible_word = ""
    for letter in word:
        if letter in guessed_letters:
            visible_word += letter
        else:
            visible_word += "_"

    print("Current word:", visible_word)


def display_hangman(attempts_left):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        """
    ]

    print(stages[6 - attempts_left])


def play_game():
    word, guessed_letters, attempts_left = initialize_game()

    while attempts_left > 0:
        display_word(word, guessed_letters)
        display_hangman(attempts_left)

        guess = get_guess()
        guessed_letters, attempts_left = update_game_state(
            word, guessed_letters, attempts_left, guess)

        if all(letter in guessed_letters for letter in word):
            display_word(word, guessed_letters)
            print("Congratulations! You won!")
            break

    if attempts_left == 0:
        display_hangman(attempts_left)
        print("Game over. You lost! The word was", word)


play_game()

"""
This code defines several functions to handle different aspects of the game, such as choosing a word, getting user input, updating the game state, and displaying the hangman figure and word. The play_game() function ties everything together and runs the game loop until the player wins or loses.

Please note that this is a basic implementation, and you can enhance it further by adding input validation, a user interface, or additional features as per your requirements.


DESCRIPTION:
Hangman Game Description:

You have been tasked with implementing a classic game of Hangman. Hangman is a word-guessing game where the player tries to guess a word by suggesting letters one at a time. The player has a limited number of attempts before the game ends.

Here's how the game works:
The computer will randomly choose a word from a predefined list.

The chosen word will be represented by a series of underscores, with each underscore representing a letter in the word.

The player's goal is to guess the letters in the word correctly.

For each guess, the player will enter a letter.

If the letter is present in the word, the corresponding underscore(s) will be replaced with the correctly guessed letter.

If the letter is not present in the word, a part of the hangman figure will be displayed. The hangman figure has 7 parts, and each incorrect guess will add a part to the figure until the entire figure is displayed.

The player continues guessing letters until they have guessed all the letters in the word or until the hangman figure is complete.

If the player guesses all the letters in the word correctly, they win the game.

If the hangman figure is complete before the player guesses all the letters, they lose the game.

Your task is to implement the Hangman game using Python. You should create functions to handle various aspects of the game, such as choosing a word, getting user input, updating the game state, and displaying the hangman figure and word. You can use the provided code template as a starting point and modify it as needed.

Make sure to test your implementation thoroughly to ensure it works correctly. You can play the game multiple times with different words to verify its functionality.

Good luck, and have fun implementing the Hangman game!
"""

