__author__ = 'wamballa'

array = ["First row data", "Second Row data", "Third Row data","Fourth Row data","Fifth Row data","Sixth Row data","Seventh Row data"]
arrayLength = len(array)
while True:
    numberofRows = int ( input ("Number of rows to print: "))
    if numberofRows > arrayLength:
        print ("1!Not that many rows in your data")
        continue

    for row in range ( 0, numberofRows):
        print (array[row])