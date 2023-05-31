/*
    In C#, "abstraction" refers to the concept of hiding implementation details and exposing only the essential features of a program. Abstraction is achieved through the use of abstract classes and interfaces.

    An abstract class is a class that cannot be instantiated on its own, but can only be used as a base class for other classes. It may contain abstract methods, which have no implementation in the abstract class itself but must be implemented in derived classes. By providing an abstract class with abstract methods, you can define a set of methods that derived classes must implement in order to provide their own implementation.

    An interface is similar to an abstract class in that it defines a set of methods and properties that implementing classes must provide. However, an interface cannot contain any implementation details, only method and property signatures. A class can implement multiple interfaces, but can only inherit from one base class.

    Abstraction is a key concept in object-oriented programming, as it allows you to create classes and interfaces that can be used in a variety of contexts without exposing implementation details. This makes code more flexible, easier to maintain, and less prone to errors caused by unexpected changes to implementation details.
*/


// Example Program
using System;

// Define an interface for a shape
interface IShape
{
    double GetArea();
    double GetPerimeter();
}

// Define an abstract class for a shape
abstract class Shape : IShape
{
    public abstract double GetArea();
    public abstract double GetPerimeter();
}

// Define a concrete class for a rectangle
class Rectangle : Shape
{
    private double _width;
    private double _height;

    public Rectangle(double width, double height)
    {
        _width = width;
        _height = height;
    }

    public override double GetArea()
    {
        return _width * _height;
    }

    public override double GetPerimeter()
    {
        return 2 * (_width + _height);
    }
}

// Define a concrete class for a circle
class Circle : Shape
{
    private double _radius;

    public Circle(double radius)
    {
        _radius = radius;
    }

    public override double GetArea()
    {
        return Math.PI * _radius * _radius;
    }

    public override double GetPerimeter()
    {
        return 2 * Math.PI * _radius;
    }
}

// Main program
class Program
{
    static void Main(string[] args)
    {
        // Create a rectangle
        Rectangle rect = new Rectangle(5, 10);
        Console.WriteLine($"Rectangle area: {rect.GetArea()}");
        Console.WriteLine($"Rectangle perimeter: {rect.GetPerimeter()}");

        // Create a circle
        Circle circle = new Circle(5);
        Console.WriteLine($"Circle area: {circle.GetArea()}");
        Console.WriteLine($"Circle circumference: {circle.GetPerimeter()}");
    }
}


/*
    In this program, we define an interface IShape that defines two methods: GetArea() and GetPerimeter(). We then define an abstract class Shape that implements the IShape interface and declares the same two methods as abstract, which means that any derived class must implement these methods.

    We then define two concrete classes Rectangle and Circle that inherit from Shape and provide their own implementations of the GetArea() and GetPerimeter() methods.

    In the Main() method, we create instances of Rectangle and Circle and call their GetArea() and GetPerimeter() methods. The fact that we can call these methods on objects of different classes that implement the same interface demonstrates the power of abstraction in allowing us to work with different types of objects in a generic way.
*/