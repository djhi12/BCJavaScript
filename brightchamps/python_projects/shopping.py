shopping_list = []

while True:
    print("Shopping List:")
    for i, item in enumerate(shopping_list):
        print(f"{i+1}. {item['name']} - ${item['price']}")

    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        item_name = input("\nEnter the item name: ")
        item_price = float(input("Enter the item price: "))
        item = {"name": item_name, "price": item_price}
        shopping_list.append(item)
        print(
            f"\n{item_name} (Price: ${item_price}) has been added to the shopping list.")
    
    elif choice == "2":
        item_name = input("\nEnter the item name you want to remove: ")
        found = False
        
        for item in shopping_list:
            
            if item["name"] == item_name:
                shopping_list.remove(item)
                print(f"{item_name} has been removed from the shopping list.")
                found = True
                break
        
        if not found:
            print("Item not found in the shopping list.")
            
    elif choice == "3":
        if len(shopping_list) == 0:
            print("\nThe shopping list is empty.")
        else:
            print("Current shopping list:")
            for item in shopping_list:
                print(f"{item['name']} - ${item['price']}")
    
    elif choice == "4":
        break
    
    else:
        print("\nInvalid choice, please try again.")

"""
In this program, the shopping list is stored in a list called shopping_list. The user is presented with a menu where they can choose to add an item, remove an item, view the list, or exit the program.

To add an item, the user is prompted to enter the name of the item, and it is then added to the shopping list.

To remove an item, the user is prompted to enter the name of the item they want to remove. If the item exists in the shopping list, it is removed; otherwise, an appropriate message is displayed.

To view the list, the program displays all the items in the shopping list. If the list is empty, an appropriate message is displayed.

To exit the program, the user can choose the "Exit" option, which breaks out of the while loop.


In this updated version, each item in the shopping list is represented as a dictionary with two keys: "name" and "price". When adding an item, the user is prompted to enter the item name and price. The price is stored as a float value.

When displaying the shopping list, the program prints both the item name and price for each item.

Feel free to modify or enhance the program further to meet your specific requirements. Enjoy!
"""