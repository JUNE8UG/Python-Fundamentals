# Programmer: Olmedo, Johnny
# Submission date: 10/26/2019 
# This program determines whether somone passed the drivers exam
def main():
    # Explain what we are doing.
    print("This program takes 20 inputs from the user and determines if the user ")
    print("passed the driving exam. ")

    answer = input("Do you wish to continue [Y/N]? ")

    while (answer == "Y" or answer == "y"):
        # Start with creating an array for all answers
        # array that holds all the correct answer
        actualAns = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A',
                     'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
        # array that automatically sets all answers to false to be able to change to true if need be
        wrongAns = [False, False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False, False, False,
                    False]  # False means correct answer, True means wrong answer
        # Get the users 20 answers using an array
        correcAns = calcTrueFalse(actualAns, wrongAns)
        # call display function
        displayInformation(actualAns, wrongAns, correcAns)
        # allow the user to run the program again if so desired without having to restart
        answer = input("Do you wish to run the program again [Y/N]? ")

    # End program gracefully
    print("\nThank you and goodbye!")


def calcTrueFalse(actualAns, wrongAns):
    correcAns = 0  # Initilie loop tracker
    # for loop to take an answer for every variable/letter in array actualAns
    for i in range(20):
        # Take user input
        answer = input("Enter answer for all 20 questions in exam : ")
        # Compare answers
        if answer == actualAns[i]:
            correcAns += 1  # correctAns = correctAns + 1
        else:
            wrongAns[i] = True  # set answer to true
    return correcAns  # return the correct answer


def displayInformation(actualAns, wrongAns, correcAns):
    print("The number questions answered incorrectly : ",
          20 - correcAns)  # display the number of wrong answers by subtracting the # of correct asnwers by 20
    # for loop to print which answers were answered incorrectly
    for i in range(20):
        # if the answer was incorrect
        # then print the number(s) that were incorrect
        if (wrongAns[i]):
            print("question number : ", i + 1, "was incorrect")  # +1 because the arrays start at 0
    # print the number correct answers given by user
    print("the number of questions answered correctly: ", correcAns)
    # validation if the user passed the exam
    # users passes if the user getts 15 or more correct
    if (correcAns >= 15):
        print("you passed the exam!")


main()
