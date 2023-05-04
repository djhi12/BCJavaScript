# In Python, the any() function is a built-in function that takes an iterable (such as a list, tuple, or set) as its argument and returns True if at least one element in the iterable is truthy, and False otherwise.

numbers = [3, 7, 1, 8, 4, 6]

if any(num % 2 == 0 for num in numbers):
    print("The list contains at least one even number.")
else:
    print("The list does not contain any even numbers.")

# In this program, the any() function is used with a generator expression that checks if each number in the numbers list is even (i.e., divisible by 2). Since the list contains the even numbers 8, 4, and 6, the any() function returns True, and the program prints "The list contains at least one even number." If the list did not contain any even numbers, the any() function would return False, and the program would print "The list does not contain any even numbers."