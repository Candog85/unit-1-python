"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""

#I'm using functions so I can reuse variables cause im lazy
def task_1():

    #Created float variable
    float_var=9.14

    #Converted to integer
    int_var=int(float_var)

    #Printed both variables (and converted to strings)
    print(str(float_var)+" "+str(int_var))

task_1()

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

def task_2():

    #Defined number
    number=float(input("Input a number: "))

    #Checks if number is negative
    if number < 0:
        print("That number is negative!")

    #Checks if number is positive
    elif number > 0:
        print("Your number is positive!")

    #Checks if number is zero
    elif number == 0:
        print("Your number is cero. Bleach reference??!!?")

task_2()

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

def task_3():

    #Define an interger and float variable through user input
    int_var=int(input("Enter a integer: "))
    float_var=float(input("Enter a float: "))

    #Prints the sums, product, and quotient of the two variables
    print("Sum (addition): "+str(int_var+float_var))
    print("Sum (subtraction): "+str(int_var-float_var))
    print("Product: "+str(int_var*float_var))
    print("Quotient: "+str(int_var/float_var))

task_3()

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
def task_4():

    #List of fruits called "fruitas"
    fruitas = {

        "Grapes": 5,
        "Bananas": 9,
        "Cherries": 12,
        "Orange": 1

    }

    #Prints value for bananas
    print(fruitas["Bananas"])

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
def task_5():

    #String version of the list
    string_var=("1,5,2,35,59")

    #Using split() to turn string into a list, then tuple() to turn the list into a tuple
    num_tuple= tuple(string_var.split(","))

    #Prints both string and tuple
    print(string_var)
    print(num_tuple)

task_5()