"""
Define the debt-to-income ratio (DTI) that will be used as a criterion for loan affordability. The DTI is typically expressed as a percentage and represents the ratio of a person's total monthly debt payments to their monthly income.

Create a function that takes the user's monthly income and expenses as input and calculates the maximum loan amount they can afford based on the specified DTI ratio.

Within the function, subtract the total monthly expenses from the monthly income to determine the amount available for loan repayment.

Multiply the available amount by the DTI ratio (expressed as a decimal) to obtain the maximum allowable monthly loan payment.

To convert the monthly payment to a loan amount, you need to consider the interest rate and loan term. Use the loan payment calculation formula or a financial library to calculate the loan amount based on the maximum allowable monthly payment.
"""


def calculate_loan_amount(interest_rate, loan_term, monthly_payment):
    # Implement your loan amount calculation logic here
    # This function should calculate and return the loan amount
    # based on the provided interest rate, loan term, and monthly payment
    # You can use formulas or financial libraries to perform the calculation
    # and return the loan amount.

    # Placeholder calculation
    loan_amount = monthly_payment * loan_term
    return loan_amount


def calculate_loan_affordability(income, expenses, dti_ratio, interest_rate, loan_term):
    available_income = income - expenses
    max_monthly_payment = available_income * dti_ratio
    # Calculate the loan amount based on the maximum allowable monthly payment
    loan_amount = calculate_loan_amount(interest_rate, loan_term, max_monthly_payment)
    
    return loan_amount


def main():
    print("\nLoan Affordability Calculator")
    print("------------------------------")

    # Get user inputs
    income = float(input("\nEnter your monthly income: "))
    expenses = float(input("Enter your monthly expenses: "))
    dti_ratio = float(input("Enter your desired debt-to-income ratio (in decimal form): "))
    interest_rate = float(input("Enter the loan interest rate (in decimal form): "))
    loan_term = int(input("Enter the loan term (in months): "))

    # Calculate maximum loan amount
    loan_amount = calculate_loan_affordability(income, expenses, dti_ratio, interest_rate, loan_term)

    # Display the result
    print("\nMaximum Loan Amount:", loan_amount, "\n")


# Call the main function directly
main()
