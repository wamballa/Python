"""
Challenge 26

Write a maths quiz with three questions
It must ask the user to input their name at the start.
At the end it should display a message informing of their score.
Write a function that saves the users name and result in a file,
"""

    import random  # import random module to use random function

#define variables
operation = ["+", "-", "*"]
firstNumber = 0 #first number of equation
secondNumber = 0 # second number of equation
randomOperation = 0 # randomly select +, -, *
correctAnswer = 0 # correct answer
question = 0 # which question out of three
score = 0 # play score

#######################################################
# Function to write players Maths Quiz result to a file
#######################################################
def writeResultToFile ():
    #open a file to write results
    file = open("%sMathsQuiz.txt" % name, "a")  # open file to append to
    file.write ("\n%s you scored %d percent in the Maths Quiz." % (name, score/3*100))
    file.close()

print ("Maths Quiz. Answer the following three questions.\n")
name = input("Tell me your name to enter the Maths Quiz: ")

# create loop for 3 questions
for question in range (0,3):
    firstNumber = random.randint(0, 5)
    secondNumber = random.randint(0, 5)
    randomOperation = random.randint(0, 2)
    correctAnswer = 0
    answer = int(input("Question: %s: What is %s %s %s? " % (question+1, firstNumber, operation[randomOperation], secondNumber)))

    if randomOperation == 0:
        correctAnswer = firstNumber + secondNumber
    elif randomOperation == 1:
        correctAnswer = firstNumber - secondNumber
    elif randomOperation == 2:
        correctAnswer = firstNumber * secondNumber

    if answer == correctAnswer:
        print("CORRECT %s: %s %s %s = %s" % (name, firstNumber, operation[randomOperation], secondNumber, correctAnswer))
        score += 1
    else:
        print("INCORRECT %s: %s %s %s = %s" % (name, firstNumber, operation[randomOperation], secondNumber, correctAnswer))

writeResultToFile () # write the results of the Maths Quiz to file
print ("Thanks for playing. You scored %d percent. Your results are in file %sMathsQuiz.txt" % (score/3*100,name))