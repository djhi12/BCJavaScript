/*
    In C#, an "instance" refers to a specific occurrence of a class. When a class is defined, it serves as a blueprint for creating objects or instances of that class. Each instance of a class has its own set of data, which is distinct from the data of other instances of the same class.

    For example, suppose you have a class called "Person" with properties such as "Name" and "Age". You can create multiple instances of the "Person" class, each with its own unique values for the "Name" and "Age" properties. These instances are separate from each other, and any changes made to one instance will not affect the others.
*/

// In C#, you create an instance of a class by using the "new" keyword followed by the name of the class. For example:

// Person person1 = new Person();
// Person person2 = new Person();


using System;

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}

class Program
{
    static void Main(string[] args)
    {
        Person person = new Person();
        person.Name = "John";
        person.Age = 30;

        Console.WriteLine("Name: " + person.Name);
        Console.WriteLine("Age: " + person.Age);
    }
}

/*
    In this program, we define a class called "Person" with two properties: "Name" and "Age". We then create an instance of this class by using the "new" keyword, and set the "Name" and "Age" properties of this instance.
*/