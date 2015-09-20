"""
Challenge 10

Write a game that:
allows the user to play rock, paper, scissors against the computer must display the computers
choice and show the result of the game

Tip:	The computers answer must be random.

"""

import random  # import random module to use random function

rock = 1
paper = 2
scissors = 3

object = [" ","rock","paper","scissors"]

def checkWinner (playerChoice):
    computerChoice = random.randint(1, 3)
    print("Player: %s     Computer: %s" % (object[playerChoice],object[computerChoice]))
    if playerChoice == computerChoice:
        print ("It's a Draw!!")

    elif playerChoice==rock and computerChoice==scissors:
        print("Player Wins!!")
    elif playerChoice==paper and computerChoice== scissors:
        print ("Player Loses!!")

    elif playerChoice==rock and computerChoice== paper:
        print ("Player Loses!!")
    elif playerChoice==scissors and computerChoice== paper:
        print ("Player Wins!!")

    elif playerChoice==paper and computerChoice== rock:
        print ("Player Wins!!")
    elif playerChoice==scissors and computerChoice== rock:
        print ("Computer Wins!!")

print ("Welcome to Rock, Paper, Scissors")
print ("Rules: Scissors beats Paper, Paper beats Rock, Rock beats Scissor")

while True:
    checkWinner (int(input("1. Rock\n2. Paper\n3. Scissors\nChoose now: ")))
