def print_numbers_version_one():
    number = 2
    while number <= 100:
        # If number is even, print it:
        if number % 2 == 0:
            print(number)
            number += 1

print_numbers_version_one()


def print_numbers_version_two():
    number = 2
    while number <= 100:
        print(number)
        # Increase number by 2, which, by definition,
        # is the next even number:
        number += 2

print_numbers_version_two()

