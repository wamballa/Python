# this is on my branch
import os.path #  Checks if the file exists
#Version 0.5
print("""**************************************MENU**************************************""")
############################################################
#All the defs
def Luggage():
    global listLength
    luggageList = [] # create an empty list
    fileExists = os.path.isfile("luggage.txt") # check if a file has already been created

    if fileExists == True: #File exists so read contents into a list
        with open("luggage.txt") as file:
            for line in file:
                luggageList.append (line.strip())
        open ("luggage.txt","w").close() #erase text in file

    elif fileExists == False: # File doesnt exist so create one called luggage.txt
        open ("luggage.txt","w").close() #create empty file

    ans = True
    while ans:
        print ("""
        What do you want to do:
        1. Show inventory
        2. Add another item
        3. Delete last entry
        4. Delete whole inventory
        
        """)
        ans = input ("Enter choice ")

        if ans == "1": # display current inventory
            listLength = len(luggageList) #how many items in list
            for i in range (0 , listLength):
                print (i+1, luggageList[i])
        elif ans == "2": # add item to list
            newItem = input ("Enter a new item") #get new item to add to list
            luggageList.append (newItem) # add new item to list
            listLength = len(luggageList) #how many items in list
            file = open ("luggage.txt","a") #open file to append to
            for i in range (0 , listLength):
                file.write (luggageList[i]) # write each item in list to file
                file.write ("\n") #add end of line seperator
            file.close()
        elif ans == "3":
            deleteCheck = input ("Are you sure you want to delete last item added? Y/N ")

            if deleteCheck == "Y" or deleteCheck == "y" and (listLength>0):
                luggageList.pop() # deletes last item from list.....................
                listLength = len(luggageList) #how many items in list
                open ("luggage.txt","w").close() #erase text in file
                file = open ("luggage.txt","a") # open file to append to
                for i in range (0, listLength):
                    file.write (luggageList[i]) #write each item in list to file
                    file.write ("\n") #add end of line seperator
                file.close()
            elif deleteCheck == "N" or deleteCheck == "n":
                continue
        elif ans == "4":
            deleteCheck = input ("Are you sure you want to delete whole inventory? Y/N ")
            if deleteCheck == "Y" or deleteCheck == "y":
                open ("luggage.txt","w").close() #erase text in file
                luggageList = []
                print ("Inventory Cleared")
            else:
                continue
        elif ans!="":
            input ("Incorrect Option. Select Option or press ENTER to return to main menu")
            continue
        #ans = False
############################################################
##Function: Time Zone Change
##Description: The Time Zone Changer allows you to pick where
##you currently are and where you are going. Then it will tell
##you how much to reset your watch by.        
############################################################
def TimeZone():
#locations and the time difference in comparison to the UK
    UK=0#Uk time difference
    France=+1#France time difference
    Germany=+1#Germany time difference
    Poland=+2#Poland time difference
    New_York=-4#New_york time difference
    Japan=+8#Japan time difference
#The Current Loacation Your In
    ans=True
    while ans:
        print("This is the Time Zone feature")#Introduction
        print(""" 
        Select your current location:
        UK
        Poland
        France
        Germany
        Poland
        New York
        Japan""")#Choices
        ans=input("Chose your location")#Current location choice
        if ans=="UK":origion=UK#Current location UK
        elif ans=="Poland":origion=Poland#Current location Poland
        elif ans=="France":origion=France#Current location France
        elif ans=="Germany":origion=Germany#Current location Germany
        elif ans=="New York":origion=New_York#Current location New York
        elif ans=="Japan":origion=Japan#Current location Japan
        elif ans!="":input("Im sorry, but what you entered was invalid. Please enter a country name");continue#Not valid message


        #Where you are going
        print("""
        Select your destination:
        UK
        Poland
        France
        Germany
        Poland
        New York
        Japan""")#All the options
        ans=input("Chose your target location")#Destination Choice
        if ans=="UK":target=UK #Destination UK
        elif ans=="Poland":target=Poland#Destination Poland
        elif ans=="France":target=France#Destination France
        elif ans=="Germany":target=Germany#Destination Germany
        elif ans=="New York":target=New_York#Destination New York
        elif ans=="Japan":target=Japan#Destination Japan
        elif ans=="":print("Not valid")#Not valid message

        print("Reset your watch by %d hours." % (target-origion))#Telling user how much they need to change their clock by

        ans=False

############################################################
## Function: Currency Exchange
## Description: Converts between two currencies
## Variable: convertTO: this is the local currency
############################################################

def CurrencyConverter():
    GBP=1
    US=0.57
    #print("You can Exchange your currency here")
############################################################
#####Convert from
    currencypick=input("""Hello, what currency would you like to convert from?
    1.Us Dollar
    2.Poland
    3.France
    4.Germany
    5.Japan
    6.UK""")
    print("Please choose")
    if currencypick=="1":convertTo=GBP
        #print("You have picked GBP")
    elif currencypick=="2":convertTo=US

