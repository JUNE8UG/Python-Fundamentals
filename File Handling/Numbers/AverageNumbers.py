# Programmer: Olmedo, Johnny
# Submission date: 11/10/2019 
# This program calculates the average of the numbers.txt file
def main():
    # Explain what we are doing.
    print("This program calclates the average of the numbers.txt file.")
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]?: ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        fileLines = []  # initilize array
        # call openReadFile function to open numbers.txt file
        returnCount = openReadFile(fileLines)
        # call the totalFunction to determine the total
        returnTotal = totalFunction(fileLines)
        # call the displayFunction to display and calculate the average
        displayFunction(returnTotal, returnCount)
        # allow the user to run the program again if so desired without having to restart
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def openReadFile(fileLinesList):
    # open the number.txt file
    with open("numbers.txt", "r") as readFile:
        count = 0  # initilize count
        for each in readFile:  # for loop to go threw every line in the file
            count += 1  # add 1 to count for each loop
            fileLinesList.append(each)  # append each line to the fileLines array
        readFile.close()  # close file
        return count  # return count


def totalFunction(fileLinesList):
    total = 0  # initilize counter
    # for loop to go thre every line and add each line to each other
    for each in fileLinesList:
        total += (int(each))  # add the total up
    return total  # return total


def displayFunction(total, count):
    # print total
    print("the total of all the numbers in numbers.txt: ", total)
    # print average
    print("the average of all the numbers in numbers.txt: ", total / count)


# call main
main()
