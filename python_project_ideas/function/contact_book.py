contacts = []

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

def search_contact():
    name = input("Enter the name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found!")
            print("Current details:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            contact["phone"] = input("Enter the new phone number: ")
            contact["email"] = input("Enter the new email address: ")
            print("Contact updated successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Thank you for using the Contact Book!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
