"""
    In Python, "dot notation" is a way of accessing attributes or methods of an object. It involves using a dot "." followed by the name of the attribute or method that you want to access.

    For example, if you have a variable my_list that is a list object, you can use dot notation to access its methods, such as append() or pop().
"""
my_list = [1, 2, 3]
my_list.append(4)
my_list.pop()

# In this example, the append() and pop() methods are accessed using dot notation, as they are methods of the list object.


# Similarly, if you have a class Person with attributes name and age, you can use dot notation to access these attributes of an instance of the class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
print(person1.name)
print(person1.age)

# In this example, the name and age attributes of person1 are accessed using dot notation.