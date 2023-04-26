def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest given the principal amount, rate of interest, and time period.
    """
    return (principal * rate * time) / 100

# Get input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

# Calculate the simple interest using the function
interest = calculate_simple_interest(principal, rate, time)

# Print the result
print("The simple interest for a principal of Rs.", principal, "at a rate of", rate, "percent per year for", time, "years is Rs.", interest)

"""
    In this updated code, we have defined the calculate_simple_interest function that takes three arguments and returns the simple interest calculated using the formula (P * R * T) / 100. We then call this function with the user input values of principal, rate, and time to calculate the simple interest and store it in the interest variable. Finally, we print the result using the print() function.

    By defining the calculate_simple_interest function, we have made the code more modular and reusable. We can now call this function from different parts of the code, or even from other programs, without having to repeat the same calculation code again and again.
"""