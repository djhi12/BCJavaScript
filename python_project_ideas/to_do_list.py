tasks = []

while True:
    print("\nTo-do list:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

    print("\nMenu:")
    print("1. Add task")
    print("2. Delete task")
    print("3. Mark task as complete")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("\nEnter a task: ")
        tasks.append(task)
        
    elif choice == "2":
        task = input("\nEnter the task you want to delete: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("\nTask not found")
            
    elif choice == "3":
        task = input("\nEnter the task you want to mark as complete: ")
        if task in tasks:
            tasks = [t if t != task else f"{task} (completed)" for t in tasks]
        else:
            print("\nTask not found")
            
    elif choice == "4":
        break
    else:
        print("Invalid choice, please try again")
