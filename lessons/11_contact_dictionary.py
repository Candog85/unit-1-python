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

def list():

    if contacts=={}:
        print()
        print("Your contact list is empty")
        print()
        prompt()
    
    else:
        print()
        print("Contacts:")
        print()
        for contact in contacts:
            print(f"{contact}: {contacts[contact]}")
        print()
        prompt()

def add_contact():
    try:
        print()
        contacts[str(input("What is the name of the contact?: "))]=str(input("What is the contact's number?: "))
        if len()
        print()
        prompt()        
    except:
        print("Invalid choice, try again")
        add_contact()


def delete_contact():
    try:
        print()
        del contacts[str(input("What would you like to delete?: "))]
        prompt()
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
    elif choice==3:
        list()

prompt()
