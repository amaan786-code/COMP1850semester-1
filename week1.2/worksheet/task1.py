# Worksheet 1.2: Task 1 Solution
import sys

grade = input("Please enter a grade in the range 0-100: ")
if grade.isdecimal() == True:
    grade = int(grade)
    if grade < 0 or grade > 100:
        sys.exit("Error: Grade must be an integer between 0 and 100")  
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade >= 0 and grade <= 39:
    print(f"{grade} is a Fail")
elif grade >= 40 and grade <= 69:
    print(f"{grade} is a Pass")
elif grade >= 70 and grade <= 100:
    print(f"{grade} is a Distinction") 
