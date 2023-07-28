"""
In Python, "super()" is a built-in function used primarily in the context of inheritance and object-oriented programming. It provides a way to call a method from the parent (or superclass) within a subclass. This allows the subclass to extend or override the behavior of the parent class while still utilizing its functionality.

The most common use of "super()" is in the constructor (__init__) of a subclass to ensure that the initialization of the parent class is executed before adding any additional attributes specific to the subclass.

Here's a typical example of how "super()" is used:
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}."

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of the parent class
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

child = Child("Alice", 5)
print(child.greet())  # Output: Hi, I'm Alice and I'm 5 years old.


"""
In this example, the "Child" class inherits from the "Parent" class. By calling super().__init__(name) inside the constructor of the "Child" class, it first calls the constructor of the "Parent" class to set the "name" attribute, and then it adds the "age" attribute specific to the "Child" class.

Using "super()" ensures that the base class is correctly initialized and that you can access its methods and attributes from the subclass. It provides a clean way to handle inheritance, especially when there are multiple levels of inheritance in the class hierarchy.
"""



# Example Code
import math

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass  # We will implement this method in the subclasses

    def display(self):
        return f"I am a {self.color} shape."

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def display(self):
        return f"I am a {self.color} rectangle with width {self.width} and height {self.height}."

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def display(self):
        return f"I am a {self.color} circle with radius {self.radius}."

# Test the classes
rectangle = Rectangle("blue", 5, 10)
circle = Circle("red", 7)

print(rectangle.display())
print(f"Area: {rectangle.area()}")

print(circle.display())
print(f"Area: {circle.area()}")

"""
In this example, the "Shape" class has a constructor that sets the "color" attribute. The subclasses, "Rectangle" and "Circle," use "super()" to call the constructor of the "Shape" class, ensuring that the "color" attribute is initialized correctly.

Each subclass also provides its own implementation of the "area()" method, which calculates the area specific to each shape. The "display()" method is overridden in each subclass to provide a more specific description of each shape.

By using "super()" to handle the initialization and inheritance, we can avoid code duplication and create a clean class hierarchy to represent different shapes.
"""