import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle forward to draw the square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)  # Turn right by 90 degrees

# Close the turtle graphics window
turtle.done()

"""
This code will create a square using the Turtle module. The turtle starts at the default position, which is the center of the screen. It moves forward by 100 units and then turns right by 90 degrees. This process is repeated four times to complete the square. Finally, the turtle.done() function is called to keep the turtle graphics window open until it is closed by the user.

You can customize the code as per your requirements. For example, you can change the size of the square by modifying the value passed to the forward() function, or you can change the angle of rotation by modifying the value passed to the right() function.
"""