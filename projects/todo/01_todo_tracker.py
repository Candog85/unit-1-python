#Prints the intro
print("""
Welcome to the To-Do tracker!
All changes are saved automatically
""")

#Placeholder for task list
list=[]

#Reads contents of the todo list saved in the text file
with open("projects/todo/todo.txt", "r") as file:
    list=file.readlines()

#Function for updating list by writing to an external file.
def update():
    with open("projects/todo/todo.txt", "w") as file:
            file.writelines(list)

#Function for printing list
def print_list():

    #If list is empty, tell the user
    if list==[]:
        print("""Your list is currently empty!
""")
        
    #Otherwise:
    else:
        print("""
Your tasks:
""")
        #For every item in the list:
        for items in list:

            #Print the index of the item plus one, followed by the item's value itself
            print(f"{list.index(items)+1}: {items}")
            print()

#Function for adding item
def add():

    #Tries to append user input to list
    try:
        list.append(str(input("""What would you like to add?: 
"""))+"\n")
        update()
        
        
    #If theres an error, prints and restarts function
    except:
        print("Invalid choice! Please try again")
        add()

#Function for deleting item
def delete():

    #Tries to take input for the index of the item being deleted
    try:
        delete_choice=int(input("""Which task number to remove?: 
"""))
        update()
    
    #If error, restarts function:
    except:
        print("Invalid choice! Try again")
        delete()
    
    #Tries to delete the list item of the inputted index
    try:
        del(list[delete_choice-1])
    
    #If error, restarts function
    except:
        print("Invalid choice! Try again")
        delete()

#Function to clear list
def clear_list():

    #Clears list and notifies user
    list.clear()
    update()
    print("Your list haas been cleared!")
    print()

#Function for deciding what to do with program
def prompt():

    #Tries to take input for what to do to list (as integer)
    try:
        choice=int(input("""What would you like to do?

1: Add task
2: Remove task
3: Clear list
4: End program
                            
:"""))
        print()
    
    #If error, restarts
    except:
        print("Invalid choice! Please try again")
        prompt()
    
    #If user inputs 1, runs add function
    if choice==1:
        add()

    #If user inputs 2, runs delete function
    elif choice==2:
        delete()

    #If user inputs 3, runs clear_list function
    elif choice==3:
        clear_list()

    #If user inputs 4, ends the program using the quit function
    elif choice==4:
        print("Thank you for using the To-Do tracker!")
        quit()

#Makes program run indefinitely
while True:
    print_list()
    prompt()