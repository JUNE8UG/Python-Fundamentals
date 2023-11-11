# Programmer: Olmedo, Johnny
# Submission date: 10/12/2019
# This program determines the miles per hour a driver is speeding
MIN_SPEED = 20 
MAX_SPEED = 70

def main():
   # Explain what we are doing. 
   print("This program takes the speed limit of a given road and the driving speed of a driver ")
   print("and determine the number of miles per hour the driver is exceeding the speed limit. ")
    
   answer = input("Do you wish to continue [Y/N]? ")
    
   while (answer == "Y" or answer == "y"):     
      # ask the user for the speed limit of the road they're driving on 
      speedLimit = int(input("enter the speed limit of a given road : "))
      # set up an input validation loop if the user enters in a limit below 20MPH
      while (speedLimit < MIN_SPEED or speedLimit > MAX_SPEED):
         # tell the user that they entered an incorrect value
         print("incorrect speed limit!")
         # tell the users their parameter
         print("the speed limit must be between 20 MPH and 70 mph")
         # ask the question again
         speedLimit = int(input("enter the speed limit in miles per hour of a given road : "))
   
      # ask the user to enter their current driving speed
      driveSpeed = int(input("enter current speed in miles per hour : "))
      # input validaion loop to ensure driver speed is >= speedLimit
      while (driveSpeed <= speedLimit):
         # let the user know the are not speeding
         print("your are not speeding!")
         # tell the user their parameters
         print("please enter a speed that is greater than or equal to")
         print("the speedlimit.")
         # ask the question again
         driveSpeed = int(input("enter current speed in miles per hour: "))
      # call function that will calculate how fast the driver is speeding
      speedingRate = calcSpeedingRate(speedLimit, driveSpeed) 
      # call the function that will display the drivers speeding rate
      display = displaySpeeding(speedingRate)  
      # allow the user to run the program again if so desired without having to restart 
      answer = input("Do you wish to run the program again [Y/N]? ")
   # End program gracefully
   print("\nThank you and goodbye!")
def calcSpeedingRate(limit, speed):
   # create variabe to hold calulations
   # subtract speed limt from driver speed to determine speed"
   speeding = speed - limit 
   return speeding 

def displaySpeeding(speedingRate):
   # tell the user how fast they were speeding
   print("the number of miles per hour the driver is speedings is : ", speedingRate)   

   # call main  
main()             