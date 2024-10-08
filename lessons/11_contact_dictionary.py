global choice
contacts=dict()

print("Welcome to the Contact Dictionary")
print()

def options():
    print(
    """1: Add contact
2: Delete contact
3: List contact
4: Exit"""
)
    print()

def update():

    if contacts=={}:
        print("Your contact list is empty")
        print()
    
    else:
        print("Contacts:")
        print()
        for contact in contacts:
            print(f"{contact}: {contacts[contact]}")
        print()
        prompt()

def add_contact():
    try:
        contacts[str(input("What is the name of the contact?: "))]=str(input("What is the contact's number?: "))
        update()
    except:
        print("Invalid choice, try again")
        add_contact()


def delete_contact():
    try:
        del contacts[str(input("What would you like to delete?: "))]
        update()
    except:
        print("Invalid choice, try again")
        delete_contact()


def prompt():
    options()
    global choice
    try:
        choice=int(input("Enter your choice: "))
    except:
        print("Invalid choice, try again")
        prompt()

    if choice==1:
        add_contact()
    elif choice==2:
        delete_contact()
prompt()
