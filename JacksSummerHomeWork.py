# back on master
import os.path  # used to see if a local file exists or not
from datetime import datetime  # used for getting the local time
import sys  # used to kill python script


######################################################
def function_Cricket_Scores():

    print ("\n=Cricket Scores: keep track of the scores for a cricket game======================\n ")

    overScore = 0 # score for each over, zero'd after each over
    totalScoreA = 0 # running total score for teamA
    totalScoreB = 0 # running total score for teamB

    teamA = ( input ("Enter the name of the first cricket team: ")) #enter teamA name
    teamB = ( input ("Enter the name of the second cricket team: ")) #enter teamB name

    print ("\nTeam %s bats first.\n" % teamA)

    for over in range (1 , 21): # 20 overs per team

        for bowls in range (1 , 7 ): # 6 bowls per over
            overScore += int(input("Enter runs for Over %s, Ball %s, for team %s: " % (over, bowls, teamA)))

        print ( "Score for over %s is %s " % (over,overScore))
        totalScoreA += overScore  # add score from the over to total score
        overScore = 0 # zero over score
        print ("\nTeam %s total score for %s overs is %s \n" % (teamA ,over, totalScoreA))

    print ("\nTeam %s bats next.\n" % teamB)

    for over in range (1 , 21): # 20 overs per team
        for bowls in range ( 1 , 7 ): # 6 bowls per over
            overScore += int(input("Enter runs for Over %s, Ball %s, for team %s: " % (over, bowls, teamB)))
        print ( "Score for over %s is %s " % (over,overScore))
        totalScoreB += overScore  # add score from the over to total score
        overScore = 0 # zero over score
        if totalScoreB > totalScoreA: # check after every over if teamB score beats teamA score
            print ("\nCONGRATS team %s. You beat team %s by %s runs to %s" % (teamB, teamA , totalScoreB,totalScoreA))
            break # break the for loop
        else:
            print ("\nTeam %s total score for %s overs is %s \n" % (teamB ,over, totalScoreB))

    if totalScoreA > totalScoreB:
        print ("\nCONGRATS team %s. You beat %s by %s runs to %s" % (teamA , teamB,totalScoreA,totalScoreB))
    elif totalScoreA == totalScoreB:
        print ("\nDRAW team %s and team %s both got %s runs.\n" % (teamA,teamB , totalScoreB ))

    input ("\nPress enter to return to main menu.")

######################################################
def funcInv():
    print("\n=Manage My Inventory===============================================")
    fileExists = os.path.isfile("myLuggage.txt")  # check if a file has already been created

    if fileExists:  # File exists so read contents into a list
        luggageList = []
        with open("myLuggage.txt") as file:
            for line in file:
                luggageList.append(line.strip())

    elif not fileExists:  # File doesnt exist so create one called myLuggage.txt
        luggageList = []
        open("myLuggage.txt", "w").close()  # create empty file

    ans = True
    while ans:
        print("""
What do you want to do:
1. Show inventory
2. Add another item
3. Delete last entry
4. Delete whole inventory
5. Exit to main        """)
        answer = input("Enter choice 1..5 ")

        if answer == "1":  # display current inventory
            listLength = len(luggageList)  # how many items in list
            for i in range(0, listLength):
                print(i + 1, luggageList[i])
        elif answer == "2":  # add item to list
            newItem = input("Enter a new item")  # get new item to add to list
            luggageList.append(newItem)  # add new item to list
            open("myLuggage.txt", "w").close()  # erase text in file
            listLength = len(luggageList)  # how many items in list
            file = open("myLuggage.txt", "a")  # open file to append to
            for i in range(0, listLength):
                file.write(luggageList[i])  # write each item in list to file
                file.write("\n")  # add end of line seperator
            file.close()
        elif answer == "3":
            deleteCheck = input("Are you sure you want to delete last item added? Y/N ")
            listLength = len(luggageList)  # how many items in list
            if (deleteCheck == "Y" or deleteCheck == "y") and (listLength > 0):
                luggageList.pop()  # deletes last item from list
                listLength = len(luggageList)  # how many items in list
                open("myLuggage.txt", "w").close()  # erase text in file
                file = open("myLuggage.txt", "a")  # open file to append to
                for i in range(0, listLength):
                    file.write(luggageList[i])  # write each item in list to file
                    file.write("\n")  # add end of line seperator
                file.close()
            else:
                continue
        elif answer == "4":
            deleteCheck = input("Are you sure you want to delete whole inventory? Y/N ")
            if deleteCheck == "y" or deleteCheck == "Y":
                open("myLuggage.txt", "w").close()  # erase text in file
                luggageList = []
                print("\nInventory Cleared")
            else:
                continue
        elif answer == "5":
            return () # exit function
        else:
            continue # continue from beginning of while


