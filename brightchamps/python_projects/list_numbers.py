numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_numbers(is_even):
    if is_even:
        return list(filter(lambda x: x % 2 == 0, numbers))
    else:
        return list(filter(lambda x: x % 2 != 0, numbers))

even_numbers = filter_numbers(True)
odd_numbers = filter_numbers(False)

print("\nEven numbers:", even_numbers)
print("Odd numbers:", odd_numbers, "\n")
