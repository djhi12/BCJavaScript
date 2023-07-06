import turtle

# Create a Turtle instance
t = turtle.Turtle()

# Set the initial parameters
length = 100  # Length of the main branch
levels = 4    # Number of levels or branches

# Function to draw a branch
def draw_branch(branch_length, levels):
    if levels == 0:
        t.forward(branch_length)
        return

    branch_length /= 3.0

    draw_branch(branch_length, levels - 1)
    t.left(60)
    draw_branch(branch_length, levels - 1)
    t.right(120)
    draw_branch(branch_length, levels - 1)
    t.left(60)
    draw_branch(branch_length, levels - 1)

# Function to draw a snowflake
def draw_snowflake(branch_length, levels):
    for _ in range(6):
        draw_branch(branch_length, levels)
        t.right(60)

# Set up the turtle
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw the snowflake
draw_snowflake(length, levels)

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.exitonclick()

"""
In this code, we start by importing the turtle module and creating a Turtle instance called t. We set the initial parameters: length represents the length of the main branch, and levels represents the number of levels or branches.

We define a recursive function called draw_branch that takes the branch_length and levels as parameters. Inside the function, we have a base case that checks if levels is 0. If it is, we move the turtle forward by branch_length and return.

If levels is not 0, we divide the branch_length by 3.0 to create smaller branches in each recursive call. We then make four recursive calls, each turning the turtle by 60 degrees and calling draw_branch with the reduced branch_length and levels - 1.

Next, we define another function called draw_snowflake that takes the branch_length and levels as parameters. This function is responsible for drawing the complete snowflake pattern. It uses a loop to draw six branches in a snowflake pattern by calling the draw_branch function and then turning the turtle right by 60 degrees.

We set up the turtle's initial position using t.penup() and t.goto(-100, 0), and then use t.pendown() to put the pen down for drawing.

Finally, we call the draw_snowflake function with the initial length and levels to draw the snowflake pattern. After drawing is complete, we hide the turtle using t.hideturtle(). Finally, we use turtle.exitonclick() to keep the window open until we click on it.

When you run this code, you'll see the turtle drawing a snowflake pattern using recursion. The number of levels (levels) determines the complexity of the snowflake. Feel free to adjust the length and levels variables to create different snowflake patterns.
"""