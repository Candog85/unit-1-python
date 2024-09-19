"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
def task_1():

    #Takes user password input, makes it lowercase and strips it
    attempt=input("Enter Password: ").lower().strip()

    #Real password
    password="fujin"

    #Compares the input with the actual password
    if attempt.strip() == password:
        print("Welcome, Anji Mito")
    else:
        print("You are not cool")

task_1()


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

def task_2():
    
    #Takes user input for string
    string_var=input("Enter a string that's NOT blank!!: ")

    #Compares stripped string to blank space to detect spaces.
    if string_var.strip() == "":
        print("You put spaces. What's wrong with you?")
    else:
        print("Alright, that works. :)")

task_2()

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""

def task_3():

    #Defines a string phrase
    phrase="I love Cats and CATS are so cool and cats are awesome!"

    #Makes the string lowercase. Checks if it has "cats" and replaces with "dogs"
    phrase=(phrase.lower()).replace("cats","dogs")
    print(phrase)

task_3()

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
def task_4():

    #Asks user for name and age amd strips
    name=input("What is your name?: ").strip()
    age=int(input("What is your age?: ").strip())

    #Uses f string to insert name and age values into string
    print(f"Your name is {name}, and you are {age} years old!")

task_4()


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

def task_5():

    #Takes input for two floats and makes them floats
    number_1=float(input("Enter number 1: ").strip())
    number_2=float(input("Enter number 2: ").strip())

    #Prints string with placeholder, first number divided by second, and rounded using format specifier ".1f"
    print(f"The rounded quotient is {number_1/number_2:.1f}")

task_5()
