# # print("Test")
# # This function takes a temperature
# # in Celcius and converts it to
# # Farenheit.
# def celcius_to_farenheit(celcius):
#     return celcius * 1.8 + 32

# # This function takes a temperature
# # in Farenheit and converts it to
# # Celcius.
# def farenheit_to_celcius(farenheit):
#     return (farenheit - 32) / 1.8

# try:
#     c = float(input("Enter a temp in C: "))
#     print("In F: " + str(celcius_to_farenheit(c)))
    
#     f = float(input("Enter a temp in F: "))
#     print("In C: " + str(farenheit_to_celcius(f)))
    
# except ValueError:
#     print("You must enter a float!")



def retrieve_positive_number():
    while True:
        try:
            number = int(input("Enter a positive number: "))
            if number > 0:
                return number # true
            print("The number must be positive!") # false
        except ValueError:
            print("That wasn't a number!")

print(retrieve_positive_number())