# back on master
import os.path  # used to see if a local file exists or not
from datetime import datetime  # used for getting the local time
import sys  # used to kill python script


######################################################
def funcGolf():
    print("This is the GOLF function")


######################################################
def funcInv():
    print("\n=Manage My Inventory===============================================")
    fileExists = os.path.isfile("myLuggage.txt")  # check if a file has already been created

    if fileExists:  # File exists so read contents into a list
        luggageList = []
        with open("myLuggage.txt") as file:
            for line in file:
                luggageList.append(line.strip())
                # open ("myLuggage.txt","w").close() #erase text in file

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
            return ()
        else:
            continue


######################################################
def funcTZ():
    # GMT difference
    UK = 0;
    France = +1;
    Poland = +2;
    Germany = +1
    NewYork = -7
    Australia = +12

    now = datetime.now()
    print("\n=Manage My Timezone ==========================================")

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
                origin = UK;
                break
            elif answer == "2":
                origin = France;
                break
            elif answer == "3":
                origin = Poland;
                break
            elif answer == "4":
                origin = Germany;
                break
            elif answer == "5":
                origin = NewYork;
                break
            elif answer == "6":
                origin = Australia;
                break
            elif answer == "7":
                return ()
            else:
                input("ERROR: Enter 1..7. Press ENTER to try again");
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
                dest = UK;
                break
            elif answer == "2":
                dest = France;
                break
            elif answer == "3":
                dest = Poland;
                break
            elif answer == "4":
                dest = Germany;
                break
            elif answer == "5":
                dest = NewYork;
                break
            elif answer == "6":
                dest = Australia;
                break
            elif answer == "7":
                return ()
            else:
                input("ERROR: Enter 1..7. Press ENTER to try again");
                continue
        timeDifference = dest - origin
        newHour = now.hour + timeDifference
        if newHour > 23:
            newHour = newHour - 24
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
loop = True
while loop:
    print("""
=MAIN MENU======================================================
1. Inventory
2. Time change
3. Golf
4. Currency Converter
5. Exit application""")
    answer = input("Choose option 1..4  ")
    if answer == "1":
        funcInv()
    elif answer == "2":
        funcTZ()
    elif answer == "3":
        funcGolf()
    elif answer == "4":
        funcCurrencyConverter()
    elif answer == "5":
        sys.exit()
    else:
        input("ERROR: Enter 1..4. Press Enter to try again");
        continue
