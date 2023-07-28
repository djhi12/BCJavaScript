"""
In Python, __init__() is a special method used in classes to initialize object attributes when an instance of the class is created. It is commonly referred to as the "constructor" method. When you create an object (an instance) of a class, Python automatically calls the __init__() method if it's defined within the class.

Here's the basic syntax of the __init__() method:

class MyClass:
    def __init__(self, param1, param2, ...):
        # Initialize object attributes here
        self.attribute1 = param1
        self.attribute2 = param2
        # ...

# Creating an instance of MyClass
my_instance = MyClass(value1, value2, ...)

"""

"""
Let's break down the code:

We define a class called MyClass.

Inside the class, we define the __init__() method, which takes self as its first parameter. self refers to the instance of the class being created.
Apart from self, the __init__() method can also take other parameters (param1, param2, ...) that you want to use to initialize the object's attributes.
Inside the __init__() method, we set the attributes of the object using the provided parameters. These attributes are specific to each instance of the class.

When you create an instance of the class (e.g., my_instance = MyClass(value1, value2, ...)), Python automatically calls the __init__() method with the provided values, and those values are used to initialize the attributes of the instance.

Here's an example:
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name, person1.age)  # Output: Alice 30
print(person2.name, person2.age)  # Output: Bob 25

"""
In this example, we define a Person class with an __init__() method that takes name and age as parameters. When we create instances of the Person class (person1 and person2), we pass the respective values for name and age, and the __init__() method initializes the attributes accordingly.
"""


# Example Program
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model} is now running.")

    def stop(self):
        self.is_running = False
        print(f"The {self.year} {self.make} {self.model} has been stopped.")

    def honk(self):
        if self.is_running:
            print("Beep! Beep!")
        else:
            print("The car must be running to honk.")

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Honda", "Civic", 2021, "Red")

# Starting and honking car1
car1.start()
car1.honk()

# Stopping car2
car2.start()
car2.stop()

"""
In this example, we have a Car class with an __init__() method that takes make, model, year, and color as parameters. The __init__() method initializes the object's attributes with the provided values.

We also have three other methods: start(), stop(), and honk(). These methods perform actions based on the state of the car (running or stopped). The start() method changes the is_running attribute to True, the stop() method changes it to False, and the honk() method checks if the car is running and makes the appropriate sound.

We then create two instances of the Car class (car1 and car2) and call the methods on these instances to see how the attributes and methods work together.
"""