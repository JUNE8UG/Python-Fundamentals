# Program 8 exercise # 8
# Programmer: Olmedo, Johnny
# CSC119-141
# Submission date: 10/26/2019 
# This program determines pay wage of multiple employees
def main():
   # Initialize list
   empId = [56588, 45201, 78951, 87775, 84512, 13028, 75804]
   hours = [0, 1, 2, 3, 4, 5, 6]
   payRate = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
   wages = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]             
   
   # Dislay purpose of program to the user
   print("This program calculates employee pay roll")
   
   # Give user a chance to quit the program
   answer = input("Do you wish to continue [Y/N]? ")
   
   while (answer. lower() == "y" or answer.lower() == "YES"):    
      # call function that will retrieve user inputs
      inputData = dataInput(empId, hours, payRate, wages)
      # call function that will display information
      displayInf = displayFunc(empId, wages)   
      # Give user a chance to quit the program
      answer = input("\nDo you wish to continue [Y/N]? ")
   print("Thank you and goodbye")
   
def dataInput(empId, hours, payRate, wages):
   # for empNum in range(len(empId)):                
   for empNum in range(len(empId)):
      # display the employe number
      print("emplyee number: ", empId[empNum])
      # retrieve hours worked
      hours[empNum] = int(input("enter the number of hours worked by the employee : "))  
      # input validation
      while (hours[empNum] < 0):
         print("invalid value")
         print("please enter a number equal to")
         print("or greater than 0")
         hours[empNum] = int(input("enter the number of hours worked by the employee : "))    
      # retrieve houly rate
      payRate[empNum]= int(input("enter the employees pay rate : "))
      # input validation
      while(payRate[empNum] < 0):
         print("invalid value")
         print("please enter a number equal to")
         print("or greater than 0")
         payRate[empNum]= int(input("enter the employees pay rate : "))         
      # calculate wage (hours * rate)
      wages[empNum] = hours[empNum] * payRate[empNum] 
  
def displayFunc(empId, wages):
   # for each element in empId array
   for i in range(len(empId)):
      # print the Emdployee ID 
      print(empId[i])
      # print wages earned
      print("the wage earned by the employee ($): ", wages[i])   

# Call main() 
main()    