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
    print("4. Apply age-based discount")
    print("5. Exit")

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
        age = int(input("Enter your age: "))
        discount = 0
        if age < 18:
            discount = 0.2  # 20% discount for customers below 18
        elif age >= 60:
            discount = 0.1  # 10% discount for customers 60 and above
        for item in shopping_list:
            item['discount'] = discount
        print(
            f"Age-based discount of {discount*100:.2f}% applied to all items.")
    elif choice == "5":
        break
    else:
        print("Invalid choice, please try again.")

"""
In this updated version, the program includes an additional menu option labeled "4. Apply age-based discount". When selected, the user is prompted to enter their age. Based on the entered age, the program applies a corresponding discount to all the items in the shopping list.

If the age is below 18, a 20% discount is applied to all items.
If the age is 60 or above, a 10% discount is applied to all items.
If the age is between 18 and 59, no additional discount is applied.

The discounts are stored in the `'discount
"""