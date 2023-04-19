"""
Nested loops in Python are a way to iterate over a sequence or multiple sequences within another sequence. It allows you to iterate over the elements of an outer loop while also iterating over the elements of an inner loop. 

"""

# Here's an example:
"""
for i in range(3):
    for j in range(3):
        print(i, j)

"""

# In this example, the outer loop iterates over the values 0, 1, and 2 using the range function. For each of these values, the inner loop iterates over the same values using another range function.

# As a result, the output of this code is:
"""
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2

"""

# Note that the inner loop runs completely for each value of the outer loop. So, in this case, the inner loop runs 3 times for each iteration of the outer loop.

"""
Nested loops are often used when working with multidimensional data structures, such as matrices or arrays. They can also be used to generate all possible combinations of elements from two or more lists.

"""