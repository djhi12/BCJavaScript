"""
    The .strftime() method is a built-in method in Python that is used to format a datetime object as a string. It takes a string argument that specifies the format of the resulting string.

    The format string consists of format codes that start with a percent sign %, followed by one or more characters that represent a particular date or time element, such as year, month, day, hour, minute, second, etc.

    For example, %Y represents the year with century as a decimal number, %m represents the month as a zero-padded decimal number, %d represents the day of the month as a zero-padded decimal number, %H represents the hour as a zero-padded decimal number (24-hour clock), %M represents the minute as a zero-padded decimal number, %S represents the second as a zero-padded decimal number, %A represents the full weekday name, %B represents the full month name, and so on.
    
"""

# Here's an example of how to use the .strftime() method:
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string using the strftime() method
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted date
print(formatted_date)

# This code gets the current date and time using datetime.datetime.now(), formats it as a string using the .strftime() method with the format string "%Y-%m-%d %H:%M:%S", and then prints the formatted date in the specified format. The resulting output will look something like this: 2022-08-16 14:30:00.


# Example Program
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string using the strftime() method
formatted_date = now.strftime("Today is %A, %B %d, %Y at %I:%M %p")

# Print the formatted date
print(formatted_date)

"""
    In this program, we first import the datetime module. We then use the datetime.datetime.now() method to get the current date and time as a datetime object, which we assign to the variable now.

    Next, we use the .strftime() method to format the now object as a string with the desired format. In this case, we format the date and time as "Today is [weekday], [month name] [day of month], [year] at [hour:minute AM/PM]".

    Finally, we print the formatted date string using the print() function.
"""

# When you run this program, the output will be a string that includes the current date and time in the specified format, similar to this: Today is Thursday, April 21, 2023 at 11:30 AM

# Note that the exact output will depend on the current date and time on your computer.