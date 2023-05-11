"""
In Python, a dictionary is a collection of key-value pairs, also known as a hash map or associative array. It is an unordered and mutable data type that allows for fast lookup of values based on their associated keys.

To create a dictionary in Python, you can use curly braces {} or the dict() constructor. Here's an example:

"""

my_dict = {'apple': 3, 'banana': 5, 'cherry': 2}

# In this example, the keys are strings ('apple', 'banana', and 'cherry') and the values are integers (3, 5, and 2). You can access the values in the dictionary using their corresponding keys like this:

print(my_dict['banana'])  # Output: 5

# You can also add, remove, or update key-value pairs in the dictionary using the dictionary methods such as .update(), .pop(), .popitem(), and so on.

# Here's an example of adding a new key-value pair to the dictionary:

my_dict['orange'] = 4

# This adds a new key 'orange' with a value of 4 to the dictionary.


# Example Program
# Create a dictionary of fruits and their prices
fruit_prices = {'apple': 0.75, 'banana': 0.50, 'orange': 1.00}

# Print the price of an apple
print("The price of an apple is:", fruit_prices['apple'])

# Add a new fruit to the dictionary
fruit_prices['grape'] = 1.50

# Print all the fruits and their prices
for fruit, price in fruit_prices.items():
    print(fruit, "costs", price, "dollars")

"""
In this program, we create a dictionary called fruit_prices that maps the names of fruits to their prices. We then print the price of an apple using the key 'apple'.

Next, we add a new fruit 'grape' to the dictionary using the key-value assignment.

Finally, we loop through all the items in the dictionary using the .items() method and print out each fruit name and its corresponding price.
"""