# # Store information about a pizza being ordered.
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# # Summarize the order.
# print(f"You ordered a {pizza['crust']}-crust pizza "
#        "with the following toppings:")

# for topping in pizza['toppings']:
#     print(f"\t{topping}")


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    
    for topping in toppings:
        print(f"- {topping}")
