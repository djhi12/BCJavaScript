/*
    In C#, the private keyword is an access modifier used to limit the visibility of a class member (field, property, method or nested type) to the class or struct where it is declared.

    Members declared as private are accessible only within the same class or struct and cannot be accessed from outside the class. This helps to hide the implementation details of a class or struct and prevent unintended modification or misuse of the member by other code in the application.
*/

using System;

public class BankAccount
{
    private string accountNumber;
    private decimal balance;

    public BankAccount(string accountNumber, decimal initialBalance)
    {
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }

    public void Deposit(decimal amount)
    {
        balance += amount;
    }

    public void Withdraw(decimal amount)
    {
        if (amount <= balance)
        {
            balance -= amount;
        }
        else
        {
            Console.WriteLine("Insufficient funds.");
        }
    }

    public void DisplayAccountInfo()
    {
        Console.WriteLine("Account number: {0}", accountNumber);
        Console.WriteLine("Balance: {0}", balance);
    }
}

public class Program
{
    public static void Main()
    {
        BankAccount myAccount = new BankAccount("12345", 1000.00m);

        myAccount.Deposit(500.00m);
        myAccount.Withdraw(2000.00m);
        myAccount.DisplayAccountInfo();
    }
}

/*
    In the above program, the BankAccount class has two private fields, accountNumber and balance, which can only be accessed within the class. The Deposit and Withdraw methods modify the balance field, while the DisplayAccountInfo method displays the values of both fields.

    In the Main method, a BankAccount object is created and its Deposit, Withdraw, and DisplayAccountInfo methods are called to demonstrate how the class works. Since the accountNumber and balance fields are private, they cannot be accessed or modified directly from outside the class.
*/