"""
In Python, the split() method is used to split a string into a list of substrings based on a specified delimiter. The split() method is available for strings and returns a list of substrings.

Here's the basic syntax of the split() method:

string.split(separator, maxsplit)

"""

"""
The split() method takes two optional parameters:

separator (optional): Specifies the delimiter to use for splitting the string. If the separator is not provided, whitespace (spaces, tabs, and newlines) is used as the default delimiter.

maxsplit (optional): Specifies the maximum number of splits to be done. If the maxsplit parameter is not provided, all possible splits are made.

Here are a few examples to demonstrate the usage of the split() method:

Example 1: Splitting a string using whitespace as the delimiter (default)
"""

text = "Hello, world! This is an example."
words = text.split()  # Split the string into words using whitespace as delimiter
print(words)


# Example 2: Splitting a string using a specified delimiter
text = "apple,banana,orange"
fruits = text.split(",")  # Split the string into fruits using comma as delimiter
print(fruits)


# Example 3: Limiting the number of splits
text = "one, two, three, four, five"
parts = text.split(", ", 2)  # Split the string into 3 parts using comma and space as delimiter, maximum of 2 splits
print(parts)

# In the above examples, the split() method is used to split the strings into substrings based on the specified delimiter. The result is a list containing the substrings obtained from the split operation.


# Example Program
def split_string(text):
    words = text.split()  # Split the string into words using whitespace as delimiter
    return words

# Example usage
sentence = "I love coding in Python"
result = split_string(sentence)
print(result)

"""
In this example, we define a function split_string() that takes a string as input. Inside the function, we use the split() method to split the input string into words using whitespace as the delimiter. The resulting list of words is then returned.

We then create a sample sentence, "I love coding in Python," and pass it to the split_string() function. The returned result is a list of words ['I', 'love', 'coding', 'in', 'Python'], which is printed to the console.

You can modify the split_string() function or the input sentence to experiment with different scenarios and understand how the split() method works in Python.
"""