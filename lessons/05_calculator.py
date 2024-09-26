#Prints intro text
print(
    """
    Welcome to the Calculatinator V2 Premium 
    (Bathed in light, Promised Consort)
    """
)

#Function for deciding what operation to perform
def option_func():

    #Global'd option to be used later
    global option

    #Prints the options for operation, and takes integer input to decide
    option = int(input(
        """
        What operation would you like?

        1: Addition
        2: Subtraction
        3: Multiply
        4: Division
        5: Floor Division
        6: Exponential
        7: Remainder

        Enter Choice: """
    ))

    #If the input isn't 1-7, error is printed and function is restarted
    if option>7 or option<1:
        print("Invalid choice!: ")
        option_func()

#Initial iteration
option_func()

#Function for deciding the two numbers to calculate with
def input_func():

    #Global'd nums to be used later
    global nums

    #Try is used to check if the input is valid
    try:

        #Input for both numbers to calculate is taken, stripped, made a float, and added as first two items in list
        nums=[
            float(input("Enter your first number: ").strip()),
            float(input("Enter your second number: ").strip())
            ]
    
    #If an error occurs in the try above, the input must be a string or boolean, and an error is printed likewise
    except:
        print("Invalid number. You may have used a string")
        input_func()

#Initial iteration
input_func()


#Checks the operation through the value of options, and uses the first and second items in the number lists to calculate accordingly

#Addition
if option==1:
    result=nums[0]+nums[1]
    print(f"Result: {result}")

#Subtraction
elif option==2:
    result=nums[0]-nums[1]
    print(f"Result: {result}")

#Multiplication
elif option==3:
    result=nums[0]*nums[1]
    print(f"Result: {result}")

#Division
elif option==4:
    result=nums[0]/nums[1]
    print(f"Result: {result}")

#Floor Division
elif option==5:
    result=nums[0]//nums[1]
    print(f"Result: {result}")

#Exponents
elif option==6:
    result=nums[0]**nums[1]
    print(f"Result: {result}")

#Remainder (modulo)
elif option==7:
    result=nums[0]%nums[1]
    print(f"Result: {result}")

