# define a function to reverse the name
def reverse_name(name):
    # split the name into a list of separate words
    name_parts = name.split()

    # reverse the order of the list
    name_parts.reverse()

    # join the reversed list into a single string
    reversed_name = " ".join(name_parts)

    # return the reversed name
    return reversed_name

# prompt the user to enter their full name
name = input("Enter your full name: ")

# call the function to reverse the name
reversed_name = reverse_name(name)

# print the reversed name
print("Your name in reverse order is:", reversed_name)
