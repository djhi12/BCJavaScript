student_names = []

while True:
    print("\nMenu:")
    print("1. Add a student name")
    print("2. Remove a student name")
    print("3. View the list of student names")
    print("4. Quit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("Enter the student's name: ")
        student_names.append(name)
        print(f"{name} has been added to the list.")
    
    elif choice == "2":
        name = input("Enter the student's name: ")
        if name in student_names:
            student_names.remove(name)
            print(f"{name} has been removed from the list.")
        else:
            print("That student is not in the list.")
    
    elif choice == "3":
        print("Current student names:")
        for name in student_names:
            print(name)
    
    elif choice == "4":
        print("\nGoodbye!\n")
        break
    
    else:
        print("Invalid choice. Please try again.")

# This program uses an infinite while loop to display a menu of options to the user, and then performs the appropriate action based on the user's input. The user can add a new student name to the list, remove an existing student name from the list, view the current list of student names, or quit the program. The program also includes input validation to ensure that the user enters a valid choice from the menu.