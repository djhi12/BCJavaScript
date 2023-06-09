"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

    Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
 
    Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
"""

pizzas = ['Margherita', 'Pepperoni', 'Hawaiian']

for pizza in pizzas:
    print("I like", pizza, "pizza.")

print("\nPizza is one of my favorite foods!")

# In this code, we start by creating a list called pizzas with three different types of pizzas. Then, we use a for loop to iterate over each pizza in the list. Inside the loop, we print a sentence using the name of each pizza. Finally, outside the loop, we print a statement expressing our love for pizza.