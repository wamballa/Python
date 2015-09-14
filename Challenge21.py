"""
Challenge 21

Write a program that converts between centimetres, and inches and vice versa, by:
asking the user to input a number
asking the user to choose between converting from centimetres to inches or from inches to centimetres
calculating and outputting the result using functions
1 inch = 2.54 cm
1 cm = 0.393700787 inches

"""

print ("Convert between centimetres and inches and vice versa")

def convertLength ( convertTo, length ):
    if convertTo == 1:
        cmToInch = 0.393700787
        print ("%s Centimetres = %.2f inches " % (length, (length * cmToInch)))
    elif convertTo == 2:
        inchToCM = 2.54
        print ("%s inches = %.2f centimetres " % (length, (length * inchToCM)))

length = float(input("Enter the length you wish to convert: "))
convertTo = int(input("1. Convert Centimetres to Inches\n2. Convert Inches to Centimetres\nChoose how to convert:"))
convertLength (convertTo,length)