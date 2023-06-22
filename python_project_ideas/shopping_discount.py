shopping_list = []

while True:
    print("Shopping List:")
    for i, item in enumerate(shopping_list):
        name = item['name']
        price = item['price']
        discount = item.get('discount', 0)
        discounted_price = price - (price * discount)
        print(
            f"{i+1}. {name} - ${price:.2f} (Discount: {discount*100:.2f}%) - ${discounted_price:.2f}")

    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item_name = input("Enter the item name: ")
        item_price = float(input("Enter the item price: "))
       
        item_discount = float(
            input("Enter the discount percentage (0-100): ")) / 100
       
        item = {"name": item_name, "price": item_price,
                "discount": item_discount}
        
        shopping_list.append(item)
        print(f"{item_name} (Price: ${item_price:.2f}, Discount: {item_discount*100:.2f}%) has been added to the shopping list.")
        
    elif choice == "2":
        item_name = input("Enter the item name you want to remove: ")
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
            print("The shopping list is empty.")
        else:
            print("Current shopping list:")
            for item in shopping_list:
                name = item['name']
                price = item['price']
                discount = item.get('discount', 0)
                discounted_price = price - (price * discount)
                print(
                    f"{name} - ${price:.2f} (Discount: {discount*100:.2f}%) - ${discounted_price:.2f}")
    elif choice == "4":
        break
    else:
        print("Invalid choice, please try again.")


"""
In this updated version, each item in the shopping list dictionary includes an additional key, "discount", which represents the discount percentage for that item.

When displaying the shopping list, the program calculates the discounted price based on the original price and discount percentage. The discounted price is then displayed along with the item name and price.

When adding an item, the user is prompted to enter the discount percentage for that item. The discount is divided by 100 to convert it from a percentage to a decimal.

Feel free to further customize or expand the program as per your requirements. Happy coding!
"""