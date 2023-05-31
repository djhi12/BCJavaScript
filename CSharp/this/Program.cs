/*
    
In C#, the "this" keyword is a reference to the current instance of the class. It is commonly used to differentiate between class-level variables and local variables with the same name.

*/

using System;

class MyClass {
  private int myVar;

  public void SetMyVar(int value) {
    this.myVar = value; // use "this" to refer to the class-level variable
  }

  public void PrintMyVar() {
    Console.WriteLine("MyVar = " + this.myVar); // use "this" to refer to the class-level variable
  }
}

class Program {
  static void Main() {
    MyClass obj = new MyClass();
    obj.SetMyVar(42);
    obj.PrintMyVar();
  }
}

/*
    In this program, we define a class called MyClass that has a private class-level variable myVar. The class also has two methods: SetMyVar to set the value of myVar, and PrintMyVar to print the value of myVar.

    In the SetMyVar method, we use the "this" keyword to refer to the class-level variable myVar and set its value to the input parameter value. In the PrintMyVar method, we also use the "this" keyword to refer to the class-level variable myVar and print its value to the console.

    In the Main method, we create an instance of MyClass and call SetMyVar to set the value of myVar to 42. Then, we call PrintMyVar to print the value of myVar to the console. The output of this program should be:
*/