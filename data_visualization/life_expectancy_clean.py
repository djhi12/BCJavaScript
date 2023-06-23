import csv

filename = 'life-expectancy.csv'
with open(filename) as life_expectancies:
    
    i = 0
    for life in life_expectancies:
        i += 1
        life_details = life.strip()
        life_detail_clean = life_details.split(",")
        
        if i > 1:
            print(life_detail_clean)

