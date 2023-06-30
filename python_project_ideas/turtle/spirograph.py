import turtle

def draw_spirograph(R, r, d):
    turtle.speed(0)
    turtle.bgcolor("black")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    for i in range(0, 360, 5):
        turtle.color(colors[i % len(colors)])
        turtle.setheading(i)
        x = (R - r) * turtle.cos(turtle.radians(i)) + d * turtle.cos(turtle.radians((R - r) / r * i))
        y = (R - r) * turtle.sin(turtle.radians(i)) - d * turtle.sin(turtle.radians((R - r) / r * i))
        turtle.goto(x, y)

draw_spirograph(100, 50, 75)
turtle.done()
