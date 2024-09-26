#Prints the intro
print("""
Welcome to the To-Do tracker!
""")

#Placeholder for task list
list=[]

#Makes program run indefinitely
while True:
    def print_list():
        if list==[]:
            print("""Your list is currently empty!
    """)
        else:
            print(f"""
    Your tasks:{list}
    """)        
        
    #Function for adding item
    def add():
        if choice==1:
            try:
                list.append(str(input("""What would you like to add?: 
    """)))
            except:
                print("Invalid choice! Please try again")

    #Function for deleting item
    def delete():
        if choice==2:
            try:
                delete_choice=int(input("""Which task number to remove?: 
    """))
            except:
                print("Invalid choice! Try again")
                delete()
            try:
                del(list[delete_choice-1])
            except:
                print("Invalid choice! Try again")
                delete()

    #Function for deciding what to do with program
    def prompt():
        global choice
        try:
            choice=int(input("""What would you like to do?

        1:Add task
        2:Remove task
        """))
            print(" ")
        except:
            print("Invalid choice! Please try again")
        if choice==1:
            add()
        elif choice==2:
            delete()
    print_list()
    prompt()



