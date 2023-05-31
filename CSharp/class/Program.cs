using System;

// Define a new class called "Person"
class Person
{
    // Define some properties for the Person class
    public string Name { get; set; }
    public int Age { get; set; }

    // Define a constructor for the Person class
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    // Define a method for the Person class
    public void Greet()
    {
        Console.WriteLine($"Hello, my name is {Name} and I am {Age} years old.");
    }
}

// Define the main program
class Program
{
    static void Main(string[] args)
    {
        // Create a new instance of the Person class
        Person person = new Person("Alice", 25);

        // Call the Greet method on the person object
        person.Greet();
    }
}
