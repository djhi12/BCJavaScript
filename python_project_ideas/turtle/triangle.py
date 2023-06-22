import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle forward to draw the triangle
for _ in range(3):
    t.forward(100)  # Move forward by 100 units
    t.left(120)  # Turn left by 120 degrees

# Close the turtle graphics window
turtle.done()

"""
In the code above, the turtle object is created. It moves forward by 100 units and then turns left by 120 degrees. This process is repeated three times to complete the triangle.

You can modify the code to customize the triangle's size or position. Adjust the value passed to the forward() function to change the side length of the triangle. Additionally, you can change the angle of rotation by modifying the value passed to the left() function.

Feel free to experiment and modify the code according to your specific requirements.
"""