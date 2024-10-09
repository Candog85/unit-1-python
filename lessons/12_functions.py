"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""

#defines function as greeting, with name perameter
def greeting(name):
    #prints "Hello (name)""
    print(f"Hello, {name}")

#Runs function with user input as parameter
greeting(input("What is your name?: "))

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

#defines function as square with number as parameter
def square(number):

    #returns number squared
    return number**2

#Calls square function and prints the result
print(square(32))


"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

#defines function as evenodd with number as parameter
def evenodd(number):
    
    #returns the boolean of the statement below, makes that boolean a string
    return str(number%2==0)

#prints the result of the called function evenodd
print(evenodd(12))


"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

#defines function as area with length and width as parameters
def area(length, width):

    #returns length times width
    return length*width

#prints the statement as well as whatever is returned by the area function
print(f"The area of this rectangle is {area(12,24)}")

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def temp_convert(temp):
    return temp*1.8+32

print(f"Your converted farenheit value is {temp_convert(54)} degrees")

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def average(numbers):
    sum=0
    for number in numbers:
        sum=sum+number
    return sum/len(numbers)

print(f"The average of your list is {average([10, 23, 30, 20])}")

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""

def calculator(price, quantity, discount=0):

    total=price*quantity

    discount=discount/100
    
    if discount>0:
        total=total-discount