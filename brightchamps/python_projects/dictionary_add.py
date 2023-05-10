dictionary = {}  # initialize an empty dictionary

# function to add a new word and its meaning to the dictionary


def add_word():
    word = input("\nEnter a new word: ")
    meaning = input("Enter the meaning of the word: ")
    dictionary[word] = meaning
    print(f"\n{word} has been added to the dictionary with meaning: {meaning}\n")


# main program loop
while True:
    print("\nSelect an option:")
    print("1. Add a new word")
    print("2. Search for a word")
    print("3. Exit")
    choice = input("\nEnter your choice (1, 2, or 3): ")

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
