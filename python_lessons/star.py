# Define the number of rows you want to print
num_rows = 5

# Outer loop for rows in descending order
for i in range(num_rows, 0, -1):
    
    # Inner loop for columns
    for j in range(i):
        print("*", end="")
        
    print() 
