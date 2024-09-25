"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
def task_1():

    #Placehoder for counter
    counter=0

    #While counter is less than 1, add one to counter and print its value
    while counter<10:
        counter+=1
        print(counter)
        

task_1()

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

def task_2():

    #Placeholder for counter, starts 10
    counter=10

    #While counter is greater than or equal to 1, print its value
    while counter>=1:
        print(counter)
        counter-=1

task_2()

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

def task_3():

    #Takes user input for the number being used
    number=float(input("Enter a number: "))

    #Starts at ten
    counter=10

    #While counter is a positive integer, 
    while counter>=1:

        #number is multiplied by counter
        number=number*counter

        #counter is decreased by one
        counter-=1

    #Prints result
    print(number)

task_3()


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

def task_4():

    #Preset password "meggido"
    password="meggido"

    #Takes input for the guess
    guess=input("Guess the password: ")
    
    #If the guess isn't the password
    while guess!=password:

        #Prints incorrect password
        print("Incorrect password!")

        #Reprompt
        guess=input("Guess the password: ")
    
    #When the loop is broken (guess=password), prints:
    print("Correct!")

task_4()

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

def task_5():

    sum_var=0

    number=input("Enter an integer: ")

    for digits in number:
        sum_var=sum_var+int(digits)
    
    print(sum_var)

#task_5()

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

def task_6():

    #List of the first 2 fibbonachi numbers
    fibonacci=[0,1]

    #Takes input for the amount of numbers to be printed
    n=int(input("How many fibbonachi numbers?"))

    #For loop in range og 
    for x in range(n):
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    
    print(fibonacci)

task_6()    