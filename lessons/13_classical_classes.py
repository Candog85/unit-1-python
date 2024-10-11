"""
Task 0: Class We-dDo

Create a class  for a video game character, that tracks its health,
    - Create methods for damage

    Then create a subvlass called"player" that has more health
    - Create a method for healing
"""

# class Charater:
#     health = 20

#     def __init__(self, name):
#         self.name=name
    
#     def damage(self, dmg=1):
#         self.health-=dmg

# class Player(Charater):
#     health=50

#     def heal(self):
#         if self.health<50:
#             self.health+=1

# enemy1 = Charater("Ywch")
# enemy1.damage()

# print(enemy1.health)

# player=Player("Kerdon")
# player.heal()

# print(player.health)


"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

# #created class Person
# class Person:

#     #initializes class with name and age parameters
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     #defined introduce method that prints a string containing self.name and self.age
#     def introduce(self):
#         print(f"Hello my name is {self.name} and i am {self.age} years old.")


# #defines a new variable using the Person class with "Kerdon" as the name and 16 as the age
# kerdon=Person("Kerdon", 16)

# #runs the introduce method for the kerdon object
# kerdon.introduce()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

#
class Animal:
    def speak(self):
        ""
   
class Dog(Animal):
    def speak(self):
        print("Woof!")
        

class Cat(Animal):  
    def speak(self):
        print("Meow!")

Lucy=Cat()

Lucy.speak()



"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""