import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to the starting position
t.penup()
t.goto(0, -100)  # Adjust the y-coordinate as needed
t.pendown()

# Draw a circle
radius = 100  # Adjust the radius as needed
t.circle(radius)

# Close the turtle graphics window
turtle.done()

"""
In the code above, the turtle object is created and then moved to the starting position for drawing the circle. The penup() function lifts the turtle's pen off the drawing surface, and pendown() puts it back down to start drawing. The goto() function is used to position the turtle at the center of the circle. Adjust the coordinates as needed to change the position of the circle.

The circle() function is used to draw the circle. The argument passed to it specifies the radius of the circle. Adjust the radius variable to change the size of the circle.

Finally, the turtle.done() function is called to keep the turtle graphics window open until it is closed by the user.

You can modify the code to suit your requirements, such as changing the position or size of the circle.
"""