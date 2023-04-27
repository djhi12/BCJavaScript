# ask user for the number they want the multiplication table for
num = int(input("Enter a number: "))

# use a for loop to iterate through the range 1 to 11
for i in range(1, 11):
    # calculate the product of the number and the loop variable
    product = num * i
    # print the equation and the product in a formatted string
    print(f"{num} x {i} = {product}")

# You can modify this code to generate a larger or smaller multiplication table by changing the range of the for loop.
