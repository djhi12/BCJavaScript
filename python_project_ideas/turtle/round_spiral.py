import turtle

# Create a Turtle instance
t = turtle.Turtle()

# Set the initial radius and angle
radius = 10
angle = 91

# Draw the round spiral
for _ in range(100):
    t.circle(radius)
    t.right(angle)
    radius += 5

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.exitonclick()

"""
In this code, we start by importing the turtle module and creating a Turtle instance called t. We set the initial values for the radius and angle. The radius determines the distance from the turtle to the center of the circle, and the angle represents the angle at which the turtle turns.

We use a loop to draw the round spiral. In each iteration, the turtle moves in a circular path with the current radius using t.circle(radius). Then, we turn the turtle right by the specified angle using t.right(angle). After that, we increase the radius by a fixed amount to make the spiral gradually grow.

Once the loop is complete, we hide the turtle using t.hideturtle() so only the final spiral is visible. Finally, we use turtle.exitonclick() to keep the window open until we click on it.

You can run this code in a Python environment and observe the round spiral being drawn. Feel free to adjust the range value in the for loop or modify the angle to create different spiral shapes.
"""