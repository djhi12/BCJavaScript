/*
    In C#, "object" is a class that serves as the base class for all other classes in the .NET Framework. It is defined in the System namespace and provides a common set of methods and properties that are inherited by all other classes.

    The "object" class defines several important methods that are used throughout C# programming. These include the ToString method, which returns a string representation of the object, and the Equals method, which is used to compare two objects for equality.

    Because all classes in C# ultimately derive from the "object" class, you can use any object as an argument to a method or as the return value of a method. This makes it possible to create methods that can accept any type of object as input, which can be useful in certain situations.

    In addition to providing a common set of methods and properties, the "object" class also provides a way to box value types, such as integers or floats, so that they can be treated as objects. This is important when working with interfaces or other scenarios where an object is expected, but a value type needs to be passed in.

    Overall, the "object" class is a fundamental part of C# programming and is used extensively throughout the .NET Framework.
*/

using System;

public class Program
{
    public static void Main()
    {
        object obj1 = new object(); // create a new object
        object obj2 = new object();

        Console.WriteLine(obj1.ToString()); // call the ToString method on obj1
        Console.WriteLine(obj1.Equals(obj2)); // call the Equals method on obj1 to compare with obj2

        int num = 5; // create a value type
        object boxedNum = num; // box the value type in an object

        Console.WriteLine(boxedNum.GetType()); // call the GetType method on boxedNum to get its type
    }
}
