# import turtle

# def draw_decagon():
#     window = turtle.Screen()
#     window.bgcolor("white")

#     pen = turtle.Turtle()
#     pen.color("black")
#     pen.speed(2)

#     side_length = 100  # Length of each side of the decagon

#     for _ in range(10):
#         pen.forward(side_length)
#         pen.right(36)  # 360 degrees divided by 10 sides

#     turtle.done()

# draw_decagon()


import turtle
import random

def draw_decagon():
    window = turtle.Screen()
    window.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(2)

    side_length = 100  # Length of each side of the decagon

    for _ in range(10):
        # Generate random RGB values for color
        red = random.random()
        green = random.random()
        blue = random.random()

        pen.color(red, green, blue)
        pen.forward(side_length)
        pen.right(36)  # 360 degrees divided by 10 sides

    turtle.done()

draw_decagon()
