# Driver License Program with Age Validation Function

# Define the age validation function
def is_eligible(age):
    if age >= 16:
        return True
    else:
        return False

# Prompt the user to input their information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
license_num = input("Enter your license number: ")
expiry_date = input("Enter your expiry date (MM/DD/YYYY): ")

# Validate the age using the age validation function
if is_eligible(age):
    print("You are eligible to apply for a driver's license.")
else:
    print("Sorry, you are not eligible to apply for a driver's license.")

# Display the driver's license information
print("\nDRIVER'S LICENSE")
print("Name: " + name)
print("Age: " + str(age))
print("Address: " + address)
print("License Number: " + license_num)
print("Expiry Date: " + expiry_date)
