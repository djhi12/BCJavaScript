# import math module and datetime
import math
import datetime

# Get input from the user
width = float(input("\nEnter the width of the tire in mm (ex 205): "))
ratio_aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches(ex 15): "))

# Simplify the formula using variables
number_d = 2540 * diameter
parenthesis = width * ratio_aspect + number_d
semi_v = math.pi * width**2 * ratio_aspect
volume = semi_v * parenthesis / 10000000000

# Round the answer to two decimal points
volume = round(volume, 2)

# Print the results
print(f"\nThe approximate volume is {volume} liters \n")

# Get current date of the week
today = datetime.datetime.now()

# Open a text file named volumes.txt in append mode
with open("volumes.txt", "at") as volumes_file:
    print(f"{today:%Y-%m-%d} , {width} , {ratio_aspect} , {diameter}, {volume}\n")
