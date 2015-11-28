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
banditPos = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]  # up to 15 bandits
numberofBandits = 5
temp = random.randint (0,63)
for i in range (numberofBandits):
    while temp in banditPos or playerPos == temp:
        temp = random.randint (0,63)
    banditPos[i] = temp
    slot[banditPos[i]] = "B"
# Setup Chest Position
chestPos = [0,0,0,0,0,0,0,0,0,0] #5 # 10 chests
chestHit = [0,0,0,0,0,0,0,0,0,0]
temp = random.randint (0,63)
for i in range (10):
    while temp in chestPos or playerPos == temp or temp in banditPos:
        temp = random.randint (0,63)
    chestPos[i] = temp
    slot[chestPos[i]] = "C"

counter = 0
########################################
def printMaze():
    global counter
    for counter in range (64):
        if counter % 8 == 0:
            print("")
        if counter in chestPos and counter != playerPos:
                print ("C",end="")
        else:
                print ("%s" % (slot [counter]),end="")
    print ("\nScore = %s" % score)

################################
def checkforBandit():
    global banditPos
    global playerPos
    global score
    #print ("PP = %s  BP = %s" % (playerPos, banditPos[1]))

    if playerPos in banditPos:
        print ("HIT BANDIT")
        score = 0
        newPos = random.randint (0,63)
        while newPos == playerPos:
            newPos = random.randint (0,63)
        t = banditPos.index( playerPos )
        banditPos[t] = newPos
        slot [banditPos[t]] = "B"
        #printMaze()

    #print ("Score = %s" % score)

###############################
def spawnBandit():
    global banditPos, playerPos, chestPos, numberofBandits
    if numberofBandits <=15:
        temp = random.randint (0,63)
        while temp in chestPos or temp == playerPos or temp in banditPos:
            temp = random.randint (0,63)
        banditPos [numberofBandits]=temp
        slot[temp]="B"
        numberofBandits += 1

###############################

def checkChest():
    global banditPos
    global playerPos
    global score
    global chestPos, chestHit

    for i in range (10):
        if chestPos[i] == playerPos:
            score += 10
            chestHit[i] += 1
        if chestHit[i] >= 3:
            spawnBandit() #####################################################################
            chestPos[i] = -1
            chestHit[i] =0
    for i in range(10):
        print (" %s " % chestHit[i],end="")
    print ("")


#Main Loop
printMaze()

while True:
    move = input ("\nL R U P")

    if move == "R" or move =="r":

        slot [playerPos] = "-"
        playerPos += 1
        slot [playerPos] = "P"
        checkforBandit()
        checkChest()
        printMaze()

    if move == "L" or move == "l":
        slot [playerPos] = "-"
        playerPos -= 1
        slot [playerPos] = "P"
        checkforBandit()
        checkChest()
        printMaze()

    if move == "D" or move == "d" and playerPos <56:
        slot [playerPos] = "-"
        playerPos += 8
        slot [playerPos] = "P"
        checkforBandit()
        checkChest()
        printMaze()

    if move == "U" or move == "u" and playerPos >= 8:
        slot [playerPos] = "-"
        playerPos -= 8
        slot [playerPos] = "P"
        checkforBandit()
        checkChest()
        printMaze()