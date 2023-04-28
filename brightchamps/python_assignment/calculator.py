# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Function to calculate modulo
def modulo(x, y):
    return x % y

# Function to calculate exponential
def exponent(x, y):
    return x ** y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulo")
print("6.Exponential")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
    
elif choice == '5':
    print(num1,"%",num2,"=", modulo(num1,num2))
    
elif choice == '6':
    print(num1,"**",num2,"=", exponent(num1,num2))

else:
    print("Invalid input")
