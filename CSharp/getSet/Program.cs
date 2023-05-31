/*
    In C#, "{ get; set; }" is a shorthand notation for defining a property in a class.

    The "get" accessor is used to retrieve the value of the property, and the "set" accessor is used to assign a new value to the property.


    For example, consider the following code:

    public class Person
    {
        public string Name { get; set; }
    }

    Here, the "Name" property of the "Person" class can be accessed and modified using the "get" and "set" accessors respectively, as shown in the following code:

    Person person = new Person();
    person.Name = "John"; // set the value of the Name property
    string name = person.Name; // get the value of the Name property


    This shorthand notation allows developers to quickly define properties in a concise and readable way, without having to write out the full property definition with separate getter and setter methods.

*/

using System;

public class Person
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
        Console.WriteLine("Name: {0}", person.Name);
        Console.WriteLine("Age: {0}", person.Age);
    }
}

/*
    In this program, we define a class called "Person" with two properties: "Name" and "Age". These properties are defined using the "{ get; set; }" shorthand notation.

    In the "Main" method, we create a new instance of the "Person" class and set the values of the "Name" and "Age" properties. We then use the Console.WriteLine method to output the values of these properties to the console.
*/
