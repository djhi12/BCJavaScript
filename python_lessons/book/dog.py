class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
    
    def print_info(self):
        """Print the name and age of the dog."""
        print(f"Dog's name: {self.name}, Age: {self.age}")


# Creating a Dog object
my_dog = Dog("Buddy", 3)

# Calling the print_info method to print the input values
my_dog.print_info()
