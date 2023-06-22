def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) given weight in kilograms (kg) and height in meters (m).
    Returns the calculated BMI.
    """
    bmi = weight / (height ** 2)
    return bmi


def interpret_bmi(bmi):
    """
    Interprets the BMI value and provides a corresponding category.
    Returns the BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Taking user input for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = calculate_bmi(weight, height)

# Interpreting BMI
bmi_category = interpret_bmi(bmi)

# Displaying the result
print("Your BMI is:", bmi)
print("BMI Category:", bmi_category)

"""
In this program, we define two functions: calculate_bmi and interpret_bmi. The calculate_bmi function takes the weight and height as input, calculates the BMI using the formula, and returns the result. The interpret_bmi function takes the calculated BMI and assigns it to a BMI category based on specific ranges.

The user is prompted to enter their weight and height, which are then used to calculate the BMI using the calculate_bmi function. The resulting BMI is passed to the interpret_bmi function to determine the BMI category. Finally, the program displays the calculated BMI and the corresponding category.

Feel free to customize this program according to your requirements or add additional features. Let me know if you need any further assistance!
"""

"""
DESCRIPTION:
Program Description: BMI Calculator

Welcome to the BMI Calculator program! This program allows you to calculate your Body Mass Index (BMI) based on your weight and height. BMI is a measure of body fat and provides an indication of whether you are underweight, have a normal weight, are overweight, or fall into the obese category.

Here's how the program works:

You will be prompted to enter your weight in kilograms (kg).
Next, you will be asked to enter your height in meters (m).
Once you provide the required information, the program will calculate your BMI using the formula: BMI = weight / (height ** 2).
After calculating your BMI, the program will interpret the BMI value and assign it to a specific category: "Underweight," "Normal weight," "Overweight," or "Obese."
Finally, the program will display your calculated BMI and the corresponding BMI category.

It's important to note that the BMI calculation is a simple formula and does not take into account factors such as muscle mass or body composition. Therefore, it should be used as a general guideline rather than a definitive assessment of your overall health.

Feel free to use this program to track your BMI over time or to gain insights into your weight status. Remember, maintaining a healthy weight is important for your overall well-being.

We hope you find this BMI Calculator program helpful in your health journey. Start by entering your weight and height, and let's calculate your BMI!
"""