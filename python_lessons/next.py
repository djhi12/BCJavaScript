"""
In Python, the next() function is used to retrieve the next item from an iterator. It is commonly used in conjunction with the built-in iter() function to create an iterator object and then retrieve elements from it one by one.

The basic syntax of the next() function is as follows:

next(iterator[, default])

"""


"""
Here, the iterator parameter is an object that implements the iterator protocol. It can be a list, tuple, string, or any other iterable object. The default parameter is optional and is used to specify a default value that should be returned if the iterator is exhausted.

When you call next(iterator), it advances the iterator and returns the next item. If the iterator is already exhausted and there are no more items, it raises the StopIteration exception. If you provide a default value, it will be returned instead of raising an exception.

Here's an example that demonstrates the use of next():
"""

my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
print(next(my_iterator))  # Output: 4
print(next(my_iterator))  # Output: 5
print(next(my_iterator, "End"))  # Output: "End" (iterator exhausted)

"""
In this example, we create an iterator my_iterator from a list my_list. We call next() multiple times to retrieve each item from the iterator until it is exhausted. Finally, we provide a default value "End" in the last next() call to handle the case when the iterator is exhausted.

Note that once an iterator is exhausted, calling next() on it again will continue to raise the StopIteration exception unless a default value is provided.
"""


# Example Program
numbers = [1, 2, 3, 4, 5]
my_iterator = iter(numbers)

while True:
    try:
        next_number = next(my_iterator)
        print(next_number)
    except StopIteration:
        print("Iterator is exhausted.")
        break

"""
In this program, we have a list of numbers [1, 2, 3, 4, 5]. We create an iterator my_iterator using the iter() function.

We use a while loop to iterate over the items in the iterator. Inside the loop, we call next(my_iterator) to retrieve the next number from the iterator and store it in the next_number variable.

If the iterator is not yet exhausted, we print the value of next_number. If the iterator is exhausted and there are no more items, the StopIteration exception is raised. We catch this exception using a try-except block and print a message indicating that the iterator is exhausted. Then we break out of the loop to exit the program.
"""