############################################################
####Convert to
    print("Please choose")
    currencyChange=input("""And what currency would you like to convert to?
    1.US Dollar
    2.Poland
    3.France
    4.Germany
    5.Japan
    6.UK""")
    if currencyChange=="1":convertFrom=GBP
        #print("You have chosen GBP")
    elif currencyChange=="2":convertFrom=US
        #print("You have chosen US Dollar")
    #Amount the user wants
    amount=int(input("How much would you like?"))
############################################################
##calculation
    #US
    sum=(amount+0.57)#I also tried sum=(amount*0.57+amount) and sum=(amount*0.57)
    print("You will recieve" , sum,"Dollars")
    #Poland
    sum=(amount+5.79)
    print("You will recieve" , sum,"Polish Zloty")
    #France
    sum=(amount+1.36)
    print("You will recieve" , sum,"Euros")
    #Germany
    sum=(amount+2.70)
    print("You will recieve" , sum,"Marks")
    #Japan
    sum=(amount+186.85)
    print("You will recieve" , sum,"Yen")
    #UK

    sum=(amount+1)
    print("You will recieve" , sum,"Pounds")

############################################################
## Function: Cricket Scores
## Description: 
############################################################

def CricketMatch():

    cricketList = [] # create an empty list
    fileExists = os.path.isfile("cricket.txt") # check if a file has already been created

    if fileExists == True: #File exists so read contents into a list
        with open("cricket.txt") as file:
            for line in file:
                cricketList.append (line.strip())
        open ("cricket.txt","w").close() #erase text in file

    elif fileExists == False: # File doesnt exist so create one called luggage.txt
        open ("cricket.txt","w").close() #create empty file
    print("Here you can store your game while you play. And see who wins")
    ans = True
    while ans:
        print ("""
        What do you want to do:
        1. Show score
        2. Add score
        3. Delete last score added
        4. Reset
        
        """)
        ans = input ("Enter choice ")

        if ans == "1": # display current points
            listLength = len(cricketList) #how many items in points
            for i in range (0 , listLength):
                print (i+1, cricketList[i])

        elif ans == "2": # add item to list
            newItem = input ("Enter a new item") #get new item to add to list
            cricketList.append (newItem) # add new item to list
            listLength = len(cricketList) #how many items in list
            file = open ("cricket.txt","a") #open file to append to
            for i in range (0 , listLength):
                file.write (cricketList[i]) # write each item in list to file
                file.write ("\n") #add end of line seperator
            file.close()

        elif ans == "3":#
            deleteCheck = input ("Are you sure you want to delete last item added? Y/N ")

            if deleteCheck == "Y" or "y" and listLength>0:
                cricketList.pop() # deletes last score from list
                listLength = len(cricketList) #how many items in list
                open ("luggage.txt","w").close() #erase text in file
                file = open ("cricket.txt","a") # open file to append to
                for i in range (0, listLength):
                    file.write (cricketList[i]) #write each point scored in list to file
                    file.write ("\n") #add end of line seperator
                file.close()
            elif deleteCheck == "N" or "n":
                continue
        elif ans == "4":
            deleteCheck = input ("Are you sure you want to reset the score? Y/N ")
            if deleteCheck == "Y" or "y":
                open ("cricket.txt","w").close() #erase text in file
                luggageList = []
                print ("Score Cleared")
            elif deleteCheck == "N" or "n":
                continue
        elif ans!="":
            input ("Incorrect Option. Select Option or press ENTER to return to main menu")
            continue
        #ans = False
    #1st over=6 ballsserved to batter



    #Batting team 1st e.g. team A
    score=input("Amount scored on first hit")




    #Fielding team 1st e.g. team B

    #Batting team 2nd e.g. team B

    #fielding team 2nd e.g. team A

############################################################
## Function: Golf
## Description: You can calculate your scratch score in golf.
## It will take the course you selected then times the course
## by how many shots were taken, then display on screen.
############################################################

def Golf():
    print("You can calculate your scratch score of golf")
############################################################
##Course (How many holes)


############################################################
    #answer=True
    #while answer:
##  2 holes

    shots=int(input("How many shots did it take to finish the 2 holes?"))
    ScratchScore=sum=int(input(2*shots))

##  6 holes

    shots=int(input("How many shots did it take to finish the 6 holes?"))
    ScratchScore=sum=int(input(6*shots))

##  10 holes


    shots=int(input("How many shots did it take to finish the 10 holes"))
    ScratchScore=sum=int(input(10*shots))


        #elif ans!="":input("Sorry the infomation is not valid");continue

    sum ("Your Scratch Score is",ScratchScore)





##  Total

############################################################
## Function: Main Menu
## Description: The main menu is to allow the user to select
## what function they want to use. 
############################################################
answer=True
while answer:
    print("""
1.View Your Luggage.
2.Change Your Clock To The Local Timezone. 
3.Change Your Currency To your Holiday Location.
4.Keep Scores When Playing Cricket
5.Work Out The Scratch Scores In Golf""")
    answer=input("Select A Number To Chose What Feature That You Would Like To Use")
    if answer=="1":Luggage()
    elif answer=="2":TimeZone()
    elif answer=="3":CurrencyConverter()
    elif answer=="4":CricketMatch()
    elif answer=="5":Golf()
    elif answer !="": continue

