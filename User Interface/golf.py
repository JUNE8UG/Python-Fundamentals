# Programmer: Olmedo, Johnny
# Submission date: 11/12/2019
# This program consolidates 2 programs into 1
def main():
    # Explain what we are doing.
    print('This program lets you enter golfers name and score into a file and display the contents of the file')
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]?: ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        # call user input function to get the user input and display the menu
        getInput = chooseProgram()
        # while the user decides not to quit
        while getInput != 3:
            # call the makeChoice function to determine which planet info to diplay to the user
            # pass the user input
            makeChoice(getInput)
            # call the choose program function
            getInput = chooseProgram()
        # give the user the option to run the program again
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def chooseProgram():
    # call displayPlanetMenu function
    displayProgramMenu()
    # ask the user to choose from a planet to learn about
    userInput = int(input("enter the menu number of the program you'd like to run: "))
    # input validation to ensure user input to withing numbers 1,2,3
    while userInput < 1 or userInput > 3:
        print("invalid selection, please choose one of the number options from the menu")  # prompt the user
        # call display program menu
        displayProgramMenu()
        userInput = int(input("enter the menu number of the program you'd like to run: "))  # ask the question again
    return userInput  # return user input


def displayProgramMenu():
    # display menu
    print('''\nselect a program
   1. run the program that inputs the golfer name and golf score
   2. run the program that display the golfer name and golf score
   3. exit the program''')


def makeChoice(getInput):
    if getInput == 1:  # criteria for program 1
        # call program 1
        programOne()
    else:  # criteria for program 2
        programTwo()  # call program 2


def programOne():
    # Explain what we are doing.
    print("This program  allows users to write golf player names and player scores onto the golf.txt file. ")
    # open the the file "golf.txt" in write mode
    with open("golf.txt", "w") as writeFile:
        # call the name function to obtain the name of a player in a golf tournament
        getName = nameFunction()
        # call the inputScore function to get the score of the corresponding player
        getScore = inputScoreFunction(getName)
        # call the writeFileFunction that will write all the data on the golf.txt file
        writeFileFunction(writeFile, getName, getScore)
        # call the closeFileFunction to close the file
        writeFile.close()


def nameFunction():
    # ask the user to enter a players name
    nameInput = input("enter the name of any player in the golf tournament : ")
    # return user input
    return nameInput


def inputScoreFunction(getName):
    # get the user input for the players score
    inputScore = input("enter the score that the player recieved : ")
    # input validation for negative numbers
    while int(inputScore) < 0:
        print("invalid score entry")  # explain the conditions needed of the entry
        print("please enter a player score that is greater than or equal to zero")
        inputScore = input("enter the score that the player recieved : ")  # ask the question again

    return inputScore  # return user input


def writeFileFunction(writeFile, getName, getScore):
    # write the name and score of the player on the file
    writeFile.write(getName + " " + getScore)


def programTwo():
    # Explain what we are doing.
    print("This program reads and display the golf.txt file. ")
    # call openFile to open the golf file and append/read the contents
    openFile()


def openFile():
    try:
        # open the golf file in read mode
        with open("golf.txt", "r") as writeFile:
            # for loop to go threw each line in the text
            for each in writeFile:
                print(each)  # print each line
            # close the file
            writeFile.close()
    except:
        print("file not found, creating one now")
        with open("golf.txt", "w") as writeFile:
            writeFile.close()
        # call main


main()
