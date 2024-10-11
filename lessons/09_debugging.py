#Second problem
text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":
       count += 1

print(count)

#Third problem
print("give me a number")
n = int(input())+1

for num in range(1, n):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

#Fourth problem
num = int(input("Enter an integer: "))

if num <= -1:
  print("No negative numbers.")
else:
  result = num
  for i in range(1,11):
    result *= i   

  print("Factorial of " + num + "is" + result)

#fifth problem
attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts == 3:
        print("Too many attempts")
        break