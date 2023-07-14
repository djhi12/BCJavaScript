import csv
with open('life-expectancy.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)