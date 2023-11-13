# Program 10 exercise # 6 PT 1
# Programmer: Olmedo, Johnny
# CSC119-141
# Submission date: 11/10/2019 
# This program reads a sentence as input and converts each word to "pig latin"
def main():
    # Explain what we are doing.
    print('This program reads a sentence as input and converts each word to "pig latin"')
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]?: ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        # ask for the user input
        inputSentence = input('''please enter any sentence you would like to convert to pig latin below:
        ''')  # gets sentance or word from a user that the program can convert to pig latin
        # call pig sentence / wholeSentence function
        pigsentence = wholeSentence(inputSentence)  # pass inputSentence / user input
        # call the display function
        displaySentence(pigsentence)  # pass pig sentence
        # allow the user to run the program again if so desired without having to restart
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def pigLatin(userString):  # the pigLatin function converts words/strings into pig latin
    firstLetter = userString[0]  # retrieve  the first letter
    newstr = userString[1:]  # set the new string to the old userString missing the first letter
    # add the firstLetter of the old userString to the end of the newStr
    newstr = newstr + firstLetter  # long way of +=
    newstr += "ay"  # append ay to end of each newStr
    # return the new string
    return newstr


def wholeSentence(inputSentence):
    pigString = ""  # initlize variable to an empty string
    # for loop to loop threw every element in the string
    for each in inputSentence.split():  # split the string to get the letters of the string chunked into words
        # add the pig latin version of each word in the inputSentence to the new pigString
        pigString += pigLatin(
            each) + " "  # add empty space at the end so that their is proper spacing after each append
    # return pigString
    return pigString


def displaySentence(sentence):
    # print out the pig version of the sentence
    print("The pig latin version of the sentence is :")
    print(sentence)


main()
