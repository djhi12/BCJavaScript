import turtle

# Create a turtle screen
screen = turtle.Screen()

# Set the screen size and background color
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()

# Set the turtle shape and speed
t.shape("turtle")
t.speed(5)

# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

# Move the turtle to a new location
t.penup()
t.goto(0, -50)
t.pendown()

# Draw a circle
t.circle(50)

# Close the turtle window when clicked
screen.exitonclick()
