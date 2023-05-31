/*
    In C#, "System.IO.File.ReadAllLines()" is a method that reads all the lines of a specified text file and returns them as an array of strings. The method takes a single argument, which is the path to the file to be read.
*/
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = @"C:\Programming_with_Classes\codes\ReadAllLines\sampleFile.txt";

        try
        {
            string[] lines = File.ReadAllLines(path);
            foreach (string line in lines)
            {
                Console.WriteLine(line);
            }
        }
        catch (Exception e)
        {
            Console.WriteLine("An error occurred: " + e.Message);
        }
    }
}

/*
    In this example, the code reads all the lines of the file located at "C:\example.txt" and then outputs each line to the console. If an error occurs during the file reading, the code catches the exception and outputs an error message instead.
*/
