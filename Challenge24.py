"""
Challenge 24
Write a function that takes two numbers.
The first number indicates the number of spaces that should be displayed and the second indicates
the number of Xs that should be displayed. These should both be displayed on the same line.
Now write another function that makes multiple calls to your first function and draws a picture with Xs.
"""

def drawText (numSpaces,numX):

    for space in range (0, numSpaces):
        print (" ", end="") # comma after print stops printing to new line

    for x in range (0, numX):
        print ("X", end="")


def drawPicture():

    drawText (10,1)
    drawText (9,2)
    drawText (8,3)
    drawText (8,4)
    drawText (6,5)
    drawText (5,6)
    drawText (4,7)
    drawText (3,8)
    drawText (2,9)
    drawText (1,10)

drawPicture()