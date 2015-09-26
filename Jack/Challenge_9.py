"""
Challenge 9

Write a program that:
asks the user to name one of the Olympic Values (Respect, Excellence and Friendship)
if they correctly name one, output Thats correct, otherwise output Try again
"""

ans=input("Name a olympic value")
if ans=="respect":
    print("Correct!")
elif ans=="excellence":
    print("Correct!")
elif ans=="friendship":
    print("Correct!")
elif ans!="":
    print("Incorrect")

