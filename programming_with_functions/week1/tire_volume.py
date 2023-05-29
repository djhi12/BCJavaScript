import math

"""
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

Formula: v = pi * w**2 * a (w * a + 2540 * d) / 10000000000

> python tire_volume.py
Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15): 14
The approximate volume is 24.09 liters

> python tire_volume.py
Enter the width of the tire in mm (ex 205): 205
Enter the aspect ratio of the tire (ex 60): 60
Enter the diameter of the wheel in inches (ex 15): 15
The approximate volume is 39.92 liters
"""

tire_width = float(input("\nEnter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Formula: v = pi * w**2 * a (w * a + 2540 * d) / 10000000000
volume = math.pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * diameter) / 10000000000

print(f"\nThe approximate volume in {round(volume, 2)} liters.\n")

