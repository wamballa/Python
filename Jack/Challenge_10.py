"""
Challenge 10

Write a game that:
allows the user to play rock, paper, scissors against the computer
must display the computer’s choice and show the result of the game

"""
rock=1
paper=2
scissors=3
import random
again="y"
while again=="y":

    print("Player 1s turn")
    guess=input()
    print("Player 2s turn")
    guess_2=random.randint(1,3)
    if guess=="r"and guess_2==1:
        print("DRAW")

    elif guess=="r"and guess_2==2:
        print("Player 2 wins")

    elif guess=="r"and guess_2==3:
        print("Player 1 wins")

    elif guess=="s"and guess_2==2:
        print("Player 1 wins")
    ################
    elif guess=="s"and guess_2==1:
        print("Player 2 wins")

    elif guess=="s"and guess_2==3:
        print("DRAW")

    elif guess=="p"and guess_2==3:
        print("Player 2 wins")

    elif guess=="p"and guess_2==2:
        print("DRAW")

    elif guess=="p"and guess_2==1:
        print("Player 1 wins")

    again=input("Play again?")
