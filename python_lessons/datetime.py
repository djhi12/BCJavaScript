# To get the current date in Python, you can use the datetime module. Here's an example:

from datetime import date

current_date = date.today()
print(current_date)

"""
This code will output the current date in the format YYYY-MM-DD. For example, if you run this code today (May 31, 2023), it will output 2023-05-31.

If you want to format the date in a different way, you can use the strftime() method of the date object. Here's an example:
"""

from datetime import date

current_date = date.today()
formatted_date = current_date.strftime("%B %d, %Y")
print(formatted_date)

"""
This code will output the current date in the format Month Day, Year. For example, if you run this code today (May 31, 2023), it will output May 31, 2023.

You can customize the format by specifying the desired format codes in the strftime() method. The %B represents the full month name, %d represents the day as a zero-padded decimal number, and %Y represents the year with century as a decimal number.
"""


# How to get the specific day?
from datetime import date

current_date = date.today()
day_of_week = current_date.weekday()

# Mapping the integer value to the corresponding day
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
specific_day = days[day_of_week]

print(specific_day)

"""
This code will output the specific day of the week for the current date. For example, if you run this code today (May 31, 2023), it will output Wednesday.

You can customize the output format or use the day integer directly according to your needs.
"""