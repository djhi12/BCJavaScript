# Function to draw a pentagon
import turtle

# Create a turtle object
t = turtle.Turtle()

def draw_pentagon():
    for _ in range(5):
        t.forward(100)
        t.right(72)
        
draw_pentagon()

turtle.done()