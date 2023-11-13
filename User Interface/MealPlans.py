# Programmer: Olmedo, Johnny
# Submission date: 11/12/2019 
# This program gives information on meal plans for students
def main():
    # Explain what we are doing.
    print('This program gives information on meal plans for students')
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]?: ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        # call user input function
        getInput = inputFunction()
        # while user decides not to exit the program
        while getInput != 4:
            # call the makeChoice function
            makeChoice(getInput)
            # call the input function again to display the menu. Give the
            # user the option to run another task in the menu
            getInput = inputFunction()
        # give the user the option to run the program again
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def displayMenu():
    print('''\nchoose from a plan
   
   Plan 1. 7 meals per week for $560 per semester
   Plan 2. 14 meals per week for $1,095
   Plan 3. Unlimited meals for $1,500
   Option 4. end of program''')


def inputFunction():
    # call the display menu functon to show the menu
    displayMenu()
    # get a user input on which menu option to perform
    userInput = int(input("\nselect a meal plan: "))
    # input validation to ensure the program doesn't crash
    while userInput < 1 or userInput > 4:
        print("invalid selection")
        print("please choose a valid option number from the menu board")
        # call display
        displayMenu()
        # ask the question again
        userInput = int(input("\nselect a meal plan: "))
    return userInput  # return the userInut


def makeChoice(getInput):
    # set up criteria for option 1
    if getInput == 1:
        # call planType function
        planType(560)  # pass 560 for price of plan
    # set up criteria for option 2
    elif getInput == 2:
        # call planType function
        planType(1095)  # pass 1095 for the cost of the plan
    else:
        # set up criteria for option 3
        planType(1500)  # pass 1500 as cost of pplan


def planType(cost):  # pass plan prices as an argument
    # retrieve the number of semesters the student will be using the plan for
    semesterInput = int(input("enter the number of semesters you will use the meal plan: "))
    # calculate the total cost
    totalPrice = cost * semesterInput
    # print the total cost of the plan for that student
    print("the total cost of plan will be ($)", totalPrice)


main()
