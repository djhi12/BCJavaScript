contacts = []

# 1
def add_contact():
    name = input("\nEnter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("\nContact added successfully!\n")
    print(contacts)

# 2
def search_contact():
    name = input("\nEnter the name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found!")
            print_contact(contact)
            found = True
            break
    if not found:
        print("Contact not found.")

# 3
def update_contact():
    name = input("\nEnter the name of the contact to update: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found!")
            print_contact(contact)
            contact["phone"] = input("Enter the new phone number: ")
            contact["email"] = input("Enter the new email address: ")
            print("Contact updated successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")

# 4
def delete_contact():
    name = input("\nEnter the name of the contact to delete: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")

# 5
def print_contact(contact):
    print("Name:", contact["name"])
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])

def print_all_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- All Contacts ---")
        for contact in contacts:
            print_contact(contact)
            print()

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print_all_contacts()
        elif choice == "6":
            print("Thank you for using the Contact Book!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

"""
The added feature is the "View All Contacts" option (choice 5) in the menu. It allows the user to see all the contacts stored in the contacts list. The function print_all_contacts() is introduced to print the details of all contacts. If no contacts are found, it displays a message indicating that no contacts are available.
"""