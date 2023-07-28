"""
In Python, "inheritance" is a fundamental object-oriented programming concept that allows a class (called the child or derived class) to inherit attributes and methods from another class (called the parent or base class). Inheritance facilitates code reuse and promotes the creation of hierarchical relationships among classes.

When a class inherits from another class, it automatically gains access to the attributes and methods defined in the parent class. This means that you don't need to rewrite common code; instead, you can extend the functionality of the parent class by adding new attributes or methods in the child class.

Here's the basic syntax of defining a class that inherits from another class in Python:
"""

class ParentClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        print("This is method 1 from the parent class.")

class ChildClass(ParentClass):
    def __init__(self, attribute1, attribute2, attribute3):
        super().__init__(attribute1, attribute2)  # Call the constructor of the parent class
        self.attribute3 = attribute3

    def method2(self):
        print("This is method 2 from the child class.")

# Creating an instance of the child class
child_obj = ChildClass("value1", "value2", "value3")

# Accessing attributes and methods of both parent and child classes
print(child_obj.attribute1)  # Output: value1
print(child_obj.attribute3)  # Output: value3
child_obj.method1()  # Output: This is method 1 from the parent class.
child_obj.method2()  # Output: This is method 2 from the child class.

"""
In this example, ChildClass inherits from ParentClass by including the name of the parent class in parentheses after the child class name. The super().__init__() method is used in the child class's constructor to call the constructor of the parent class, allowing it to initialize the inherited attributes.

Keep in mind that Python supports multiple inheritance, meaning a class can inherit from multiple base classes. However, using multiple inheritance should be done carefully as it can lead to complex relationships and potential conflicts if not managed properly.
"""



# Example Program
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate / 100
        self.balance += interest_amount
        print(f"Interest applied. Current balance: {self.balance}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Withdrawal amount exceeds overdraft limit.")


# Create instances of the classes
savings_account = SavingsAccount(account_number="SA1234", balance=1000, interest_rate=2.5)
checking_account = CheckingAccount(account_number="CA5678", balance=2000, overdraft_limit=500)

# Perform some operations
savings_account.display_balance()  # Output: Account Number: SA1234, Balance: 1000
savings_account.deposit(500)       # Output: Deposited 500. Current balance: 1500
savings_account.apply_interest()   # Output: Interest applied. Current balance: 1537.5

checking_account.display_balance()  # Output: Account Number: CA5678, Balance: 2000
checking_account.withdraw(2200)     # Output: Withdrew 2200. Current balance: -200
checking_account.withdraw(300)      # Output: Withdrawal amount exceeds overdraft limit.

"""
In this example, the BankAccount class is the base class with common attributes like account_number and balance. It also has methods for depositing, withdrawing, and displaying the account balance.

The SavingsAccount class inherits from the BankAccount class and adds an interest_rate attribute along with a method apply_interest() to apply interest to the account balance.

The CheckingAccount class also inherits from the BankAccount class and includes an overdraft_limit attribute. It overrides the withdraw() method from the base class to take into account the overdraft limit when withdrawing funds.

The program demonstrates how we can create different types of bank accounts with specific functionalities while reusing the common functionalities from the base BankAccount class through inheritance.
"""