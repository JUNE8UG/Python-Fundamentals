# Programmer: Olmedo, Johnny
# Submission date: 11/10/2019 
# This program calclates the largest number in the numbers.txt file.  
def main():
    # Explain what we are doing.
    print("This program determines the largest number in the numbers.txt file.")
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]? : ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        smaller = 0  # initilize smaller variable for smallest numbers
        larger = 0  # initilize larger varirable for largest numbers
        # call the largestNum function that determies the largest and smallest numbers
        largest = largestNum(larger, smaller)
        # call displayInfo to display largest and smallest numbers found
        displayInfo(largest)
        # allow the user to run the program again if so desired without having to restart
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def largestNum(largest, smallest):
    # open the numbers.txt file as readFile
    with open("numbers.txt", "r") as readFile:
        for each in readFile:  # for loop to go threw every line in the file
            # determine if the newly entered number is lower or higher numerically than the previously read number
            # if the number in file is smaller than the smallest
            if int(each) < int(smallest):
                # set smallest to each, aka the smaller number found in file
                smallest = each
            # if the number in the file is greater than the largest
            if int(each) > int(largest):
                # set that number as the new largest
                largest = each
        readFile.close()  # close file
        return largest  # return largest number


def displayInfo(large):
    # print the largest number found
    print("The largest number found was ", large)


main()
