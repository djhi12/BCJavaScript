# Get input from the user
principal = float(input("\nEnter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

# Calculate the simple interest
interest = (principal * rate * time) / 100

# Print the result
print("The simple interest for a principal of Rs.", principal, "at a rate of", rate, "percent per year for", time, "years is Rs.", interest, "\n")


"""
    In this program, we first get the input from the user using the input() function and convert the input to floating-point numbers using the float() function. We then calculate the simple interest using the formula (P * R * T) / 100, where P is the principal amount, R is the rate of interest, and T is the time period in years. Finally, we print the result using the print() function.

    You can further enhance this program by adding error handling, formatting the output, or allowing the user to choose between calculating the simple interest or the final amount.
"""