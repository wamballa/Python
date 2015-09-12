"""
Challenge 28

Write a random name generator that asks for the user to input 5 names,
stores them in an array and then outputs one of them at random.

Variables, Repetition, Arrays

"""
import random  # import random module to use random function

name = []  # create name array

for i in range(0, 5):
    name.append(input("Enter name %s of 5: " % (i + 1)))  # apend names to array name[]

print("\nYour random name is %s" % name[random.randint(0, 4)])  # print name from random position 0 to 4
