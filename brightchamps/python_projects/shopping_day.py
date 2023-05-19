import datetime

shopping_list = []

while True:
    print("\nShopping List:")
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
    print("4. Apply day and age-based discount")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        item_name = input("\nEnter the item name: ")
        item_price = float(input("Enter the item price: "))
        item_discount = float(
            input("Enter the discount percentage (0-100): ")) / 100
        item = {"name": item_name, "price": item_price,
                "discount": item_discount}
        shopping_list.append(item)
        print(f"{item_name} (Price: ${item_price:.2f}, Discount: {item_discount*100:.2f}%) has been added to the shopping list.")
    
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
            print("\nCurrent shopping list:")
            for item in shopping_list:
                name = item['name']
                price = item['price']
                discount = item.get('discount', 0)
                discounted_price = price - (price * discount)
                print(
                    f"{name} - ${price:.2f} (Discount: {discount*100:.2f}%) - ${discounted_price:.2f}")
    
    elif choice == "4":
        age = int(input("\nEnter your age: "))
        day = datetime.datetime.today().strftime("%A")
        discount = 0
        
        if day == "Monday" and age >= 50:
            discount = 0.3  # 30% discount for customers aged 50 and above on Mondays
        elif day == "Wednesday" and age < 18:
            discount = 0.2  # 20% discount for customers below 18 on Wednesdays
        for item in shopping_list:
            item['discount'] = discount
        print(
            f"Day and age-based discount of {discount*100:.2f}% applied to all items.")
    
    elif choice == "5":
        break
    
    else:
        print("Invalid choice, please try again.")


"""
In this updated version, the program considers both the current day of the week and the customer's age to apply specific discounts to the items in the shopping list.

On Mondays, customers aged 50 and above receive a 30% discount on all items.
On Wednesdays, customers below 18 receive a 20% discount on all items.
For other days and age groups, no
"""