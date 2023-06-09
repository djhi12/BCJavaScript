pizzas = [
    {'name': 'Margherita', 'toppings': ['tomato', 'mozzarella', 'basil']},
    {'name': 'Pepperoni', 'toppings': ['tomato', 'mozzarella', 'pepperoni']},
    {'name': 'Hawaiian', 'toppings': ['tomato', 'mozzarella', 'ham', 'pineapple']}
]

for pizza in pizzas:
    pizza_name = pizza['name']
    pizza_toppings = ', '.join(pizza['toppings'])
    print("I like", pizza_name, "pizza with", pizza_toppings, "toppings.")

print("\nPizza is one of my favorite foods!")


"""
Output:
I like Margherita pizza with tomato, mozzarella, basil toppings.
I like Pepperoni pizza with tomato, mozzarella, pepperoni toppings.
I like Hawaiian pizza with tomato, mozzarella, ham, pineapple toppings.

Pizza is one of my favorite foods!

"""