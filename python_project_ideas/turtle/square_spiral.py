import turtle

# Create a Turtle instance
t = turtle.Turtle()

# Set the initial side length and angle
side_length = 10
angle = 90

# Draw the square spiral
for _ in range(50):  # Change the range value to adjust the spiral size
    t.forward(side_length)
    t.right(angle)
    side_length += 5  # Increase the side length for each iteration

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.exitonclick()


"""
In this code, we start by importing the turtle module and creating a Turtle instance called t. We then set the initial values for the side length and angle. The side length determines the length of each side of the square, and the angle represents the angle at which the turtle turns.

We use a loop to draw the square spiral. In each iteration, the turtle moves forward by the current side length and then turns right by the specified angle. After that, we increase the side length by a fixed amount to make the spiral gradually grow.

Once the loop is complete, we hide the turtle using t.hideturtle(), so only the final spiral is visible. Finally, we use turtle.exitonclick() to keep the window open until we click on it.

You can run this code in a Python environment and observe the square spiral being drawn. Feel free to adjust the range value in the for loop to change the size of the spiral.
"""