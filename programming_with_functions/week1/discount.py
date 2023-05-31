from datetime import date

"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
"""

current_date = date.today()
# print(current_date)
day_of_week = current_date.weekday()
# print(day_of_week)

# Mapping the integer value to the corresponding day
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
specific_day = days[day_of_week]
# print(specific_day)

subtotal = float(input("\nPlease enter the subtotal: "))
sales_tax = 0.06
sales_tax_amount = subtotal * sales_tax
# print(f"Sales tax amount: {sales_tax_amount:.2f}")

total_amount = subtotal + sales_tax_amount
# print(f"Total: {total_amount:.2f}\n")

discount = .10

# Discount based on day
if specific_day == 'Tuesday' or specific_day == 'Wednesday' and subtotal >= 50:
    discounted_amount = subtotal * discount
    subtracted_amount = discounted_amount - subtotal
    print(subtracted_amount)
    
    