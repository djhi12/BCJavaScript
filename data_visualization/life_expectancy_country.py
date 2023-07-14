# import csv

# filename = 'life-expectancy.csv'
# year_input = input("Enter a country: ")
# print()
# with open(filename) as life_expectancies:
#     i = 0
#     for life in life_expectancies:
#         i += 1
#         life_details = life.strip()
#         life_detail_clean = life_details.split(",")

#         if i > 1 and life_detail_clean[0] == year_input.title():
#             # Print all details for the specified year
#             # print("Country:", life_detail_clean[0])
#             # print("Code:", life_detail_clean[1])
#             # print("Year:", life_detail_clean[2])
#             # print("Life Expectancy:", life_detail_clean[3])

#             print(f"{life_detail_clean[0]}, {life_detail_clean[1]}, {life_detail_clean[2]}, {life_detail_clean[3]}\n")


# Largest
# import csv

# filename = 'life-expectancy.csv'
# year_input = input("Enter a country: ")
# print()
# max_life_expectancy = 0

# with open(filename) as life_expectancies:
#     i = 0
#     for life in life_expectancies:
#         i += 1
#         life_details = life.strip()
#         life_detail_clean = life_details.split(",")

#         if i > 1 and life_detail_clean[0] == year_input.title():
#             # Print all details for the specified year
#             # print(f"Country: {life_detail_clean[0]}")
#             # print(f"Code: {life_detail_clean[1]}")
#             # print(f"Year: {life_detail_clean[2]}")
#             # print(f"Life Expectancy: {life_detail_clean[3]}\n")

#             # Check if the current life expectancy is greater than the previous maximum
#             current_life_expectancy = float(life_detail_clean[3])
#             if current_life_expectancy > max_life_expectancy:
#                 max_life_expectancy = current_life_expectancy

# print(f"Highest Life Expectancy: {max_life_expectancy}\n")


# Lowest

filename = 'life-expectancy.csv'
year_input = input("Enter a country: ")
print()
max_life_expectancy = 0
min_life_expectancy = float('inf')

with open(filename) as life_expectancies:
    i = 0
    for life in life_expectancies:
        i += 1
        life_details = life.strip()
        life_detail_clean = life_details.split(",")

        if i > 1 and life_detail_clean[0] == year_input.title():
            # Print all details for the specified year
            # print(f"Country: {life_detail_clean[0]}")
            # print(f"Code: {life_detail_clean[1]}")
            # print(f"Year: {life_detail_clean[2]}")
            # print(f"Life Expectancy: {life_detail_clean[3]}\n")

            # Check if the current life expectancy is greater than the previous maximum
            current_life_expectancy = float(life_detail_clean[3])
            if current_life_expectancy > max_life_expectancy:
                max_life_expectancy = current_life_expectancy

            # Check if the current life expectancy is less than the previous minimum
            if current_life_expectancy < min_life_expectancy:
                min_life_expectancy = current_life_expectancy

print(f"Highest Life Expectancy: {max_life_expectancy}")
print(f"Lowest Life Expectancy: {min_life_expectancy}")
