#importing date, time, and datetime from datetime module
from datetime import date,time,datetime

#also imports the floor function from the math module for the last step
from math import floor

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

#Prints the current date and time using the now() function of datetime
print(datetime.now())

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

#assigns current_dt to current date and time using the now() function of datetime
current_dt=datetime.now()

#Prints date and time
print(current_dt)

#Using strftime prints the current_dt as a string
print(current_dt.strftime("%m/%d/%Y"))


"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

#Defining bday and current_dt as strings
bday="11/03/2007"

current_dt="10/07/2024"

#Converts bday and current_dt into date using strptime
print(datetime.strptime(bday, "%m/%d/%Y").date())
print(datetime.strptime(current_dt, "%m/%d/%Y").date())

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

#defines bday as user input string
bday=input("What is your birthday? Use month/day/year format: ")

#redefines bday as a string parse time, using the month/day/full year format. Then uses date operator to isolate the date from the time
bday=(datetime.strptime(bday, "%m/%d/%Y").date())

#prints the difference between the current date and bday, divides by 365 to determine the amount of years, and rounding down if their birthday hasn't passed yet
print(floor((date.today()-bday).days/365))