"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

global list_var

#Creates a list
list_var=["item 1", "item 2", "item 3", "item 4"]

#prints said list
print(list_var) 

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

#Appends item 5 prints updated
list_var.append("item 5")
print(list_var)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

#Deletes first item, prints updated list
list_var.remove("item 1")
print(list_var)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

#Replaces item index 1 in the list
list_var[1]="replaced item"
print(list_var)

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

#Appends one item, then the next
list_var.append("multi append 1")
list_var.append("multi append 2")

#Prints updated list
print(list_var)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

#Deletes the item of index 1 and prints the updated list
del list_var[2]
print(list_var)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
#Combines fist and second index of the original list into a new list and prints it
new_list=[list_var[0], list_var[1]]
print(new_list)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

#Combines original and new list into the original list and prints
list_var=list_var+new_list
print(list_var)