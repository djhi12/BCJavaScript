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
def calculate_sales_tax(subtotal):
    # Function to calculate sales tax
    sales_tax_rate = 0.06
    sales_tax_amount = subtotal * sales_tax_rate
    return sales_tax_amount


def calculate_discount(subtotal):
    # Function to calculate discount
    discount_rate = 0.1
    discount_amount = subtotal * discount_rate
    return discount_amount


# Get today's weekday
today = datetime.datetime.today().weekday()

# Testing Procedure 1
if today not in [1, 2]:
    subtotal = 42.75
    expected_sales_tax_amount = 2.56
    expected_total = 45.31

    sales_tax_amount = calculate_sales_tax(subtotal)
    total = subtotal + sales_tax_amount

    assert sales_tax_amount == expected_sales_tax_amount, f"Error: Sales tax amount is {sales_tax_amount}, but expected {expected_sales_tax_amount}"
    assert total == expected_total, f"Error: Total is {total}, but expected {expected_total}"

    subtotal = 55.20
    expected_sales_tax_amount = 3.31
    expected_total = 58.51

    sales_tax_amount = calculate_sales_tax(subtotal)
    total = subtotal + sales_tax_amount

    assert sales_tax_amount == expected_sales_tax_amount, f"Error: Sales tax amount is {sales_tax_amount}, but expected {expected_sales_tax_amount}"
    assert total == expected_total, f"Error: Total is {total}, but expected {expected_total}"

# Testing Procedure 2
if today in [1, 2]:
    subtotal = 42.75
    expected_sales_tax_amount = 2.56
    expected_total = 45.31

    sales_tax_amount = calculate_sales_tax(subtotal)
    total = subtotal + sales_tax_amount

    assert sales_tax_amount == expected_sales_tax_amount, f"Error: Sales tax amount is {sales_tax_amount}, but expected {expected_sales_tax_amount}"
    assert total == expected_total, f"Error: Total is {total}, but expected {expected_total}"

    subtotal = 55.20
    expected_discount_amount = 5.52
    expected_sales_tax_amount = 2.98
    expected_total = 52.66

    discount_amount = calculate_discount(subtotal)
    sales_tax_amount = calculate_sales_tax(subtotal - discount_amount)
    total = subtotal - discount_amount + sales_tax_amount

    assert discount_amount == expected_discount_amount, f"Error: Discount amount is {discount_amount}, but expected {expected_discount_amount}"
    assert sales_tax_amount == expected_sales_tax_amount, f"Error: Sales tax amount is {sales_tax_amount}, but expected {expected_sales_tax_amount}"
    assert total == expected_total, f"Error: Total is {total}, but expected {expected_total}"
