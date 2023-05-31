/*
    To show a random prompt in C#, you can create an array or a list of prompts and use the Random class to generate a random index that corresponds to one of the prompts.
*/
using System;

class Program
{
    static void Main(string[] args)
    {
        string[] prompts = { "What's your favorite color?", "What's your favorite food?", "What's your favorite animal?" };

        Random random = new Random();
        int index = random.Next(prompts.Length);

        Console.WriteLine(prompts[index]);
    }
}
