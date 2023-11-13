# Revised Fat Gram Calculator
# Programmer: Olmedo, Johnny
# Date : October 14, 2019

# Constant Variables
ZERO = 0
LOW_FAT = 0.3


def main():
    # Explain what we are doing.
    print("This program calculates percentage of calories from fat in a food ")
    print("it then determines if the food is nutritious. ")

    answer = input("Do you wish to continue [Y/N]? ")

    while (answer == "Y" or answer == "y"):
        # variable for user input of fat grams
        fatGrams = float(
            input("enter the number of fat grams in a food item : "))  # user inputs the fat grams in a food item
        protienGrams = float(input("enter the number of protien grams in the food item : "))
        carbohydrateGrams = float(input("enter the number of carbohydrate grams in the food item : "))
        # begining of input validation loop
        while (
                fatGrams < ZERO and protienGrams < ZERO and carbohydrateGrams < ZERO):  # if user inputs a number below zero display a message
            print("the number of grams must be above 0")
            # ask the user for a valid input
            print("please enter a valid number")
            fatGrams = float(input("enter the number of fat grams in a food item : "))
            protienGrams = float(input("enter the number of protien grams in the food item : "))
            carbohydrteGrams = float(input("enter the number of carbohydrate grams in the food item : "))
        # call the function that will display the percentage of calories from fat
        totalCalories = calcTotalCalories(fatGrams, protienGrams, carbohydrateGrams)
        # call the function that will determine the percentage of calories from fat in a food item
        fatPercentage = calcFatPercentage(fatGrams, totalCalories)
        # call the function that will display the information about the food
        displayPercentFat(fatPercentage, totalCalories)
        # allow the user to run the program again if so desired without having to restart
        answer = input("Do you wish to run the program again [Y/N]? ")
    # End program gracefully
    print("\nThank you and goodbye!")


def calcFatPercentage(fat, calories):  # funtion/equation that determines percentage of fat
    # equation of (fatGrams X 9) / FoodCalories
    percentFat = ((fat * 9) / calories)
    return percentFat


def calcTotalCalories(fat, protien, carbohydrates):
    calories = ((fat * 9) + (protien * 4) + (carbohydrates * 4))
    return calories


def displayPercentFat(fat, calories):  # function that displays percetage of fat and low fat
    if (fat < LOW_FAT):
        print("the food item is low in fat")
    print("the percentage  of calories from fat in the food item is : ", (fat * 100), "%")
    print("the total calories in the food item is : ", calories)
    # call main


main()
