import turtle

def draw_trapezium(base, top, height):
    turtle.forward(base)
    turtle.right(135)
    turtle.forward(height)
    turtle.right(45)
    turtle.forward(top)
    turtle.right(45)
    turtle.forward(height)
    turtle.right(135)
    turtle.forward(base)

# Create a turtle screen
screen = turtle.Screen()

# Set up the turtle
turtle.speed(1)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

# Draw a trapezium
draw_trapezium(200, 100, 150)

# Close the turtle graphics window
turtle.done()

