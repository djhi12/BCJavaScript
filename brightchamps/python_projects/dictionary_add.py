dictionary = {}  # initialize an empty dictionary

# function to add a new word and its meaning to the dictionary

# The def keyword is used to define a function called add_word().
def add_word():
    
    # The function starts by asking the user to enter a new word using the input() function and stores the input in the word variable.
    word = input("\nEnter a new word: ")
    
    # The function then asks the user to enter the meaning of the word using another input() function and stores the input in the meaning variable.
    meaning = input("Enter the meaning of the word: ")
    
    # The function then adds the word and its meaning to a dictionary using the square bracket notation and assigns it to the key word. The dictionary is assumed to be defined 
    dictionary[word] = meaning
    
    # Finally, the function prints a message confirming that the word has been added to the dictionary.
    print(f"\n{word} has been added to the dictionary with meaning: {meaning}\n")


# main program loop
while True:
    print("\nSelect an option:")
    print("1. Add a new word")
    print("2. Search for a word")
    print("3. Exit")
    choice = input("\nEnter your choice (1, 2, or 3): ")

    # If the user selects option 1, it calls a function named add_word() to add a new word and its meaning to the dictionary. The implementation of the add_word() function is not shown in this code snippet.
    if choice == "1":
        add_word()
        
    elif choice == "2":
        
        word = input("\nEnter a word to search for: ")
        
        if word in dictionary:
            print(f"\nThe meaning of {word} is: {dictionary[word]}\n")
        else:
            print(f"\n{word} is not in the dictionary \n")
            
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice, please try again")
