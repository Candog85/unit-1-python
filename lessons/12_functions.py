"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""

#defines function as greeting, with name parameter
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

#defines function temp_convert with temp as parameter
def temp_convert(temp):

    #returns temp processed through the conversion formula for celsius to fahrenheit 
    return temp*1.8+32

#prints result of temp_convert using 54* C as parameter
print(f"Your converted fahrenheit value is {temp_convert(54)} degrees")

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

#defines function average with numbers as parameter
def average(numbers):

    #defines sum as empty variable
    sum=0

    #for every number in the provided list of numbers using the "numbers" parameter:
    for number in numbers:

        #add that number to the sum
        sum=sum+number
    
    #return the sum divided by the amount of numbers using the len function
    return sum/len(numbers)

#print the result of the average function using 10, 23, 30, and 20 as list of numbers.
print(f"The average of your list is {average([10, 23, 30, 20])}")

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""

#defines function as calculator with parameters price, quantity, and discount. Discount is 0 by default, in case there is no discount
def calculator(price, quantity, discount=0):

    total=price*quantity

    #converts discount parameter from whole percentage to decimal percentage
    discount=discount/100
    
    #if discount is not 0, the total is reduced by the percentage of the discount
    if discount>0:
        total=total-(total*discount)
    
    #returns the total variable
    return total

#prints result of calculator using three $20 items and a 10% discount
print(calculator(20, 3, 10))