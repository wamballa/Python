"""

Noughts and Crosses

Overview:

Players: 2 players = X and O
Inputs: each player enters a slot number to put X or O into.Slots arranged:
1 2 3
4 5 6
7 8 9
Variables: slot[] = list length is 9 [0..8] and holds contents for each slot. Either - (empty), X or O

Functions:
drawBoard() - draws the slot numbers the user must enter and the contents of each slot ( from list called slot )
resetBoard() - clears the list called slot filling it with -
checkWin() - check if player has 3 in a row, column or diagonal /\


"""

# Setup global variables
slot = ["-","-","-","-","-","-","-","-","-"]
numCols = 3
numRows = 3
gameOver = False

# draw board in two parts. left is guide for the slot number, right is the game board
def drawBoard():
    print ("Slot number    Game Board")
    # prints row by row
    for row in range ( numRows ): # go row by row
        # first draw the number of the slots user needs to enter
        rowStart = row*numCols +1 #calculate


        print ("%s %s %s          " % ( rowStart, rowStart+1,rowStart+2),end="")
        for col in range ( numCols ):
            print ("%s  " % slot[( row * numCols)+col],end="")
        print("")

# sets the slot list to empty = replaces each slot with a -
def resetBoard():
    global slot # cannot change a global variable in a function without this
    slot = ["-","-","-","-","-","-","-","-","-"]

def checkWin():
    global gameOver

    # check if any rows are matching
    for row in range ( numRows ):
        checkSlot = row*numCols
        if slot[checkSlot]!="-" and slot[checkSlot] == slot[checkSlot+1] and slot[checkSlot+1]==slot[checkSlot+2]:
            gameOver = True
            if slot[checkSlot]=="X":
                print ("\n Congrats. Player X has won the game by capturing a row.")
                drawBoard()
            else:
                print ("\n Congrats. Player O has won the game by capturing a row.")
                drawBoard()
            resetBoard()
            return

    # check if any columns are matching
    for col in range (numCols ):
        checkSlot = col #*numRows
        if slot[checkSlot]!="-" and slot[checkSlot] == slot[checkSlot+numRows] and slot[checkSlot+numRows]==slot[checkSlot+numRows*2]:
            gameOver = True
            if slot[checkSlot]=="X":
                print ("\n Congrats. Player X has won the game by capturing a column.")
                drawBoard()
            else:
                print ("\n Congrats. Player O has won the game by capturing a column.")
                drawBoard()
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


# Main loop - start game

drawBoard() # draw the board to start

while True: # infinit game loop / no end to the game

    while True:
        playerMove = int ( input ("Player X: Enter slot number: "))
        if slot[playerMove -1] == "-":
            slot[playerMove -1] = "X"
            checkWin()
            if not gameOver:
                drawBoard()
            break
        else:
            print ("Slot taken!! Try again...")

    while True and not gameOver: # dont ask for input from player if game is over / True
        playerMove = int ( input ("Player O: Enter slot number: "))
        if slot[playerMove -1] == "-":
            slot[playerMove -1] = "O"
            checkWin()
            if not gameOver:
                drawBoard()
            break
        else:
            print ("Slot taken!! Try again...")


    if gameOver == True:
        gameOver = False
        print ("\nStart Another Game...clear the board!!")
        drawBoard()


