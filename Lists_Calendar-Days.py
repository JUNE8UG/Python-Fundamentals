# Program 8 exercise # 6
# Programmer: Olmedo, Johnny
# CSC119-141
# Submission date: 10/26/2019 
# This program dprints the months in the year and the # of days in each month
def main():
    # Explain what we are doing.
    print("This program displays every month in the year ")
    print("and the number of days in each month. ")

    answer = input("Do you wish to continue [Y/N]? ")

    while (answer == "Y" or answer == "y"):
        # initialize month array
        monthList = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                     "november", "december"]

        # initialize days in month loop
        dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # call display function
        displayInfo = displayFunction(monthList, dayList)

        # allow the user to run the program again if so desired without having to restart
        answer = input("Do you wish to run the program again [Y/N]? ")

    # End program gracefully
    print("\nThank you and goodbye!")


def displayFunction(month, day):  # function that displays each month and days in month
    # for loop to cycle threw every element in month array
    for i in range(len(month)):
        # for each element in the array prin the corresponding monnth
        # and days in the month
        print(month[i], "has", day[i], "days.")


main()
