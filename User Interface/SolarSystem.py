# Programmer: Olmedo, Johnny
# Submission date: 11/12/2019 
# This program gives information on different planets in our solar system
def main():
    # Explain what we are doing.
    print('This program gives information on different planets in our solar system')
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]?: ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        # call user input function to get the user input and display the menu
        getInput = choosePlanet()
        # while user does not select to exit the program
        while getInput != 5:
            # call the makeChoice function to determine which planet info to diplay to the user
            makeChoice(getInput)  # pass the userInput
            # call and display the menu again
            getInput = choosePlanet()
        # give the user the option to run the program again
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def displayPlanetMenu():
    print()
    # display menu
    print('''select a Planet
   1. Mercury
   2. Venus
   3. Earth
   4. Mars 
   5. exit the program''')


def choosePlanet():
    # call displayPlanetMenu function
    displayPlanetMenu()
    # ask the user to choose from a planet to learn about
    userInput = int(input("\nchoose a planet to learn about "))
    # input validation to ensure user input to withing numbers 1,2,3,4,5
    while userInput < 1 or userInput > 5:
        print("invalid selection, please choose one of the number options from the menu")  # prompt the user
        # call display planet menue
        displayPlanetMenu()
        userInput = int(input("choose a planet to learn about "))  # ask the question again
    return userInput  # return user input


def makeChoice(getInput):
    if getInput == 4:
        displayPlanetInfo("MARS", "149.6", "0.6424 X 10^24kg", "-140 to 20")  # criteria for planet mars
    elif getInput == 3:
        displayPlanetInfo("EARTH", "227.9", "5.967 X 10^24kg", "-50 to 50")  # criteria for planet earth
    elif getInput == 2:
        displayPlanetInfo("VENUS", "108.2", "4.87 X 10^24kg", "472")  # criteria for planet venus
    else:
        displayPlanetInfo("MERCURY", "57.9", "3.31 X 10^23kg", "-173 to 430")  # criteria for planet mercury


def displayPlanetInfo(planet, distance, mass,
                      surfTemp):  # pass the planet name, distance from sun, mass, and surf temp to thhis function
    print("\nyou choose planet", planet)  # print the planet choosen
    print("\nAverage distance from the sun:", distance, "million kilometers")  # print the distance
    print("the planets mass is:", mass)  # print the mass
    print("the planets surface tempature is:", surfTemp, "degrees Celcius")  # print surface temp


# call main
main()
