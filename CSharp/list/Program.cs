using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        /*
            In C#, "using" is a keyword that is used for declaring a scope, within which an object or resource is used, and then it is disposed of automatically when the scope is exited.

            Lists are a commonly used data structure in C# for storing collections of items. When using lists, the "using" keyword is not typically used, as it is intended for objects that require explicit disposal, such as database connections or file streams.
        */

        // You can also access items in the list by their index, like so:
        // string secondItem = myList[1];

        // When you are finished using the list, you do not need to dispose of it explicitly; it will be automatically cleaned up by the garbage collector when it is no longer in use.


        // Example Program
        // Declare a new list of strings
        // Instead, when declaring a list in C#, you would typically do the following:
        List<string> myList = new List<string>();

        // Add some items to the list
        // This creates a new instance of a list of strings named "myList". You can then add items to the list using the "Add" method, like so:
        myList.Add("apple");
        myList.Add("banana");
        myList.Add("orange");

        // Print out the items in the list
        foreach (string item in myList)
        {
            Console.WriteLine(item);
        }

        // Get the index of an item in the list
        int index = myList.IndexOf("banana");
        Console.WriteLine("Index of 'banana': " + index);

        // Remove an item from the list
        myList.Remove("banana");

        // Print out the items in the list again
        foreach (string item in myList)
        {
            Console.WriteLine(item);
        }
    }
}
