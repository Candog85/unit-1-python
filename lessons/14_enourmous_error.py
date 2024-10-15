"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except:
        print("You cannot divide by 0!")

# Example usage:
divide_numbers(10, 0)


"""
Example 2: Opening Files
"""

def read_file(filename):
    file = open(filename, 'r')
    contents = file.read()
    print("File contents:", contents)
    file.close()

# Example usage:
try:
    read_file("nonexistent.txt")
except:
    print("Invalid file name!")

"""
Example 3: List Items
"""

def get_item(lst, index):
    item = lst[index]
    print("Item:", item)

# Example usage:
my_list = [1, 2, 3]

try:
    get_item(my_list, 5)
except:
    print("Invalid list or list index")


"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    value = dictionary[key]
    print("Value:", value)

# Example usage:
my_dict = {"a": 1, "b": 2}

try:
    get_value(my_dict, "c")
except:
    print("Invalid dictionary or dictionary key")


"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        print("Your file was processed")
    finally:
        print("Thank you for using the program")

# Example usage:
process_file("example.txt")