# Program 6 exercise # 9
# Programmer: Olmedo, Johnny
# CSC119-141
# Submission date: 10/06/2019 
# This program lets a user guess a number a keeps track of how many times the user guesses
import random


def guessingGame():  # main function
    # winning number that the user will have to guess
    winNumber = random.randint(1, 10)  # the random number generated for each game
    # count control for user entry
    numberGuesses = 0
    while (winNumber):  # using while loop to 'trap' user in game
        winNumber = random.randint(1, 10)  # the random number generated for each game
        userinput = int(input(
            "guess a number between 1 and 10: "))  # ask the user to guess a number, if the number is not equal to the radom number have the user try again
        if (userinput == winNumber):  # criteria to win the game
            numberGuesses = numberGuesses + 1  # add 1 to the numbr of guesses made by user
            displayWinner(numberGuesses)  # call displayWinner function to exit loop and display out put to user
            break
        else:  # if the user doesn't enter the right number have them try again
            print("the wrong number was guessed please try again")
            numberGuesses = numberGuesses + 1  # add 1 to number of guesses already exsisting


def displayWinner(numberGuesses):
    print("YOU GUESSED THE NUMBER CORRECTLY!")  # let the user know they guessed correctly
    print("number of attepmts made : ", numberGuesses)  # display number og huesss made by user


def main():  # main module used to call main function
    guessingGame()


main()
