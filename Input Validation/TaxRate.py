# Programmer: Olmedo, Johnny
# Submission date: 12/5/2021
# This program can determine weekly tax rate based on income given by the user
# it also has input validation and exception handeling, please feel free to try and break the program  

def main():
    # Explain what we are doing. 
    print("\nThis program collects information about a car, stores it in a dictionary, then prints it out\n")
    # ask the user if they wish to continue  
    answer = input("Do you wish to continue [Y/N]? : ")
    # while user input is "Y" or "y" 
    while (answer == "Y" or answer == "y"):
        # function that gets input than returns it
        income = inputFunc()

        # function that initilizes the dictionary
        inDict = dictionaryFunc()

        # function that decides
        decide = decideTax(income, inDict)

        # print out decision
        printFunc(income, decide)

        answer = input("\n Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


# functon that will get input from user 
def inputFunc():
    getInput = input("\nPlease enter your income amount in dollars ($): ")  # get initial input from user
    checkedIn = inputVal(getInput)  # sned t input validation function
    return checkedIn  # once the input passes input validation return it


# function recieves user input to check if its the right values
def inputVal(gotInput):
    # first see if the user immediately entered the right input
    try:
        val = float(gotInput)  # see if the input is a float
    # if it's not a float its okay, but stop the program from stopping due to error
    except ValueError:
        # while the input is not a numeric number
        while gotInput.isnumeric() == False:
            # remind the user to enter the right input
            print(
                '\nit looks like you input a non numeric dollar value, please enter a valid dollar value to calculate the weekly tax: ')
            gotInput = input("\nPlease enter your income amount in dollars ($): ")  # get another input
            # check again if this time they input a float or numeric number
            try:
                val = float(gotInput)
            # if its not a float or numeric then just restart the loop and ask them for the right value again
            except ValueError:
                pass
            # if the user does enter a float or numeric then return it
            else:
                return gotInput
        return gotInput  # once it passes the while loop, conditons must be correct soo return value
    # user entered a floa or numeric so return the value 
    else:
        return gotInput


# function intitlilizes dictionary
def dictionaryFunc():
    # these are the values given from assignement
    dictionary = {'0-499': '10%', '500-1499': '15%', '1500-2499': '20%', '2500+': '30%'}
    return dictionary  # return dictionary


# function that decides what to print out
def decideTax(incomeR, dictR):
    # intitliaze income as a float to use for the rest of the function
    income = float(incomeR)
    # if income is between 0 and 499 
    if (income >= 0) and (income < 500):
        return dictR['0-499']  # return 10%
    # if income is between 500 and 1499
    elif (income >= 500) and (income < 1500):
        return dictR['500-1499']  # return 15%
    # if income is between 1500 and 2499
    elif (income >= 1500) and (income < 2500):
        return dictR['1500-2499']  # return 20%
    # i income is greater than 2500
    elif income >= 2500:
        return dictR['2500+']  # return 30%
    # other wise they entered a negative number
    else:
        print("\nI hope your financial situation gets better.")
        print("Technically you shouldn't have a weekly tax rate\n")


# function that prints stuff out
def printFunc(income, taxDict):
    # tell them the tax rate for the income given
    print("The weekly tax rate for an income of", income, "dollars is", taxDict)


main()  # call main
