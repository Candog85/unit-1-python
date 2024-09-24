"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

def task_1():

    counter=1

    while counter<=10:
        print(counter)
        counter+=1

task_1()

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

def task_2():

    counter=10

    while counter>=1:
        print(counter)
        counter-=1

task_2()

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

def task_2():

    number=float(input("Enter a number: "))
    counter=10

    while counter>=1:
        number=number*counter
        counter-=1

    print(number)

task_2()


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

def task_3():

    password="meggido"
    guess=input("Guess the password: ")
    
    while guess!=password:
        print("Incorrect password!")
        guess=input("Guess the password: ")
    
    print("Correct!")

task_3()

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

def task_5():

    number=[int(input("Enter an integer: "))]

    for x in number:
        print(x)

task_5()

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

