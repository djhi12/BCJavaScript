num_pizzas = int(input("How many favorite pizzas do you have? "))
user_pizzas = []

for _ in range(num_pizzas):
    pizza_name = input("Enter the name of a pizza: ")
    num_toppings = int(input("How many toppings does it have? "))
    toppings = []
    for _ in range(num_toppings):
        topping = input("Enter a topping: ")
        toppings.append(topping)
    user_pizzas.append({'name': pizza_name, 'toppings': toppings})

for pizza in user_pizzas:
    pizza_name = pizza['name']
    pizza_toppings = ', '.join(pizza['toppings'])
    print("You like", pizza_name, "pizza with", pizza_toppings, "toppings.")

print("\nPizza is one of your favorite foods!\n")

"""
In this modified code, we start by asking the user for the number of favorite pizzas they have. We store this value in the variable num_pizzas. Then, we iterate num_pizzas times using a for loop to collect the name and toppings for each pizza.

Inside the loop, we first ask the user to enter the name of a pizza and store it in the variable pizza_name. We also ask for the number of toppings the pizza has and store it in the variable num_toppings. Then, we use another loop to collect the individual toppings. The toppings are stored in a list called toppings.

After collecting all the user's favorite pizzas, we iterate over the user_pizzas list using a for loop. Inside the loop, we extract the pizza name and toppings from each dictionary and use the join() method to concatenate the toppings list into a comma-separated string. Finally, we print a sentence that includes the pizza name and toppings.
"""