# Program 5 exercise # 10
# Programmer: Olmedo, Johnny
# CSC119-141
# Submission date: 09/28/2019 
# This program calculates largest and highest value of a sequence of numbers 
# main module 
def main():
   # Display purpose of program 
   print("this program calculates the largest and smallest value of a series of numbers")
   print("using a while loop")
   
   answer = input("Do you wish to continue [Y/N]? ")
   
   while (answer == 'Y' or answer == 'y'):
      # Initilize exit
      exit = -99
       # Get the series of numbers
      number = int(input("enter a number (or -99 to exit) : "))
      # Set criteria for highest value
      while (exit < number):
         # set initial number as lowest number
         lowest = number
         # Get the next number 
         number = int(input("enter a number (or -99 to exit : "))
          
      # Display largest and smallest numbers
      displayNumbers(lowest, number) 
      
      answer = input("Do you wish to continue [Y/N]? ") # present an continuation/exit rout for the user
   
   print ("\nThank you and goodbye!") # end program graceflly 

def displayNumbers(least, numbers):
   if (least < numbers): 
     print()
     print("the smallest number entered is : ", least)
     print("the largest number entered is : ", numbers)  
   else:
     print()
     print("the largest number entered is : ", least)
     print("the smallest number entered is : ", numbers)    

   # Call main
   
main()       
      
           

