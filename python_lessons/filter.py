"""
    In Python, filter() is a built-in function that takes two arguments: a function and an iterable (such as a list, tuple, or set), and returns an iterator containing the elements from the iterable for which the function returns True.
"""

# The syntax for filter() is as follows:
# filter(function, iterable)

"""
    Here, function is a function that takes one argument and returns a Boolean value (i.e., True or False), and iterable is the iterable that we want to filter.

    The filter() function applies the given function to each element of the iterable and returns only those elements for which the function returns True. The returned object is an iterator, so you can use it in a for loop, or you can convert it to a list using the list() function.
"""


# Here's an example that uses filter() to return only the even numbers from a list of integers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(n):
    return n % 2 == 0


even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# In this example, the is_even() function takes an integer n as an argument and returns True if n is even, and False otherwise. We pass this function and the numbers list to filter(), which returns an iterator containing only the even numbers from the list. Finally, we convert the iterator to a list and print it.


# Example Program
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(is_prime, numbers))

print(prime_numbers)  # Output: [2, 3, 5, 7]

"""
    In this program, the is_prime() function takes an integer n as an argument and returns True if n is a prime number, and False otherwise. We use this function and the numbers list as arguments to filter(), which returns an iterator containing only the prime numbers from the list. Finally, we convert the iterator to a list and print it.

    Note that the is_prime() function uses a simple algorithm to check whether a number is prime: it checks all the integers from 2 to the square root of the number, and returns False if any of them divide the number evenly. This is not the most efficient algorithm for finding primes, but it works well for small numbers.
"""