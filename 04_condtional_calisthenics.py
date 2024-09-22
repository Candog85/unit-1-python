'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
def task_1():

    #Defines number
    number=10

    #If number is greater than ten and has a remainder of 0
    if number>10 and number%2==0:
        print(True)

    #If above is false...
    else:
        print(False)


#task_1()

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

def task_2():

    #Defines age and student status
    age=20
    student=True

    #Checks if user is under 18 OR is a student
    if age<18 or student==True:
        price=10
    
    #If they are neither:
    else:
        price=20
    
    #Prints the price calculated
    print(f"The price is ${price}")

#task_2()

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

def task_3():

    #Defines the fruit list
    fruits=["apple", "orange", "banana", "pear"]

    #Takes user input for the fruit
    fruit=input("Enter a fruit on the list: ")

    #Checks if the user's input is a part of the list
    if fruit in fruits:
        print("The fruit is in the list")

    #If it's not on the list:
    else:
        print("The fruit is not in the list")


'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

def task_4():
    year=2023
    if year%100==0 and year%3==0:
        print("This year is a leap year and century year!")
    else:
        print("This year is either not a century or not a leap year")

#task_4():

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

def task_5():

    #Takes user input for zone, lowercases it
    destination=input("Zone a or b?: ").lower()

    #If the user inputs a zone thats not "a" or "b", prints error message and restarts function
    if not(destination=="a" or destination=="b"):
        print("Enter a valid zone!")
        task_5()

    #Takes input for weight and makes it a float
    weight=float(input("How much does it weigh?: "))

    #If the user inputs weight that is not a positive number, prints error message and restarts function
    if weight<=0:
        print("Error, enter a value over 0!")
        task_5()

    #If zone a is chosen, cost is $5 per kg
    if destination=="a":
        cost=weight*5

    #If zone b is chosen, cost is $7 per kg
    elif destination=="b":
        cost=weight*7
    
    #prints resulting cost
    print(f"This package will cost ${cost} to ship.")

#task_5()
    

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

def task_6():
    sides=[
        float(input("Enter side 1 length: ")), 
        float(input("Enter side 2 length: ")), 
        float(input("Enter side 3 length: "))
    ]

    if sides[0]==sides[1]==sides[2]:
        print("This triangle is equilateral!")
    print(sides)
task_6()