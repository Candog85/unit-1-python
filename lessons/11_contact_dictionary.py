#defines empty dictionary
contacts=dict()

#intro text
print("Welcome to the Contact Dictionary")

#function defined for displaying the options of the script
def options():
    print()
    print(
    """1: Add contact
2: Delete contact
3: List contacts
4: Exit"""
)
    print()

#function defined for handling errors in the program
def error():

    #prints error message
    print("Invalid choice, try again!")

    #displays options
    options()

    #prompts the user
    prompt(input("Enter your choice: "))

#function defined for listing the contacts in the dictionary 
def list():

    #if the contacts dictionary is empty:
    if contacts=={}:

        #notify the user
        print()
        print("Your contact list is empty")
        print()

        #prompt the user
        prompt(input("Enter your choice: "))
    
    #otherwise:
    else:

        #prints Contacts:
        print()
        print("Contacts:")
        print()

        #for every contact in the dictionary:
        for contact in contacts:

            #prints the key and value of each item, separated by a colon
            print(f"{contact}: {contacts[contact]}")
        print()

        #prompt the user
        prompt(input("Enter your choice: "))

#function defined for adding contacts to the list with name and number as parameters
def add_contact(name, number):

    #tries to run:
    try:

        #convert name to string
        name=str(name)

        #convert number to integer
        number=int(number)
    
    #if the above fails:
    except:

        #runs error function
        error()

    #If the length of number is not 10 or number is not a whole integer:
    if len(str(number))!=10 or type(number)!=int:

        #runs error function
        error()
    
    #appends to dictionary by creating a new key (name) and assigning it a new value (number)
    contacts[name]=[number]

    #runs options function and prompts user
    options()
    prompt(input("Enter your choice: "))  

#function for deleting a contact with option as parameter
def delete_contact(option):

    #tries to:
    try:
        #delete the contacts dictionary item with the key of option
        del contacts[option]

        #runs options function
        options()

        #prompts user
        prompt(input("Enter your choice: "))

    #if the above fails:
    except:

        #run error function
        error()

#function for prompting user with choice as parameter
def prompt(choice):

    #tries to:
    try:
        #convert choice into integer
        choice=int(choice)
    
    #if the above fails:
    except:

        #runs error function and prompts user
        error()
        prompt(input("Enter your choice: "))

    #if choice is 1:
    if choice==1:

        #runs the add_contact function and takes input as parameters
        add_contact(input("What is the name of the contact?: "), input("What is the contact's number?: "))

    #if choice is 2:
    elif choice==2:

        #runs the delete_contact function and takes input as parameter
        delete_contact(input("What would you like to delete?: "))

    #if choice is 3:
    elif choice==3:

        #runts the list function
        list()

    #if choice is 4:
    elif choice==4:
        #runs the exit function, stopping the program
        exit()
    
    #else, runs error function
    else:
        error()

#runs the options function and prompts user as soon as the script is run
options()
prompt(input("Enter your choice: "))
