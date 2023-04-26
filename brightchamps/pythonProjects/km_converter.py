# Define the conversion function
def kmh_to_ms(kmh):
    return kmh / 3.6

# Prompt the user for input
kmh = float(input("\nEnter speed in kilometers per hour: "))

# Convert km/h to m/s
ms = kmh_to_ms(kmh)

# Print the result
print("Speed:", kmh, "km/h =", ms, "m/s", "\n")


"""
    In this code, we first define a function called kmh_to_ms that takes a speed in kilometers per hour as an input, divides it by 3.6 (the number of meters per second in one kilometer per hour), and returns the result in meters per second.

    Then, we prompt the user to enter a speed in kilometers per hour using the input function, convert the input to a floating-point number using float, and store it in a variable called kmh.

    Next, we call the kmh_to_ms function with kmh as an argument, and store the result in a variable called ms.

    Finally, we print the original speed in kilometers per hour and the converted speed in meters per second using print.
"""