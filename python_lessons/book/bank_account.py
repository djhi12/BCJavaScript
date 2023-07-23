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
