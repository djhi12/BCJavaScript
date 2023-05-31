/*
    In C#, a namespace is a way of organizing and grouping related classes, interfaces, structures, enums, and delegates together. It provides a way to avoid naming conflicts between types by creating a unique identifier for each type.
*/
using System;

namespace MyNamespace
{
    class MyClass
    {
        public void MyMethod()
        {
            Console.WriteLine("Hello from MyNamespace!");
        }
    }
}


namespace MyOtherNamespace
{
    class MyOtherClass
    {
        public void MyOtherMethod()
        {
            Console.WriteLine("Hello from MyOtherNamespace!");
        }
    }
}


class Program
{
    static void Main(string[] args)
    {

        MyNamespace.MyClass myObj = new MyNamespace.MyClass();
        myObj.MyMethod();


        MyOtherNamespace.MyOtherClass myOtherObj = new MyOtherNamespace.MyOtherClass();
        myOtherObj.MyOtherMethod();

        Console.ReadKey();
    }
}

/*
    In this program, we define two namespaces: MyNamespace and MyOtherNamespace. Each namespace contains a class with a method that writes a message to the console.

    In the Main method, we create instances of the classes from each namespace and call their methods. We use the namespace name to qualify the class names to avoid naming conflicts.
*/
