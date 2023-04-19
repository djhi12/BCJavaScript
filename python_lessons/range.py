"""
In Python, the "for i in range()" construct is a loop that iterates over a sequence of numbers. 
"""

# The basic syntax of this loop is:
"""
for i in range(start, stop, step):
    # code block

"""
# Here, start is the starting value of the loop (default value is 0), stop is the ending value (exclusive), and step is the amount by which the loop index increases on each iteration (default value is 1).


# For example, the following code block uses a for loop with range to print the numbers from 0 to 4:
for i in range(5):
    print(i)

# Output:
"""
0
1
2
3
4

"""


"""
You can also use range with different values of start, stop, and step to iterate over different sequences of numbers. 

"""

# For example:
for i in range(2, 10, 2):
    print(i)

# Output:
"""
2
4
6
8

"""

# This will iterate over the sequence of numbers 2, 4, 6, and 8 (i.e., starting from 2, ending at 10 (exclusive), and incrementing by 2 on each iteration).