# choice() is a function in the Python random module that is used to randomly select an element from a sequence.


# Example Program
import random

quotes = [
    "The best way to predict the future is to invent it. -Alan Kay",
    "I have not failed. I've just found 10,000 ways that won't work. -Thomas Edison",
    "If you want to achieve greatness, stop asking for permission. -Unknown",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. -Winston Churchill",
    "The only way to do great work is to love what you do. -Steve Jobs"
]

random_quote = random.choice(quotes)
print("Here's a quote to inspire you:")
print(random_quote)

# In this program, we define a list of quotes and use choice() to randomly select one of them. We then print the randomly selected quote to the console. Each time the program is run, a different quote will be displayed.