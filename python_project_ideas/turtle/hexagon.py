import turtle
t = turtle.Turtle()
# Function to draw a hexagon
def draw_hexagon():
    for _ in range(6):
        t.forward(100)
        t.right(60)
        t.color("red")
        t.width(10)

# Set the speed of the turtle
t.speed(20)
draw_hexagon()