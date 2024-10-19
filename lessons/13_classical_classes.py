"""
Task 0: Class We-dDo

Create a class  for a video game character, that tracks its health,
    - Create methods for damage

    Then create a subvlass called"player" that has more health
    - Create a method for healing
"""

class Charater:
    health = 20

    def __init__(self, name):
        self.name=name
    
    def damage(self, dmg=1):
        self.health-=dmg

class Player(Charater):
    health=50

    def heal(self):
        if self.health<50:
            self.health+=1

enemy1 = Charater("Ywch")
enemy1.damage()

print(enemy1.health)

player=Player("Kerdon")
player.heal()

print(player.health)


"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

#created class Person
class Person:

    #initializes class with name and age parameters
    def __init__(self, name, age):
        self.name=name
        self.age=age

    #defined introduce method that prints a string containing self.name and self.age
    def introduce(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old.")


#defines a new variable using the Person class with "Kerdon" as the name and 16 as the age
kerdon=Person("Kerdon", 16)

#runs the introduce method for the kerdon object
kerdon.introduce()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

#class defined Animal
class Animal:

    #empty method called speak with pass as placeholder
    def speak(self):
        pass
   
#subclass of Animal called Dog
class Dog(Animal):

    #speak method modified to print "Woof!"
    def speak(self):
        print("Woof!")
        
#subclass of Animal called Cat
class Cat(Animal): 

    #speak method modified to print "Meow!"
    def speak(self):
        print("Meow!")

#defines Lucy as subclass cat
Lucy=Cat()

#runs the speak method for Lucy
Lucy.speak()



"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

#class defined BankAccount
class BankAccount:

    #initialization function, calling for attributes balance and owner
    def __init__(self, balance, owner):
        self.balance=balance
        self.owner=owner
    
    #Defines withdrawal function calling for arguments money.
    def withdraw(self, money):

        #Subtracts given argument "money" from the balance attribute
        self.balance-=money

    #Defines deposit function calling for arguments money.
    def deposit(self, money):

        #Adds given argument "money" from the balance attribute
        self.balance+=money

#Defines account as class BankAccount with 300 as balance and Kerdon as owner
account=BankAccount(300, "Kerdon")

#Calls withdraw method to withdraw $100. Prints new balance
account.withdraw(100)
print(f"${account.balance}")

#Calls withdraw method to deposit $25. Prints new balance
account.deposit(25)
print(f"${account.balance}")

