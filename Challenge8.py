"""
Challenge 8

Write a program that:
converts and outputs marks into grades, using the following data:

"""

print ("Welcome to Challenge 8")

score = int ( input ("Please enter your score: "))

if score >= 75:
    print (" You got an A")
elif score >=60 and score < 75:
    print ("You got a B")
elif score >= 35 and score < 60:
    print ("You got a C")
elif score < 35:
    print ("You got a D for dumbass")