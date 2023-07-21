"""
In Python, **kwargs is a special syntax used in function definitions to allow a function to accept an arbitrary number of keyword arguments. The term "kwargs" stands for "keyword arguments." While *args is used to pass a variable number of non-keyword arguments (positional arguments), **kwargs allows passing a variable number of keyword arguments (named arguments).

Here's how **kwargs works:

Definition: When defining a function, you can use **kwargs as one of the parameters. It collects all the keyword arguments passed to the function as a dictionary.

Passing keyword arguments: When calling the function, you can pass any number of keyword arguments, and they will be collected into the **kwargs dictionary.

Accessing keyword arguments: Inside the function, you can access the keyword arguments as you would with a regular dictionary, using the keys to retrieve their corresponding values.

Let's see an example:
"""
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Calling the function with different keyword arguments
example_function(name="John", age=30)
example_function(city="New York", country="USA", occupation="Engineer")

"""
In the example above, **kwargs collects all the keyword arguments passed to the example_function() and then iterates over them to print their keys and values.

It's important to note that when defining a function, the **kwargs parameter must come after all other positional and keyword parameters. The order of arguments is essential in Python function definitions.

Using **kwargs can be helpful when you want to create flexible functions that can accept additional parameters without having to explicitly define them in the function signature. However, you should use it judiciously to ensure code clarity and maintainability.
"""


# Example Program
def display_info(**kwargs):
    print("Personal Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage of the function with different keyword arguments
display_info(name="John Doe", age=35, city="New York", occupation="Software Engineer")
display_info(name="Jane Smith", age=28, city="San Francisco", occupation="Data Scientist", hobbies=["Reading", "Traveling"])

"""
In the example above, we defined the display_info() function to accept any number of keyword arguments using **kwargs. The function then prints out each key-value pair from the provided keyword arguments, displaying the personal information passed to it.

In the first call, we provided four keyword arguments: name, age, city, and occupation. In the second call, we added a list of hobbies as an additional keyword argument.

The use of **kwargs allows us to create a flexible function that can handle different sets of personal information without explicitly defining each attribute in the function signature.
"""