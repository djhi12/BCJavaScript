using System;

class Program
{
    static void Main(string[] args)
    {
        /*
            In C#, a function is a block of code that performs a specific task and can be called from other parts of a program. Functions in C# are also known as methods.

            Functions are defined using the void keyword if they do not return a value, or a specific return type if they do. 
        */
        int a = 2;
        int b = 3;

        int result = AddNumbers(a, b);
        Console.WriteLine("The sum of {0} and {1} is {2}", a, b, result);
    }

    static int AddNumbers(int x, int y)
    {
        int sum = x + y;
        return sum;
    }
    
    // In this program, we define a function called AddNumbers that takes two integers as input and returns their sum. We then call this function from the Main method and pass in the values of a and b as arguments. The result of the function call is stored in a variable called result, which is then printed to the console using Console.WriteLine.
}
