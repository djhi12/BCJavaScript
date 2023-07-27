# Grade Calculator

# Get marks for three subjects
maths_marks = float(input("\nEnter marks obtained in Maths: "))
english_marks = float(input("Enter marks obtained in English: "))
science_marks = float(input("Enter marks obtained in Science: "))

# Calculate total marks and average percentage
total_marks = maths_marks + english_marks + science_marks
average_percentage = total_marks / 3

# Display total marks and average percentage
print("\nTotal Marks Obtained:", total_marks)
print("Average Percentage Obtained:", average_percentage)

# Determine Grade
if average_percentage >= 90:
    print("Grade: A\n")
elif average_percentage >= 80:
    print("Grade: B\n")
elif average_percentage >= 70:
    print("Grade: C\n")
else:
    if total_marks < 120:
        print("Grade: F\n")
    else:
        print("Grade: D\n")

"""
    Explanation:

    In this program, we first take the marks obtained by the student in three subjects (Maths, English, and Science) as input using the input() function. We then calculate the total marks obtained by adding the marks obtained in all three subjects and the average percentage obtained by dividing the total marks by 3.

    Next, we display the total marks and average percentage obtained by the student using the print() function.

    After that, we use an if statement to determine the grade obtained by the student based on their average percentage. We use a nested if statement to check if the total marks obtained by the student are less than 120. If so, we assign them an F grade, otherwise, they are assigned a D grade.

    Finally, we print the grade obtained by the student using the print() function.
"""