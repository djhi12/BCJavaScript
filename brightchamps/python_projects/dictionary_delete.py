dictionary = {}


def add_word():
    word = input("Enter a new word: ")
    meaning = input("Enter the meaning of the word: ")
    dictionary[word] = meaning
    print(f"{word} has been added to the dictionary with meaning: {meaning}")


def update_word():
    word = input("Enter a word to update: ")
    if word in dictionary:
        new_meaning = input(f"Enter the new meaning of {word}: ")
        dictionary[word] = new_meaning
        print(f"{word} has been updated with the new meaning: {new_meaning}")
    else:
        print(f"{word} is not in the dictionary")


def delete_word():
    word = input("Enter a word to delete: ")
    if word in dictionary:
        del dictionary[word]
        print(f"{word} has been deleted from the dictionary")
    else:
        print(f"{word} is not in the dictionary")


while True:
    print("Select an option:")
    print("1. Add a new word")
    print("2. Search for a word")
    print("3. Update an existing word")
    print("4. Delete a word")
    print("5. Exit")
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    if choice == "1":
        add_word()
    elif choice == "2":
        word = input("Enter a word to search for: ")
        if word in dictionary:
            print(f"The meaning of {word} is: {dictionary[word]}")
        else:
            print(f"{word} is not in the dictionary")
    elif choice == "3":
        update_word()
    elif choice == "4":
        delete_word()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again")

"""
In this updated version of the program, we've added a new function called delete_word(). When the user selects option 4, the program prompts them to enter a word to delete. If the word is in the dictionary, the program deletes it using the del dictionary[word] syntax.

I hope this updated program helps you add the "Allow users to delete words and their meanings from the dictionary" feature to your own dictionary project!
"""