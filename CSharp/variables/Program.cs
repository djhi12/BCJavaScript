/*
    In C#, a variable is a named memory location used to store a value of a specific type.

    To declare a variable, you need to specify the variable's name and its data type, like this:
*/

// int age; // declares an integer variable named "age"


// You can also initialize the variable when you declare it, like this:
int age = 30; // declares and initializes the variable "age" with a value of 30
Console.WriteLine(age);


/*
    C# supports many different data types for variables, including:

    bool: a Boolean value (true or false)
    byte: an 8-bit unsigned integer
    short: a 16-bit signed integer
    int: a 32-bit signed integer
    long: a 64-bit signed integer
    float: a single-precision floating-point number
    double: a double-precision floating-point number
    decimal: a decimal number with higher precision than float or double
    char: a Unicode character
    string: a sequence of Unicode characters
*/

// Here's an example that declares and initializes variables of various types:
bool isTrue = true;
Console.WriteLine(isTrue);

// In C#, "byte" is a built-in value type that represents an unsigned 8-bit integer. It has a range of 0 to 255 and uses 1 byte of memory.
byte myByte = 255;
Console.WriteLine(myByte);

// 
short myShort = -32768;
Console.WriteLine(myShort);

int myInt = 123456789;
Console.WriteLine(myInt);

long myLong = 123456789012345;
Console.WriteLine(myLong);

float myFloat = 3.14f;
Console.WriteLine(myFloat);

double myDouble = 3.14159265358979;
Console.WriteLine(myDouble);

decimal myDecimal = 3.1415926535897932384626433832m;
Console.WriteLine(myDecimal);

char myChar = 'A';
Console.WriteLine(myChar);

string myString = "Hello, world!";
Console.WriteLine(myString);

