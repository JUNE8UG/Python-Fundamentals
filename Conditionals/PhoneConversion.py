# Programmer: Olmedo, Johnny
# Submission date: 11/12/2019 
# This program gives the numeric value of a phone number 
def main():
    # Explain what we are doing.
    print("This program converts alphabet values to numeric values in a telephone number")
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]?: ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        # ask the user for a cell phone number
        userInput = input("enter a phone number ")
        # call the functon that gives the numeric equivalent
        numEquiv(userInput)
        # give the user the option to run the program again
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def numEquiv(numInput):
    # initlitze an empty string
    aString = ""
    # for loop to loop threw every character in numInput
    for each in numInput:
        # call the function that will decide what num value of the charecter is
        decide = decideFunc(each)
        # add each value to the string for every loop
        aString += decide  # assign each as an argument for decideFunc
    # call te display function
    displayString(aString)


def displayString(phoneNum):
    print("The numeric value of the phone number is:")
    print(phoneNum)  # print the phone number


def decideFunc(letter):
    # set each charchter to lower case if possible
    letter = letter.lower()
    # criteria for letters a,b,c
    if letter == "a" or letter == "b" or letter == "c":
        letter = "2"  # set letter to 2
    # crieria for d,e,f
    elif letter == "d" or letter == "e" or letter == "f":
        letter = "3"  # set the letter to 3
    # crieria for g,h,i
    elif letter == "g" or letter == "h" or letter == "i":
        letter = "4"  # set letter to 4
    # crieria for j,k,l
    elif letter == "j" or letter == "k" or letter == "l":
        letter = "5"  # set letter to 5
    # crieria for m,n,o
    elif letter == "m" or letter == "n" or letter == "o":
        letter = "6"  # set letter to 6
    # crieria for p,q,r,s
    elif letter == "p" or letter == "q" or letter == "r" or letter == "s":
        letter = "7"  # set letter to 7
    # crieria for t,u,v
    elif letter == "t" or letter == "u" or letter == "v":
        letter = "8"  # set letter to 8
    # crieria for w,x,y,z
    elif letter == "w" or letter == "x" or letter == "y" or letter == "z":
        letter = "9"
    # else leave the charecter as is
    else:
        letter = letter  # set letter to 9
    # return letter
    return letter


# call main
main()
