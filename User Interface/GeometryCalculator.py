# Programmer: Olmedo, Johnny
# Submission date: 11/14/2019 
# This program calculates the area of a shape 
def main():
    # Explain what we are doing.
    print('This program calculates the area of a shape')
    # ask the user if they wish to continue
    answer = input("Do you wish to continue [Y/N]?: ")
    # while user input is "Y" or "y"
    while (answer == "Y" or answer == "y"):
        # call user input function
        getInput = inputFunction()
        # while the user decides not to exit the menu
        while getInput != 4:
            # call makeChoice function
            makeChoice(getInput)  # pass the user input as an argument
            getInput = inputFunction()
        # give the user the option to run the program again
        answer = input("Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


def displayMenu():
    # display the menu
    print('''\nGeometry Calculator
   1. Calculate the Area of a Circle
   2. Calculate the Area of a Rectangle
   3. Calculate the Area of a Triangle 
   4. Quit''')


def inputFunction():
    # call display function
    displayMenu()
    # ask the user to choose an option from the menu
    userInput = int(input("\npick a shape to calculate its area "))
    # input validation in the event the user enters options not on the menu
    while userInput < 1 or userInput > 4:
        print("invalid entry")  # tell the user the input was incorrect
        print(
            "please enter a number option displayed on the menu")  # tell the user what kind of input the program is looking for
        # call display function
        displayMenu()
        # ask the question again
        userInput = int(input("pick a shape to calculate its area"))
    return userInput  # return the user input


def makeChoice(getInput):  # pass the user input from main()
    if getInput == 1:  # criteria for area of a circle
        areaCircle()  # call area of a cirlce functions
    elif getInput == 2:  # criteria for area of a rectangle
        areaRectangle()  # call the area of a rectangle function
    else:  # criteria for area of a triangle
        areaTriangle()  # call the area of a triangle funtion


def areaCircle():
    # ask the user for the radius of a circle
    radiusInput = float(input("enter the radius of any given circle: "))
    # determine the area by multiplying (pi * (radius^squared))
    area = (3.14159) * ((radiusInput) ** 2)
    # print out the area of the circle
    print("the area of the circle is:", area)


def areaRectangle():
    # ask the user for the length of the rectangle
    lengthInput = int(input("enter the length of the rectangle:"))
    # ask the user for the width of the rectangle
    widthInput = int(input("enter the width of a rectangle"))
    # determine the area by multiplying legth and width
    area = widthInput * lengthInput
    # tell the user what the area of the circle is
    print("the area of the rectangle is:", area)


def areaTriangle():
    # ask the user for the base length of the triangle
    baseLength = float(input("enter the length of th triangles base: "))
    # ask the user for height of the triangle
    height = float(input("enter the height of the triangle: "))
    # area is  equal to baselenth * (height(0.5))
    area = baseLength * (height * .5)
    # print the ara of the triangle
    print("the area of the triangle is:", area)


# call main
main()
