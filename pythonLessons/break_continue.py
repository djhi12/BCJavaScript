"""
In Python, break and continue are control statements that can be used within loops to alter their flow.

break is used to exit a loop prematurely, regardless of whether the loop condition has been satisfied or not. When the break statement is encountered, the loop terminates immediately and the program control moves to the statement immediately following the loop.

"""

# Here is an example of using break in a while loop:
while True:
    user_input = input("Enter a value ('q' to quit): ")
    if user_input == 'q':
        break
    print(f"You entered: {user_input}")

# In this code, the loop will continue to run until the user enters the value "q". When that happens, the break statement is executed and the loop is exited.


"""
On the other hand, continue is used to skip a particular iteration of the loop and move to the next iteration. When the continue statement is encountered, the current iteration of the loop is terminated immediately and the program control moves to the next iteration.

"""

# Here is an example of using continue in a for loop:
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# In this code, the loop will iterate through the numbers 1 to 10. However, when i is even, the continue statement is executed, and the current iteration is skipped. The program control moves to the next iteration, and the code after the continue statement is not executed.