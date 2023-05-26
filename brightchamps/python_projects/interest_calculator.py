def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


# Get user input
principal = float(input("\nEnter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Print the result
print("The simple interest is:", simple_interest, "\n")

"""
In the code above, we define a function calculate_simple_interest that takes the principal amount, interest rate, and time period as parameters. It calculates the simple interest using the formula (principal * rate * time) / 100 and returns the interest value.

We then prompt the user to enter the principal amount, interest rate, and time period using the input function. The float function is used to convert the user input into floating-point numbers.

Finally, we call the calculate_simple_interest function with the user-provided values and store the result in the simple_interest variable. We print the result to the console.

You can run this code and test it with different inputs to calculate the simple interest.

If you want to implement a compound interest calculator or any other variations, please let me know, and I'll be happy to assist you further.
"""



"""
The code begins by defining a function named calculate_simple_interest that takes three parameters: principal, rate, and time. This function is responsible for calculating the simple interest based on these values.

The interest variable inside the calculate_simple_interest function stores the result of the interest calculation, which is obtained by multiplying the principal, rate, and time variables and then dividing the result by 100.

Moving on, the code prompts the user to enter the principal amount, interest rate, and time period (in years) using the input function. Each input is stored in the corresponding variable: principal, rate, and time. The float function is used to convert the user input into floating-point numbers, allowing for decimal values.

After obtaining the user input, the code calls the calculate_simple_interest function with the provided values of principal, rate, and time. The calculated simple interest is then stored in the variable simple_interest.

Finally, the code prints the result to the console using the print function. The output message is "The simple interest is:" followed by the value of simple_interest.

By executing this code, the student can calculate the simple interest by providing the required inputs and obtaining the result for further analysis or presentation.

Remember, this code only calculates simple interest. If the student needs to calculate compound interest or perform more complex financial calculations, additional code modifications will be necessary.
"""