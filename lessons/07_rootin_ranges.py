"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

#For every number from 1 ending on 11, print the iteration number
for nums in range(1,11):
    print(nums)


"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

#For every 10th number from 1 ending on 1001, print the iteration number
for nums in range(900,1001,10):
    print(nums)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""

#For every 9th number from 1 ending in 101, print the iteration number
for nums in range(1,101,9):
    print(nums)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

#Placeholder value for sum
sum=0

#For every number between 1 and 11
for nums in range(1,11):

    #Add the number to the sum (Initially 0), and prints it
    sum=sum+nums
    print(sum)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

#Defines rows as 5
rows = 5

#for every number in range of rows (5):
for i in range(rows):

    #For every number+1 in range of rows:
    for j in range(i + 1):

        #Prints an asterisk, prevents a new line from being printed per iteration
        print('*', end=' ')

    #Prints the result in each iteration of the first for loop
    print()
