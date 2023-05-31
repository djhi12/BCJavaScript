/*
    In C#, "polymorphism" refers to the ability of an object to take on many forms or to have multiple behaviors depending on the context in which it is used. Specifically, polymorphism allows objects of different classes to be treated as if they are objects of a common base class, or interface, enabling greater flexibility and reuse in object-oriented programming.

    Polymorphism in C# can be achieved through method overriding, where a subclass provides its own implementation of a method already defined in its parent class, and through interface implementation, where a class provides its own implementation for the methods defined in an interface it implements. In both cases, a reference variable of the base class or interface type can be used to refer to an object of the subclass, enabling the object to be used interchangeably with other objects that share the same base class or interface.

    For example, suppose you have a base class called Animal and two subclasses called Dog and Cat. Both Dog and Cat are Animals, but they have their own unique behavior (such as bark() and meow() methods). By defining the Animal class with a method makeSound(), and having each subclass implement its own version of makeSound(), you can treat both Dog and Cat objects as Animals and call their makeSound() method through an Animal reference variable, even though the specific behavior of makeSound() will differ depending on whether the object is a Dog or a Cat. This is an example of polymorphism in action.
*/


// Example Program
using System;

public class Animal
{
    public virtual void makeSound()
    {
        Console.WriteLine("The animal makes a sound.");
    }
}

public class Dog : Animal
{
    public override void makeSound()
    {
        Console.WriteLine("The dog barks.");
    }
}

public class Cat : Animal
{
    public override void makeSound()
    {
        Console.WriteLine("The cat meows.");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Animal animal1 = new Dog();
        Animal animal2 = new Cat();

        animal1.makeSound(); // outputs "The dog barks."
        animal2.makeSound(); // outputs "The cat meows."
    }
}

/*
    In this program, we define the Animal base class with a makeSound() method that prints a generic message to the console. We then define two subclasses, Dog and Cat, that both override makeSound() with their own implementation that prints a specific message to the console.

    In the Main() method, we create two Animal objects, animal1 and animal2, and initialize them to be instances of the Dog and Cat classes, respectively. We then call the makeSound() method on each object using an Animal reference variable, demonstrating how we can treat the Dog and Cat objects as if they are both Animals and still get the appropriate behavior for each subclass. The output of the program shows that the makeSound() method of each object prints the appropriate message to the console based on its subclass.  
*/