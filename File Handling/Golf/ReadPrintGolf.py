# Programmer: Olmedo, Johnny
# Submission date: 11/10/2019 
# This program is part 1 of 2 that reads and prints the  golf.txt file  
def main():
    # Explain what we are doing.
    print("This program reads and display the golf.txt file. ")
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]?: ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        # call openFile to open the golf file and append/read the contents
        openFile()
        # allow the user to run the program again if so desired without having to restart
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def openFile():
    # open the gold file in read mode
    with open("golf.txt", "r") as readFile:
        # for loop to go threw each line in the text
        for each in readFile:
            print(each)  # print each line
    # close the file
    readFile.close()


# call main
main()
