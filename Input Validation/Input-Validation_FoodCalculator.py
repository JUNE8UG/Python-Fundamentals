# Revised Fat Gram Calculator
# Programmer: Olmedo, Johnny
# October 14, 2019

ZERO = 0
LOW_FAT = 0.3


def main():
    # Explain what we are doing.
    print("This program takes the grams of fat and calories in a given food ")
    print("and determine the percentage of calories from fat in the food. ")

    answer = input("Do you wish to continue [Y/N]? ")

    while answer == "Y" or answer == "y":

        # variable for user input of fat grams
        fatGrams = float(
            input("enter the number of fat grams in a food item : "))  # user inputs the fat grams in a food item
        # begining of input validation loop

        while fatGrams < ZERO:  # if user inputs a number below zero display a message
            print("the number of fat grams must be above 0")
            # ask the user for a valid input
            print("please enter a valid number")
            fatGrams = float(input("enter the number of fat grams in a food item : "))

            # ask the user to enter the number of calories of a food item
        foodCalories = float(input("enter the number of calories in a food item : "))  # user inputs number calories

        while foodCalories < ZERO:  # input validation loop
            print("the number of calories must be above 0")  # number of calories must be above 0
            foodCalories = float(input(
                "enter the number of calories in a food item : "))  # user inputs valid number of calories(hopefully)

        # if the user inputs a number greater than zero then a additional
        # input validation loop is reqiured to ensure foodCalories is not greater
        # than product of fatgrams multiplied by 9
        while foodCalories < fatGrams * 9:
            print("the number calories can not be lower than")
            print("the product of fat grams multiplied by 9.")
            print("enter a valid number")  # ask the user for a valid number
            foodCalories = float(input("enter the number of calories in a food item : "))  # user input a valid number

        # call the function that will determine the percentage of calories from fat in a food item
        percentageCaloriesFat = calcPercentageCaloriesFat(fatGrams, foodCalories)

        # call the function that will display the percentage of calories from fat
        displayPercentFat(
            percentageCaloriesFat)  # transfer the result percentageCaloriesFat fucntion to display function

        # allow the user to run the program again if so desired without having to restart
        answer = input("Do you wish to run the program again [Y/N]? ")

    # End program gracefully
    print("\nThank you and goodbye!")


def calcPercentageCaloriesFat(grams, calories):  # funtion/equation that determines percentage of fat
    # equation of (fatGrams X 9) / FoodCalories
    percentFat = ((grams * 9) / calories)
    return percentFat


def displayPercentFat(percentageCaloriesFat):  # function that displays percetage of fat and low fat
    if percentageCaloriesFat < LOW_FAT:
        print("the food item is low in fat")
    print("the percentage  of calories from fat in the food item is : ", (percentageCaloriesFat * 100), "%")

    # call main


main()
