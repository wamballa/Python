"""
Challenge 18

Write a program that:
asks the user to input a number
outputs the times table for that number

"""

print ("Times Table ")

table = int(input("Enter the number of the times table to show: "))
for i in range (1, 13): # repeat 1 to 12
    print ("%s x %s = %s" % (i,table,(i*table)))