# Programmer: Olmedo, Johnny
# Submission date: 10/22/2019 
# This program finds your friends phone numbers 
def main():
    names = ["david", "mary", "john", "joseph", "paul", "isaac", "jerimiah"]

    # Initialize list
    numbers = [17123456342, 18763857349, 15233096370, 18001752345,
               13317755678, 19638427502, 14316558901]

    # Dislay purpose of program to the user
    print("This program finds your friends phone numbers")

    # Give user a chance to quit the program
    answer = input("Do you wish to continue [Y/N]? ")

    while (answer.lower() == "y" or answer.lower() == "YES"):
        # Call dataInput for input and validation
        dataInput(names, numbers)

        # Give user a chance to quit the program
        answer = input("\nDo you wish to continue [Y/N]? ")
    print("Thank you and goodbye")


def dataInput(namesList, numbersList):
    # Get number
    inputName = input("\nEnter a friends name to validate: ")

    # Reset foundName
    foundName = False
    # names = ["joe", "mary", "john"]
    # Validate name
    # index == specific name is name list
    for index in range(len(namesList)):
        if (inputName == namesList[index]):  # if userInput == name in names list
            foundName = True  # set foundName = true if statement was true
            foundNameLocation = index  # foudNameLocation saves the correct userInput
    if foundName == True:  # if statemet to determine whether user input was true or false
        # print foundName along with that persons number
        print(numbersList[foundNameLocation])
        # print that the uer input was not found
    else:
        print(inputName, "is not found")

    # Call main()


main()
