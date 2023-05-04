import turtle

# Get the color and shape from the user
color = input("Enter a color: ")
shape = input("Enter a shape (circle, square, triangle): ")

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's color
t.color(color)

# Draw the shape
if shape == "circle":
    t.circle(50)
elif shape == "square":
    for i in range(4):
        t.forward(100)
        t.left(90)
elif shape == "triangle":
    for i in range(3):
        t.forward(100)
        t.left(120)

# Wait for the user to close the window
turtle.done()
