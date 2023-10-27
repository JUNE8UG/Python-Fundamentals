# Program 5 exercise # 9
# Programmer: Olmedo, Johnny
# CSC119-141
# Submission date: 09/25/2019 
# This program calculates pennies for pay
# main module 
def main():
   # Display purpose of program 
   print("this program calculates the amount of money a person would earn over a period time if his or her salary salary doubles")
   print("using a for loop")
   
   answer = input("Do you wish to continue [Y/N]? ")  
   
   while(answer == 'y' or answer == 'Y'): 
       
       # retrieve number of days worked
       numDays = int(input("Enter the number of days worked: "))
       # Initilize start pay
       numPennies = 0.01 # my starting salary
       # Display table
       displayTable(numDays, numPennies)
       # ask the user if they want to run the loop again
       answer = input("Do you wish to continue [Y/N]? ")
   
   # End program gracefully
   print ("\nThank you and goodbye!")
   
def displayTable(days, salary):
   # Display the salary for several days
   print("\nDays \t", "Salary")

   # for every day in the number of days worked
   for days in range(1, days + 1):   
      # Display the days and salary 
      print(days, "\t\t$", salary) # \t\t is a table notation
      # pay for the next day
      salary = salary * 2 
      # calculate total 
      totalPay = salary

   # display the total
   print("\n Total Pay ($): ", totalPay)
 # Call main ()
main()      