# Critical Thinking Assignment Option 2 
# Programmer: Olmedo, Johnny
# ITS-320
# Submission date: 11/28/2021
# This program prints out car informaton given by the user through the use of a dictionary

def main():
    # Explain what we are doing. 
    print("\nThis program collects information about a car, stores it in a dictionary, then prints it out\n")
    # ask the user if they wish to continue  
    answer = input("Do you wish to continue [Y/N]? : ")
    # while user input is "Y" or "y" 
    while (answer == "Y" or answer == "y"): 
        # Initialize getInfo to call carInfo 
        getInfo = carInfo() # getInfo will also act as a container to store info returned by carInfo()
        # call displayfunction to print results of carInfo
        display(getInfo) #pass getInfo so it knows what to print  
        # allow the user to run the program again if so desired without having to restart 
        answer = input("\n Do you wish to run the program again [Y/N]?: ")
   # End program gracefully
    print("\nThank you and goodbye!") 


def carInfo(): # this function gets the car information from user and returns it
    carDict = dict() # initialize dictionary
    # get the brand of the car
    carDict ['brand']= input("\nwhat brand is the car? ") 
    # get the model of the car
    carDict['Model'] = input("what is the model of the car? ")
    # get the year of the car
    carDict['Year'] = input("what year was the car made? ")
    # get the starting odometer of the car
    carDict['Starting Odometer'] = input("what was the starting odometer? ")
    # get the ending odometer of the car
    carDict['Ending Odometer'] = input("what is the ending odometer? ")
    # get the miles per gallon of the car
    carDict['MPG'] = input("what is the estimted miles per gallon? ")
    # return the loaded dictionary
    return (carDict)

def display(infoRecieved): #this function will print the car information recieved
    # header for the information
    print("\n CAR INFORMATION GIVEN: \n")
    # for the first and second argument in the dictionary print as followed
    for x, v in infoRecieved.items():
        # print the first argument, then the second one after 
        print(f' {x}: {v}') 

main() # call main