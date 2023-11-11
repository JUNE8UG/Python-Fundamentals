# Programmer: Olmedo, Johnny

# Submission date: 10/07/2019 
# This program determines am employees gross pay 
MIN_WAGE = 7.50
MAX_WAGE = 18.25
MIN_HOURS = 0
MAX_HOURS = 40 
def main():
   # Explain what we are doing. 
   print("This program takes the hourly wage of an employee and ")
   print("the hours worked by the employee to deterime gross pay. ")
    
   answer = input("Do you wish to continue [Y/N]?")
    
   while (answer == "Y" or answer == "y"):
         # assign a variable to the wageFunction  
         # and call wageFunction to obtain the users pay rate 
         hourWage = wageFunction()
         # assign a variable to the daysWorkedFunction
         # and call the daysWorkedFuncton to obtain the days worked  
         hoursWorked = daysWorkedFunction()
         # assign variable to employeeGrossPay
         # give the employeeGrossPay function the hours worked and hourly wage 
         # call employeeGrossPay to calculate the employees gross wage
         grossPay = employeeGrossPay(hourWage, hoursWorked)
         # pass grossPay to displayGross function
         # call displayGross function
         displayGrossFunction(grossPay)
         # allow the user to run the program again if so desired without having to restart 
         answer = input("Do you wish to run the program again [Y/N]?")

   # End program gracefully
   print("\nThank you and goodbye!")
   
def wageFunction(): # function that obtaines hourly wage from user
   userInput = float(input("enter the hourly wage of the employee : ")) # user input hourly wage
   while (userInput < MIN_WAGE or userInput > MAX_WAGE): # input validation loop to remind the user to input from $ 7.50-$18.25
      print("!error!")
      print("please enter a minimun wage of $7.50 or a maximun wage of $18.25")     
      userInput = float(input("enter the hourly wage of the employee : ")) # user input hourly wage
      
   return userInput # return userInput 

def daysWorkedFunction(): # function that obtains hours worked from user
   userInput = int(input("enter the number of hours worked by the employee : ")) # user input hours worked 
   while (userInput < MIN_HOURS or userInput > MAX_HOURS): # input validation loop to remind the user to input 0-40
      print("!error!")
      print("please enter a minimum of 0 hours worked or a maximum of 40 hours worked")
      userInput = int(input("enter the number of hours worked by the employee : ")) # user input hours worked 

   return userInput # return userInput 

def employeeGrossPay(wageFunction, daysWorkedFunction): # fucntion that decides employees gross pay
   grosspay = wageFunction * daysWorkedFunction # employee wage * hours worked = gross employee pay
   return grosspay # return gross.pay  

def displayGrossFunction(grossPay): # funvtion that displays the employees gross wage 
   print("the total wages earned by employee ($): ", grossPay)
   
   # call main
main()      