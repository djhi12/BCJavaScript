/*
    In C#, inheritance is a fundamental object-oriented programming concept that allows you to create a new class based on an existing class, known as the base or parent class. The new class is called the derived or child class. The child class inherits all the properties, methods, and events of the parent class and can also add its own unique features.

    To create a derived class in C#, you use the colon symbol followed by the name of the base class. \

    Inheritance allows you to reuse code, making it easier to maintain and modify your programs. For example, you can create a base class that contains common functionality and then create several derived classes that inherit that functionality and add their own unique features. Inheritance also enables you to create a hierarchy of classes that share common properties and behaviors.

    However, inheritance should be used judiciously, as overuse can result in tightly coupled code that is difficult to maintain. Additionally, inheritance can lead to the "fragile base class problem," where changes to the base class can have unintended consequences for derived classes. Therefore, it's important to design your class hierarchy carefully and use inheritance only when it makes sense.
*/

using System;

// Parent class
class Animal
{
    // Properties
    public string Name { get; set; }
    public int Age { get; set; }

    // Method
    public void Eat()
    {
        Console.WriteLine("I am eating.");
    }
}

// Child class
class Dog : Animal
{
    // Method
    public void Bark()
    {
        Console.WriteLine("Woof!");
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Create a new Dog object
        Dog myDog = new Dog();
        myDog.Name = "Max";
        myDog.Age = 2;

        // Call methods from parent and child classes
        Console.WriteLine("My dog's name is {0} and he is {1} years old.", myDog.Name, myDog.Age);
        myDog.Eat();
        myDog.Bark();

        Console.ReadLine();
    }
}
