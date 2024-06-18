# 13. Write a program that asks the user for their birth year and calculates their age. 
from datetime import datetime
current_year = datetime.now().year
year = int(input("Enter your birth year"))
age = current_year-year
print("Your age is : " , age)