while True:
    try:
        # ask user for the number they want the multiplication table for
        num = int(input("Please enter a positive integer: "))
        if num <= 0:
            raise ValueError("The number must be positive.")
        break
    except ValueError as error:
        print(f"Invalid input: {error}")

# use a for loop to iterate through the range 1 to 11
for i in range(1, 11):
    # calculate the product of the number and the loop variable
    product = num * i
    # print the equation and the product in a formatted string
    print(f"{num} x {i} = {product}")
