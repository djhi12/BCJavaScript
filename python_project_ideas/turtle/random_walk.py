import turtle
import random

# Create a Turtle instance
t = turtle.Turtle()

# Set the initial position
start_x = 0
start_y = 0
t.penup()
t.goto(start_x, start_y)
t.pendown()

# Set up colors
colors = ["red", "blue", "green", "purple", "orange", "yellow"]

# Simulate the random walk
num_steps = 100  # Change the number of steps for the random walk

for _ in range(num_steps):
    # Generate a random angle between 0 and 360 degrees
    angle = random.randint(0, 360)

    # Generate a random distance between 10 and 50 pixels
    distance = random.randint(10, 50)

    # Generate a random color from the list
    color = random.choice(colors)

    # Set the pen color
    t.pencolor(color)

    # Move in the random direction
    t.setheading(angle)
    t.forward(distance)

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.exitonclick()
