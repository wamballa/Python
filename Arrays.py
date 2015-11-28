__author__ = 'wamballa'

import random

#define array

slot = [ "P" , "-" , "-" , "-" , "-" , "-" , "-" , "-"     # 0 1 2
        ,"-" , "-" , "-" , "-" , "-" , "-" , "-" , "-"     # 3 4 5
        ,"-" , "-" , "-" , "-" , "-" , "-" , "-" , "-"
         ,"-" , "-" , "-" , "-" , "-" , "-" , "-" , "-"
         ,"-" , "-" , "-" , "-" , "-" , "-" , "-" , "-"
         ,"-" , "-" , "-" , "-" , "-" , "-" , "-" , "-"
         ,"-" , "-" , "-" , "-" , "-" , "-" , "-" , "-"
         ,"-" , "-" , "-" , "-" , "-" , "-" , "-" , "-"]   # 6 7 8
#Player setup
playerPos = 0
score = 0

# Setup Bandit Position
banditPos = [0,0,0,0,0]
temp = random.randint (0,63)
for i in range (5):
    while temp in banditPos or playerPos == temp:
        temp = random.randint (0,63)
    banditPos[i] = temp
    slot[banditPos[i]] = "B"
# Setup Chest Position
chestPos = [0,0,0,0,0,0,0,0,0,0] #5 # 10 chests
for i in range (10):
    while temp in chestPos or playerPos == temp:
        temp = random.randint (0,63)
    chestPos[i] = temp
    slot[chestPos[i]] = "C"

counter = 0

def printMaze():
    global counter
    for i in range (0,8):
        for x in range(0,8):

            print ("%s" % (slot [counter]),end="")
            counter += 1;
        print ("")
    counter = 0

def checkforBandit():
    global banditPos
    global playerPos
    global score
    print ("PP = %s  BP = %s" % (playerPos, banditPos[1]))
    if playerPos == banditPos[1]:
        print ("HIT BANDIT")
        score = 0
        newPos = random.randint (0,64)
        while newPos == playerPos:
            newPos = random.randint (0,64)
        banditPos[1] = newPos
        slot [banditPos[1]] = "B"
        #printMaze()

    print ("Score = %s" % score)
printMaze()

while True:
    move = input ("L R U P")

    if move == "R" or move =="r":

        slot [playerPos] = "-"
        playerPos += 1
        score += 5
        slot [playerPos] = "P"
        checkforBandit()
        printMaze()

    if move == "L" or move == "l":
        slot [playerPos] = "-"
        playerPos -= 1
        score += 5
        slot [playerPos] = "P"
        checkforBandit()
        printMaze()

    if move == "D" or move == "d" and playerPos <56:
        slot [playerPos] = "-"
        playerPos += 8
        score += 5
        slot [playerPos] = "P"
        checkforBandit()
        printMaze()

    if move == "U" or move == "u" and playerPos > 8:
        slot [playerPos] = "-"
        playerPos -= 8
        score += 5
        slot [playerPos] = "P"
        checkforBandit()
        printMaze()