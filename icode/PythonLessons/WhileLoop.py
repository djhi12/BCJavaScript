"""
In Python, a while loop is used to repeatedly execute a block of code as long as a particular condition is true.

"""

# Here is the basic syntax for a while loop:
"""
while condition:
    # code to execute while condition is true

"""

"""
The code inside the loop will continue to execute as long as the condition remains true. The condition is evaluated at the beginning of each iteration of the loop, so if the condition is initially false, the loop will not execute at all.

"""

# Here is an example of a while loop that prints the numbers from 1 to 5:
i = 1
while i <= 5:
    print(i)
    i += 1


# This will output:
"""
1
2
3
4
5

"""

# In this example, the loop starts with i equal to 1. The loop will continue to execute as long as i is less than or equal to 5. Inside the loop, the current value of i is printed, and then i is incremented by 1 using the += operator. This continues until i becomes 6, at which point the condition becomes false and the loop exits.



