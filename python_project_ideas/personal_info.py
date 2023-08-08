# Function is a block of code (mini program), organize, reuse, call many times, we can pass parameters,
def main():

    # Variables is like a container where we can store data like strings and numbers
    name = input("Type your name: ")
    
    # Int that converts the string into number
    age = int(input("Type your age: "))
    birthday = input("Type your birthday: ")
    address = input("Type your address: ")

    # print function, it will print the value
    # f-string: is a string formatting, concatenate or connect different values.
    # New line: break line
    print(f"\nYour personal info: \nName: {name}\nAge: {age}\nBirthday: {birthday}\nAddress: {address}")

# Call the function
main()
