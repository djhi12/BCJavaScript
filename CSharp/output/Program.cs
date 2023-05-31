namespace Output
{
    /*
        In C#, "output" refers to the process of sending data or results from a program to a specific destination, such as a console window or a file.

        The "output" keyword in C# is used in the context of a method or function to indicate that it returns a value to the calling code. For example, you can use the "output" keyword in a method signature to indicate that the method returns a value by reference, meaning that the value is assigned to a parameter passed to the method rather than being returned directly.
    */

    // Here is an example of a method that uses the "output" keyword:
    public void CalculateSumAndDifference(int a, int b, out int sum, out int difference)
    {
        /*
            In this method, the "out" keyword is used to indicate that the "sum" and "difference" variables are output parameters. This means that the method will assign values to these variables and return them to the calling code.

            You can call this method as follows:
        */
        sum = a + b;
        difference = a - b;

        int a = 5;
        int b = 3;
        int sum, difference;

        CalculateSumAndDifference(a, b, out sum, out difference);

        Console.WriteLine($"The sum is: {sum}");
        Console.WriteLine($"The difference is: {difference}");

        // In this example, the "out" keyword is used to pass the "sum" and "difference" variables to the "CalculateSumAndDifference" method. The method calculates the sum and difference of the two input integers and assigns the results to the "sum" and "difference" variables, respectively. The calling code then displays the results in the console window.
    }
}
