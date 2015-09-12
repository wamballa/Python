__author__ = 'wamballa'

"""
Challenge 28

Write a program that allows the user to create and store a checklist for a holiday.
It should start by asking them the destination of the holiday, how many things they
need to pack and how many tasks they need to complete to prepare.

The user should then be able to enter each item they need to pack and each task they need to complete.
"""

itemList = []
taskList = []

holidayDestination = input ("Please tell me where you're going on holiday: ")
numberOfItems = int(input ("Please tell me how many items you'll take with you: "))
numberOfTasks = int(input ("Please tell me how many tasks you need to prepare: "))

file = open("%s.txt" % holidayDestination, "a")  # open file to append to
file.write ("My %s holiday\n\n" % holidayDestination)

print ("\nNow you can enter your holiday items you will take with you.\n")
file.write ("Here are the %s items to take:\n" % (numberOfItems))

for i in range (0,numberOfItems):
    itemList.append (input("Tell me item %s you will take: " % (i+1)))
    file.write ("%s. %s\n" % (i,itemList[i]))

print ("\nNow you can enter your holiday tasks you need to do.\n")
file.write ("\nHere are the %s tasks to do:\n" % (numberOfTasks))

for i in range (0,numberOfTasks):
    taskList.append (input("Tell me task %s you will take: " % (i+1)))
    file.write ("%s. %s\n" % (i,taskList[i]))

print ("\nYour holiday items and tasks have been saved to file %s.txt.\n" % (holidayDestination))