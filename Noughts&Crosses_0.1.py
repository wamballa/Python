winning_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


winning_lines [1] = 3

print ( winning_lines[])


####################################################################################
# Setup global variables
####################################################################################
slot = [ "-" , "-" , "-"    # 0 1 2
        ,"-" , "-" , "-"    # 3 4 5
        ,"-" , "-" , "-"]   # 6 7 8
gameOver = False

#####################################################################################
# draw board in two parts. left is guide for the slot number, right is the game board
#####################################################################################
def drawBoard():
    print ("Slot number    Game Board")
    for row in range ( 0,3 ): # go down row by row
        rowStart = row * 3 # starting point in the list "sort" of each row
        print ("%s %s %s          " % ( rowStart, rowStart+1,rowStart+2),end="") # prints slots numbers

        for col in range ( 0,3 ): # now go along each column
            print ("%s  " % slot[rowStart+col],end="") # print contents of each row
        print("")

#####################################################################################
# sets the slot list to empty = replaces each slot with a -
#####################################################################################
def resetBoard():
    global slot # cannot change a global variable in a function without this
    slot = ["-","-","-","-","-","-","-","-","-"]

#####################################################################################
# check each turn to see if player has won a line/diagonal
#####################################################################################
def checkWin():
    global gameOver

    # check if any rows are all X or O
    for row in range ( 3 ):
        checkSlot = row*3 # starting point for each row in the list "slot"
        if slot[checkSlot]!="-" and slot[checkSlot] == slot[checkSlot+1] and slot[checkSlot+1]==slot[checkSlot+2]:
            gameOver = True # if all the same then game is over
            if slot[checkSlot]=="X":
                print ("\n Congrats. Player X has won the game by capturing a row.")
                drawBoard() # draw the board with the winning line in it
            else:
                print ("\n Congrats. Player O has won the game by capturing a row.")
                drawBoard() # draw the board with the winning line in it
            resetBoard()
            return

    # check if any diagonal \ are matching
    if slot[0] != "-":
        if slot[0] == slot[4] and slot[4] == slot[8]:
            gameOver = True
            if slot[0] == "X":
                print ("\n Congrats. Player X has won the game by capturing a diagonal.")
                drawBoard()
            else:
                print ("\n Congrats. Player O has won the game by capturing a diagonal.")
                drawBoard()
            resetBoard()
            return

    # check if any diagonal / are matching
    if slot[2] != "-":
        if slot[2] == slot[4] and slot[4] == slot[6]:
            gameOver = True
            if slot[2] == "X":
                print ("\n Congrats. Player X has won the game by capturing a diagonal.")
                drawBoard()
            else:
                print ("\n Congrats. Player O has won the game by capturing a diagonal.")
                drawBoard()
            resetBoard()
            return


######################################################################################
# Main loop - start game
######################################################################################

drawBoard() # draw the board to start

while True: # infinit game loop / no end to the game

    while True: # loop created to capture Player X input. Checks input is valid and breaks out of loop
        playerSlot = int ( input ("Player X: Enter slot number: "))
        if playerSlot <=8 and playerSlot>=0 and slot[playerSlot] == "-":
            slot[playerSlot] = "X"
            checkWin()
            if not gameOver:
                drawBoard()
            break
        elif playerSlot <=8 and playerSlot>=0 and slot[playerSlot] != "-":
            print ("Slot taken!! Try again...")
        elif playerSlot >8 or playerSlot<0: # checks if numbers entered are between 0 and 8
            print ("Enter slot number between 0 and 8")

    while True and not gameOver: # loop created to capture Player O input. Checks input is valid & game not over and breaks out of loop
        playerSlot = int ( input ("Player O: Enter slot number: "))
        if playerSlot <=8 and playerSlot>=0 and slot[playerSlot] == "-":
            slot[playerSlot] = "O"
            checkWin()
            if not gameOver:
                drawBoard()
            break
        elif playerSlot <=8 and playerSlot>=0 and slot[playerSlot] != "-":
            print ("Slot taken!! Try again...")
        elif playerSlot >8 and playerSlot<0: # checks if numbers entered are between 0 and 8
            print ("Enter slot number between 0 and 8")


    if gameOver == True:
        gameOver = False
        print ("\nStart Another Game...clear the board!!")
        drawBoard()