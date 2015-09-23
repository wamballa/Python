"""

Noughts and Crosses

"""


slot = ["-","-","-","-","-","-","-","-","-"]
numCols = 3
numRows = 3
gameOver = False

def drawBoard():
    print ("Slot number    Game Board")
    for row in range ( numRows ):
        rowStart = row*numCols +1
        print ("%s %s %s          " % ( rowStart, rowStart+1,rowStart+2),end="")
        for col in range ( numCols ):
            print ("%s  " % slot[( row * numCols)+col],end="")
        print("")

def resetBoard():
    global slot
    slot = ["-","-","-","-","-","-","-","-","-"]
    #drawBoard()

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
                print ("\n Congrats. Player X has won the game by capturing a row.")
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
# Main

drawBoard()

while True:
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

    while True and not gameOver:
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


