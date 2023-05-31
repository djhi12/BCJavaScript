/*
    In C#, the term "instantiate" refers to the process of creating an object of a class. When you instantiate an object, you are essentially creating a new instance of that class, which can then be used to access the properties and methods defined within the class.

    To instantiate an object in C#, you first need to define a class that you want to create an instance of. Once you have defined your class, you can create a new instance of it using the new keyword, followed by the name of the class.

    For example, if you had a class called Person with properties for Name and Age, you could create a new instance of that class like this:

    Person myPerson = new Person();

*/

using System;

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public void SayHello()
    {
        Console.WriteLine("Hello, my name is " + Name + " and I am " + Age + " years old.");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Person john = new Person();
        john.Name = "John";
        john.Age = 30;
        john.SayHello();

        Person sarah = new Person();
        sarah.Name = "Sarah";
        sarah.Age = 25;
        sarah.SayHello();
    }
}

/*
    In this example program, we define a Person class with two properties (Name and Age) and a method (SayHello) that prints a greeting message to the console.

    In the Main method, we instantiate two Person objects (john and sarah) using the new keyword and assign values to their properties (Name and Age). We then call the SayHello method on each object to print a greeting message to the console.

    When you run this program, it should output:

    Hello, my name is John and I am 30 years old.
    Hello, my name is Sarah and I am 25 years old.

*/