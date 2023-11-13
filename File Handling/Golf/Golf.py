# Programmer: Olmedo, Johnny
# Submission date: 11/10/2019 
# This program is part 1 of 2 that creates a file named golf and allows users to write player names and player scores onto the file 
def main():
    # Explain what we are doing.
    print("This program  allows users to write golf player names and player scores onto the golf.txt file. ")
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]?: ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        # open the the file "golf.txt" in append mode
        with open("golf.txt", "a") as appendFile:
            # call the name function to obtain the name of a player in a golf tournament
            getName = nameFunction()
            # call the inputScore function to get the score of the corresponding player
            getScore = inputScoreFunction()
            # call the writeFileFunction that will write all the data on the golf.txt file
            writeFileFunction(appendFile, getName, getScore)
            # call the closeFileFunction to close the file
            appendFile.close()
        # allow the user to run the program again if so desired without having to restart
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def nameFunction():
    # ask the user to enter a players name
    nameInput = input("enter the name of any player in the golf tournament : ")
    # return user input
    return nameInput


def inputScoreFunction():
    # get the user input for the players score
    inputScore = input("enter the score that the player recieved : ")
    # input validation for negative numbers
    while int(inputScore) < 0:
        print("invalid score entry")  # explain the conditions needed of the entry
        print("please enter a player score that is greater than or equal to zero")
        inputScore = input("enter the score that the player recieved : ")  # ask the question again

    return inputScore  # return user input


def writeFileFunction(appendFile, getName, getScore):
    # write the name and score of the player on the file
    appendFile.writelines(getName + " " + getScore + "\n")


# call main
main()
