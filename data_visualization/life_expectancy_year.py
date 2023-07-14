import csv

filename = 'life-expectancy.csv'
year_input = input("Enter a year: ")

with open(filename) as life_expectancies:
    i = 0
    for life in life_expectancies:
        i += 1
        life_details = life.strip()
        life_detail_clean = life_details.split(",")

        if i > 1 and life_detail_clean[2] == year_input:
            # Print all details for the specified year
            # print("Country:", life_detail_clean[0])
            # print("Code:", life_detail_clean[1])
            # print("Year:", life_detail_clean[2])
            # print("Life Expectancy:", life_detail_clean[3])

            print(f"{life_detail_clean[2]}, {life_detail_clean[0]}, {life_detail_clean[1]}, {life_detail_clean[3]}")


# import csv

# filename = 'life-expectancy.csv'
# year_input = input("Enter a year: ")

# # Initialize the variable to store the highest life expectancy
# highest_life_expectancy = 0.0
# # Variable to store the country with the highest life expectancy
# country_with_highest_life = ''

# with open(filename) as life_expectancies:
#     reader = csv.reader(life_expectancies)
#     next(reader)  # Skip the header row

#     for row in reader:
#         country = row[0]
#         code = row[1]
#         year = row[2]
#         life_expectancy = float(row[3])

#         if year == year_input:
#             # print(f"{year}, {country}, {code}, {life_expectancy}")

#             if life_expectancy > highest_life_expectancy:
#                 highest_life_expectancy = life_expectancy
#                 country_with_highest_life = country

# print(
#     f"\nThe highest life expectancy in {year_input} is {highest_life_expectancy} years in {country_with_highest_life}.")
