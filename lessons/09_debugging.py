#Second problem
#text = "Hello, world, my name is"
#count = 0

#for char in text:
#    if char == " ":
#       count += 1

#print(count)

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
  result = 1
  for i in range(11):
    result *= i   

  print("Factorial of " + num + "is" + result)