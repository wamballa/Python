"""
Challenge 19

Write a program that:
asks the user to input a number
outputs the times table for that number
starts again every time it finishes

"""

print ("Times Table ")

while True: # create a loop that starts again every time it finishes
    table = int(input("Enter the number of the times table to show: "))
    for i in range (1, 13): # repeat 1 to 12
        print ("%s x %s = %s" % (i,table,(i*table)))
