"""
If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

Near the beginning of your program replace the code that asks the user for the subtotal with a loop that repeatedly asks the user for a price and a quantity and computes the subtotal. This loop should repeat until the user enters "0" for the price.

"""

"""
    Testing Procedure 1
    If today is any day except Tuesday or Wednesday, run your program using the inputs shown below. Ensure that your program’s output matches the output shown below.
    
    Please enter the subtotal: 42.75
    Sales tax amount: 2.56
    Total: 45.31

    Please enter the subtotal: 55.20
    Sales tax amount: 3.31
    Total: 58.51
    
    
    Testing Procedure 2
    If today is Tuesday or Wednesday, run your program using the input shown below. Ensure that your program’s output matches output shown below.
    
    Please enter the subtotal: 42.75
    Sales tax amount: 2.56
    Total: 45.31


    Please enter the subtotal: 55.20
    Discount amount: 5.52
    Sales tax amount: 2.98
    Total: 52.66
"""


import datetime

# Get the current day of the week
today = datetime.datetime.now().strftime("%A")
print(today)

# Get the subtotal from the user
subtotal = float(input("\nPlease enter the subtotal: "))

# Check if the subtotal is $50 or greater and today is Tuesday or Wednesday
if subtotal >= 50 and (today == "Tuesday" or today == "Wednesday"):
    # Calculate the discount amount
    discount = subtotal * 0.1
else:
    discount = 0

# Calculate the sales tax amount
sales_tax = subtotal * 0.06

# Calculate the total amount due
total = subtotal - discount + sales_tax

# Print the discount amount if applicable, sales tax amount, and total amount due
if discount > 0:
    print("Discount amount:", round(discount, 2))

print("Sales tax amount:", round(sales_tax, 2))
print(f"Total: {round(total, 2)}\n")

