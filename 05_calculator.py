print(
    """
    Welcome to the Calculatinator V2 Premium 
    (Bathed in light, Promised Consort)
    """
)

def input_1():
    global num_1
    try:
        num_1=float(input("Enter your first number: ").strip())
    except:
        ("Invalid number")
        input_1()
input_1()

def input_2():
    global num_2
    num_2=float(input("Enter your second number: ").strip())

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

