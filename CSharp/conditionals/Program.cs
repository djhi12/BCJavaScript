using System;

class Program
{
    static void Main(string[] args)
    {
        /*
            In C#, conditionals are statements that allow the program to make decisions based on a specific condition. There are several types of conditional statements in C#:
        */

        int x = 10;
        int y = 5;


        // If statement: This is the most basic conditional statement in C#. It allows the program to execute a certain block of code only if a specified condition is true. The syntax for an if statement is as follows:
        if (x > y)
        {
            Console.WriteLine("x is greater than y");
        }


        // If-else statement: This statement is used when there are two possible outcomes based on a condition. If the condition is true, the code inside the if block is executed. If the condition is false, the code inside the else block is executed. The syntax for an if-else statement is as follows:
        if (x < y)
        {
            Console.WriteLine("x is less than y");
        }
        else
        {
            Console.WriteLine("x is greater than or equal to y");
        }


        // If-else if-else statement: This statement is used when there are multiple possible outcomes based on different conditions. It allows the program to check multiple conditions and execute different code blocks depending on which condition is true. The syntax for an if-else if-else statement is as follows:
        if (x < y)
        {
            Console.WriteLine("x is less than y");
        }
        else if (x > y)
        {
            Console.WriteLine("x is greater than y");
        }
        else
        {
            Console.WriteLine("x is equal to y");
        }


        // Switch statement: This statement is used when there are multiple possible outcomes based on the value of a variable. It allows the program to check the value of a variable and execute different code blocks depending on its value. The syntax for a switch statement is as follows:
        switch (x)
        {
            case 5:
                Console.WriteLine("x is 5");
                break;
            case 10:
                Console.WriteLine("x is 10");
                break;
            default:
                Console.WriteLine("x is not 5 or 10");
                break;
        }
    }

    // In all of these conditional statements, the condition must evaluate to a boolean value (true or false).
}