######################################################
def funcTZ():

    print("\n=Manage My Timezone ==========================================\n")

    # GMT difference
    UK = 0
    France = +1
    Poland = +2
    Germany = +1
    NewYork = -7
    Australia = +12

    now = datetime.now()


    loop1 = True
    while loop1:
        loop2 = True
        while loop2:
            print("""
Enter Origin        
1. UK
2. France
3. Poland
4. Germany
5. New York
6. Australia
7. Exit""")
            answer = input("Choose origin 1..6 ")
            if answer == "1":
                origin = UK
                break
            elif answer == "2":
                origin = France
                break
            elif answer == "3":
                origin = Poland
                break
            elif answer == "4":
                origin = Germany
                break
            elif answer == "5":
                origin = NewYork
                break
            elif answer == "6":
                origin = Australia
                break
            elif answer == "7":
                return ()
            else:
                input("ERROR: Enter 1..7. Press ENTER to try again")
                continue

        while loop2:
            print("""
Enter Distination
1. UK
2. France
3. Poland
4. Germany
5. New York
6. Australia
7. Exit""")
            answer = input("Choose destination 1..6 ")
            if answer == "1":
                dest = UK
                break
            elif answer == "2":
                dest = France
                break
            elif answer == "3":
                dest = Poland
                break
            elif answer == "4":
                dest = Germany
                break
            elif answer == "5":
                dest = NewYork
                break
            elif answer == "6":
                dest = Australia
                break
            elif answer == "7":
                return ()
            else:
                input("ERROR: Enter 1..7. Press ENTER to try again")
                continue
        timeDifference = dest - origin
        newHour = now.hour + timeDifference
        if newHour > 23:
            newHour -= 24
        print("\nPlease reset 24 hour watch by %d hours" % timeDifference)
        if now.minute < 10:
            print("Time change from %s:0%s to %s:0%s" % (now.hour, now.minute, newHour, now.minute))
        else:
            print("Time change from %s:%s to %s:%s" % (now.hour, now.minute, newHour, now.minute))
        input("\nPress ENTER to go to Main menu")
        loop1 = False


##########################################################
def funcCurrencyConverter():
    print("\n=Currency Converter ==========================================")

    currencyFrom = input("Enter name of the currency you have: ")
    currencyTo = input("Enter name of the currency you want: ")
    exchangeRate = float(input("Enter the Exchange rate between %s and %s: " % (currencyFrom, currencyTo)))
    amountToExchange = float(input("Enter the amount of %s you wish to exchange to %s: " % (currencyFrom, currencyTo)))

    amountReceived = amountToExchange * exchangeRate

    print("\nIf you convert %.2f %s you will receive %.2f %s" % (
        amountToExchange, currencyFrom, amountReceived, currencyTo))

##########################################################
def function_golf_scratch_calculator():

    print("\n=Calculate Golf Course Scratch  ===============================================")

    scratch = 0 # overall scratch for golf course
    par5holes = 0 # number of holes taking 5 shots
    par4holes = 0 # number of holes taking 4 shots
    par3holes = 0 # number of holes taking 3 shots
    difficulty = 0 # difficulty adjustment

    answer = True
    while answer:
        print("""
What do you want to do:
1. Show golf scratch
2. Enter standard scratch for 18 hole golf course
3. Delete whole scratch file
4. Exit to main        """)
        answer = input("Enter choice 1..4 ")

        if answer == "1":  # display current scratch entered
            fileExists = os.path.isfile("myGolfScratch.txt")  # check if a file has already been created
            if fileExists:  # File exists so read contents into a list
                with open("myGolfScratch.txt") as file:
                    for line in file:
                        print (line.strip())
            elif not fileExists:  # File doesnt exist so create one called myLuggage.txt
                print ("Golf course scratch card doesn't exist")
        elif answer == "2":  # enter standard scratch
            open("myGolfScratch.txt", "w").close()  # erase text in file so no old data
            file = open("myGolfScratch.txt", "a")  # open file to append to
            scratch = 0 # zero scratch for course
            par5holes = int ( input ("How many holes takes 5 shots (par 5)? "))
            par4holes = int ( input ("How many holes takes 4 shots (par 4)? "))
            par3holes = int ( input ("How many holes takes 3 shots (par 3)? "))
            difficulty = int ( input ("What is the difficulty adjustment? "))

            scratch = (par5holes*5) + (par4holes*4) + (par3holes*3) + difficulty

            print ("\nThe scratch for this golf course is %s" % (scratch))

            file.write("%s holes take 5 shots\n" % (par5holes))  # write to file number of holes
            file.write("%s holes take 4 shots\n" % (par4holes))  # write to file number of holes
            file.write("%s holes take 3 shots\n" % (par3holes))  # write to file number of holes
            file.write("Difficulty Adjustment = %s\n" % (difficulty))  # write to file difficulty
            file.write("Golf course scratch is %s\n" % (scratch))
            file.write("\n")  # add end of line seperator
            file.close()
        elif answer == "3":
            deleteCheck = input("Are you sure you want to delete whole scratch file? Y/N ")
            if deleteCheck == "y" or deleteCheck == "Y":
                open("myGolfScratch.txt", "w").close()  # erase text in file
                print("\nScratch File Cleared\n")
            else:
                continue
        elif answer == "4":
            return () # exit function
        else:
            continue # continue from beginning of while



##########################################################
loop = True
while loop:
    print("""
=MAIN MENU======================================================
1. Inventory
2. Time Zone
3. Cricket Scores
4. Currency Converter
5. Golf scratch calculator
6. Exit application""")
    answer = input("Choose option 1..4  ")
    if answer == "1":
        funcInv()
    elif answer == "2":
        funcTZ()
    elif answer == "3":
        function_Cricket_Scores()
    elif answer == "4":
        funcCurrencyConverter()
    elif answer == "5":
        function_golf_scratch_calculator()
    elif answer == "6":
        sys.exit()
    else:
        input("ERROR: Enter 1..4. Press Enter to try again")
        continue
