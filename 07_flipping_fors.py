"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

#Defines string
string="Im so happy"

#For each letter in string, print the letter
for letters in string:
    print(letters)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

#Define list and placeholder for sum
list_var=[1,2,3,4,5]
sum_var=0

#For each number in the list, add that number to the sum variable and print it
for number in list_var:
    sum_var=sum_var+number
    print(sum_var)
    

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

#Takes user input for sentence, splits it into list.
sentence=input("Enter your sentence: ").split()

#For each word in the sentence, print the length of the word
for words in sentence:
    print(len(words))


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

#Defines dictionary with 5 items    
dictionary={
    "Banana":"Fruit",
    "Apple":"Fruit",
    "Lettuce":"Vegetable",
    "Tomato":"Fruit",
    "Orange":"Fruit",
}

#Prints the key of each item in the dictionary
for items in dictionary:
    print(items)

#I expected that the value of each key would be printed instead of the key