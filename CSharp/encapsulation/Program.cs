/*
    In C#, "encapsulation" refers to the concept of wrapping data and code (methods) that operate on that data into a single unit, which can then be treated as a black box by other parts of the program.

    The main purpose of encapsulation is to hide the implementation details of an object's internal state and behavior from the outside world, while exposing a well-defined interface that other code can use to interact with that object. This helps to promote modularity, maintainability, and reusability of code.

    In C#, encapsulation is typically achieved through the use of access modifiers like public, private, protected, and internal, which control the visibility of class members (fields and methods) to other parts of the program. By default, class members are private and can only be accessed within the class itself.

    Encapsulation is one of the fundamental principles of object-oriented programming (OOP), along with inheritance and polymorphism. It enables developers to create robust and modular code that can be easily extended and maintained over time.
*/


// Example Program
using System;

public class BankAccount
{
    private string accountNumber;
    private decimal balance;

    public BankAccount(string accountNumber)
    {
        this.accountNumber = accountNumber;
        this.balance = 0;
    }

    public void Deposit(decimal amount)
    {
        if (amount <= 0)
        {
            throw new ArgumentException("Invalid deposit amount");
        }

        this.balance += amount;
    }

    public void Withdraw(decimal amount)
    {
        if (amount <= 0)
        {
            throw new ArgumentException("Invalid withdrawal amount");
        }

        if (amount > this.balance)
        {
            throw new ArgumentException("Insufficient balance");
        }

        this.balance -= amount;
    }

    public decimal GetBalance()
    {
        return this.balance;
    }
}

public class Program
{
    public static void Main()
    {
        BankAccount account = new BankAccount("1234567890");
        account.Deposit(1000);
        account.Withdraw(500);
        Console.WriteLine("Current balance: {0:C}", account.GetBalance());
    }
}


/*
    In this program, we define a BankAccount class that encapsulates the state (account number and balance) and behavior (deposit, withdraw, and get balance) of a bank account. The account number and balance are declared as private fields, which can only be accessed within the BankAccount class.

    The Deposit, Withdraw, and GetBalance methods are declared as public, which means they can be called from other parts of the program. However, these methods are the only way to interact with the BankAccount object from the outside, which ensures that the internal state of the object remains consistent and valid.

    In the Main method, we create a new BankAccount object, deposit some money, withdraw some money, and then print the current balance to the console. Thanks to encapsulation, we don't need to worry about the internal details of how the account works - we can simply use the public interface provided by the BankAccount class.
*/