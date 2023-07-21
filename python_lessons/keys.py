"""
In Python, the keys() method is a built-in function that returns a view object that contains the keys of a dictionary. The view object represents a dynamic view of the dictionary's keys, which means that if the dictionary changes, the view object will reflect those changes.

Here's the syntax for using the keys() method:

dictionary.keys()

"""


# The dictionary is the dictionary object for which you want to retrieve the keys.
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()

print(keys)


# In Python 3.x, keys() returns a view object, which is similar to a set. However, you can convert it to other data types if needed. For example, you can convert it to a list:
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = list(my_dict.keys())

print(keys)

# You can iterate over the keys or perform other operations on the view object, just like you would with a list or a set. Keep in mind that the order of the keys in the view object is arbitrary and not necessarily the same as the order in which they were inserted into the dictionary.


# Example Program
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

# Retrieve the keys using keys() method
keys = my_dict.keys()

# Convert the keys to a list
key_list = list(keys)

# Print the keys
print("Keys:", key_list)

# Iterate over the keys and print their corresponding values
for key in keys:
    value = my_dict[key]
    print(key, "->", value)

"""
In this example, we have a dictionary my_dict with fruit names as keys and their corresponding quantities as values. We use the keys() method to retrieve a view object representing the keys of the dictionary. We convert the view object to a list using list() so that we can print the keys and iterate over them.

Then, we iterate over the keys using a for loop and retrieve the corresponding values from the dictionary using the keys. We print each key along with its value.

Note that the order of the keys in the output may vary as dictionaries in Python do not maintain any specific order by default.
"""