"""
In Python, the "class" is a fundamental concept of object-oriented programming (OOP) that allows you to create user-defined data types. A class serves as a blueprint or template for creating objects that share common attributes (variables) and behaviors (methods). Objects are instances of a class, and they encapsulate data and behavior associated with that class.

Here's the basic syntax for defining a class in Python:
"""

class ClassName:
    pass
    # Class variables and methods go here

    def __init__(self, value1, value2, value...):
        pass
        # Constructor (initializer) method
        # This method is called when an object is created
        # 'self' is a reference to the object being created
        # 'parameters' are values that can be passed to initialize the object's attributes

        # Initialize class attributes here
        self.attribute1 = value1
        self.attribute2 = value2
        # ...

    def method1(self, parameters):
        pass
        # Method definition
        # 'self' refers to the instance of the class (the object itself)
        # 'parameters' are values that can be passed to the method for processing

        # Method implementation here
        # ...

    def method2(self, parameters):
        pass
        # Another method definition
        # ...

    # Additional methods and class variables can be defined here
    # ...


# Let's create an example class to represent a simple car:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, acceleration):
        self.speed += acceleration

    def brake(self, deceleration):
        self.speed -= deceleration

    def get_speed(self):
        return self.speed

# Create car objects
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2021)

# Accelerate car1 by 20 units
car1.accelerate(20)

# Brake car2 by 10 units
car2.brake(10)

# Get the speed of each car
print(car1.get_speed())  # Output: 20
print(car2.get_speed())  # Output: -10

"""
In this example, we defined a Car class with attributes like make, model, year, and speed, and methods like accelerate, brake, and get_speed. Each instance of the class (car object) can have its own unique values for these attributes and can execute the methods to perform specific actions.
"""


# Example Program
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance:.2f}")


# Example usage of the BankAccount class
if __name__ == "__main__":
    # Get account details from the user
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))

    # Create a bank account
    account1 = BankAccount(account_number, account_holder, initial_balance)

    # Deposit some money
    deposit_amount = float(input("Enter deposit amount: "))
    account1.deposit(deposit_amount)

    # Check the account balance
    account1.check_balance()

    # Withdraw some money
    withdrawal_amount = float(input("Enter withdrawal amount: "))
    account1.withdraw(withdrawal_amount)

    # Check the account balance again
    account1.check_balance()

"""
Now, the program will prompt the user to enter the account details and the initial balance. It will also ask for deposit and withdrawal amounts based on the user's input.

When using input(), keep in mind that it returns a string. To perform numerical operations, like depositing or withdrawing amounts, we need to convert the user input to a numeric type (e.g., float() for decimal numbers). Always consider handling possible exceptions if the user provides invalid input that cannot be converted to the desired type.
"""