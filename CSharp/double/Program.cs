/*
    In C#, "double" is a data type that represents a double-precision floating-point number. It is a 64-bit numeric type that can represent values with a greater range and higher precision than the "float" data type, which is a single-precision floating-point number.

    The "double" data type is typically used for numerical calculations that require greater precision than what can be provided by "float" values. Double-precision floating-point numbers can represent a wide range of values, from approximately 4.9e-324 to 1.8e+308, with a precision of approximately 15 to 17 significant digits.
*/

// You can perform mathematical operations on "double" values, including addition, subtraction, multiplication, and division. It's important to keep in mind that due to the nature of floating-point arithmetic, some operations may not yield the exact result you expect, especially when dealing with very small or very large values.

using System;

class Program
{
    static void Main()
    {
        double radius = 2.5;
        double pi = Math.PI;
        double area = pi * radius * radius;
        double circumference = 2 * pi * radius;

        Console.WriteLine("Radius: {0}", radius);
        Console.WriteLine("PI: {0}", pi);
        Console.WriteLine("Area: {0}", area);
        Console.WriteLine("Circumference: {0}", circumference);
    }
}

/*
    This program calculates and displays the area and circumference of a circle with a given radius. The "radius", "pi", "area", and "circumference" variables are all declared as "double" values.

    The "Math.PI" constant is used to retrieve the value of pi to use in the calculations. The program then calculates the area and circumference of the circle using the standard formulas, and outputs the results to the console.
*/
