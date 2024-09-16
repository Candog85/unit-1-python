#Step 1: Create a new file called "lesson_00.py"

#Step 2: Print your name to the console
print("Kerdon Chapman")

#Step 3: Favorite Show:
fav_show = "The It Crowd"

#Step 4: Create a float and integer variable using snake casing
float_var = 3.14
int_var = 1000

#Step 5: Print the product of the last two varibles
print(float_var * int_var)

#Step 6: Create a variable that stores your favorite food
fav_foods = ["Pepper Pot", "Pizza", "Fries" ]

#Step 7: Create an if statement that tells someone if they can get a drivers liscence\

age=18

permit=True

if (age >= 18) and (permit==True):
    print("You can get a liscence!")
elif (age<18):
    print("You're not old enough!")
else:
    print("You're not qualified!")

#Step 8: Ask a user for their name and print it to the console
name=str(input("What's your name?: "))
print("Your name is "+name+", eh?")

#Step 9: Create a loop that prints each of your favorite foods
for x in fav_foods:
    print(x)

#Step 10: Create a while loop that will never run:
while 1==2:
    print("MATH IS FAKE")