/* 
    In C#, the "main function" is the entry point of a program, which is the first method that gets executed when you run a C# application.

    Here, the keyword static means that the method can be called without creating an instance of the class that contains it. The return type void indicates that the method does not return any value. The parameter string[] args is an array of strings that represents the command-line arguments passed to the program.

    You can write your program logic inside the body of the "main function" or call other methods that implement the program's functionality. When the "main function" finishes executing, the program terminates.  

*/


// Example Program
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Enter your name: ");
        string name = Console.ReadLine();
        Console.WriteLine("Hello, " + name + "! Welcome to C# programming.");
        Console.ReadKey();
    }
}

/*
    This program prompts the user to enter their name and stores it in the name variable using the Console.ReadLine() method. It then outputs a greeting message using the Console.WriteLine() method, which concatenates the name variable with a welcome message. Finally, the program waits for the user to press any key before exiting, using the Console.ReadKey() method.

    When you run this program, it will display the message "Enter your name:" on the console. The user can then enter their name and press enter. The program will output a personalized greeting message based on the user's input.
*/