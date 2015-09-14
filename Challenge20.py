"""
Challenge 20

Write a program that:
asks the user to input a number and repeats until they guess the number 7
congratulate the user with a Well Done message when they guess correctly

"""

print ("Number guessing game")

answer = int(input("Guess the number between 0 and 20. Enter your number: "))

while answer != 7:
    answer = int(input("Wrong. Try again. Enter your number: "))

print ("Well done. You guessed the number 7 correctly!!!")