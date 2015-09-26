"""
Challenge 20

Write a program that:
asks the user to input a number and repeats until they guess the number 7
congratulate the user with a Well Done message when they guess correctly
"""
print("Guess The Number")
answer=0
while answer!=7:
    answer=int(input("What is the number?"))

print("Congrats you guessed the number!")


