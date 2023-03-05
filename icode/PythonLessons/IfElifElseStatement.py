"""
In Python, the If, Elif, and Else statements are used for conditional branching. Conditional statements are used when you want to execute certain code only if a certain condition is met.

"""

# Here is the syntax for the If, Elif, and Else statements:
"""
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if neither condition1 nor condition2 is True
"""


"""
Here, condition1 and condition2 are the conditions that you want to test. If condition1 is True, the code block following the If statement will be executed. If condition1 is False, then condition2 will be tested. If condition2 is True, the code block following the Elif statement will be executed. If both condition1 and condition2 are False, then the code block following the Else statement will be executed.

Note that the Elif statement is optional, and you can have multiple Elif statements to test multiple conditions. However, you can only have one If and one Else statement per block.

"""

# Here's an example to illustrate the use of If, Elif, and Else statements:
age = 20

if age < 18:
    print("You are not old enough to vote.")
elif age >= 18 and age < 21:
    print("You can vote but you cannot drink.")
else:
    print("You can vote and drink.")

# In this example, the code checks the value of the age variable. If age is less than 18, the message "You are not old enough to vote." will be printed. If age is between 18 and 21 (inclusive), the message "You can vote but you cannot drink." will be printed. If age is greater than or equal to 21, the message "You can vote and drink." will be printed.



