"""
In Python, the values() method is a built-in function that returns a view object that contains the values of a dictionary. The view object provides a dynamic view of the dictionary's values, which means that any changes made to the dictionary will be reflected in the view object, and vice versa.

Here's the syntax of the values() method:

dictionary.values()

"""


"""
The values() method doesn't take any arguments. When called on a dictionary, it returns a view object that represents the dictionary's values.

Here's an example that demonstrates the usage of the values() method:
"""
fruits = {'apple': 3, 'banana': 5, 'orange': 2}

fruit_values = fruits.values()

print(fruit_values)  # Outputs: dict_values([3, 5, 2])

# Modifying the dictionary
fruits['banana'] = 10

print(fruit_values)  # Outputs: dict_values([3, 10, 2])

# Iterating over the values
for value in fruit_values:
    print(value)

# Outputs:
# 3
# 10
# 2

"""
In the example, we have a dictionary fruits that represents the quantity of each fruit. We call the values() method on the fruits dictionary, which returns a view object fruit_values. We can iterate over this view object or access individual values. Any changes made to the fruits dictionary will be reflected in the view object fruit_values.

Note that the view object returned by values() is not a regular list or tuple, but it can be converted to one using the list() or tuple() functions if needed.
"""


# Example Program
def count_occurrences(values):
    occurrences = {}

    for value in values:
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1

    return occurrences

# Sample data
data = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]

# Counting occurrences using values() method
occurrences = count_occurrences(data)

# Printing the counts
for value, count in occurrences.items():
    print(f"{value}: {count} occurrences")

"""
In this program, we define a function count_occurrences() that takes a list of values as input. Inside the function, we create an empty dictionary occurrences to store the counts of each value.

We then iterate over the values using a for loop. For each value, we check if it exists as a key in the occurrences dictionary. If it does, we increment the count by 1. Otherwise, we add the value as a key in the dictionary and set the count to 1.

Finally, we call the count_occurrences() function with a sample list of values (data). The function returns a dictionary containing the counts of each value. We then iterate over the dictionary and print the values and their respective counts.

This program demonstrates the use of the values() method indirectly through the dictionary iteration. The values() method is not explicitly called in this example, but it provides a view object of the dictionary's values when we iterate over the dictionary using occurrences.values().
"""