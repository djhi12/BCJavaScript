def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67


def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit}°F")
    
    elif choice == 2:
        celsius = float(input("Enter the temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius}°C = {kelvin} K")
    
    elif choice == 3:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {celsius}°C")
    
    elif choice == 4:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit}°F = {kelvin} K")
    
    elif choice == 5:
        kelvin = float(input("Enter the temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"{kelvin} K = {celsius}°C")
    
    elif choice == 6:
        kelvin = float(input("Enter the temperature in Kelvin: "))
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} K = {fahrenheit}°F")
    
    else:
        print("Invalid choice!")


temperature_converter()

"""
When you run this script, it will display a menu for the user to choose the conversion type. After the user selects an option, the program will prompt for the input temperature and display the converted temperature.

For example, if the user selects option 1 and enters a temperature of 25°C, the program will output the equivalent temperature in Fahrenheit as 77°F.

Feel free to customize the code according to your requirements and add error handling as needed.
"""


# Student Problem
"""
print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    
The code begins by defining several functions that perform temperature conversions. These functions take a temperature value as an input and return the converted temperature according to the conversion formulas.

The temperature_converter() function is then defined. It serves as the main function that interacts with the user. It displays a menu with six options for temperature conversion. The user is prompted to enter their choice by selecting a number from 1 to 6.

Based on the user's choice, the program enters the corresponding if or elif block and prompts the user to enter the temperature value they want to convert. The appropriate conversion function is called with the provided temperature, and the result is displayed to the user.

If the user enters an invalid choice, the program displays an "Invalid choice!" message.

Finally, the temperature_converter() function is called to start the program execution.

Overall, the code allows the user to convert temperatures between Celsius, Fahrenheit, and Kelvin by selecting the desired conversion type and providing the input temperature.
"""