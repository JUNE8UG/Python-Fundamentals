# Programmer: Olmedo, Johnny

# Submission date: 09/10/2019

# This Program calculates the amount of income generated from ticket sales

# Global constants for ticket sales

A_SEATS = 15.00

B_SEATS = 12.00

C_SEATS = 9.00

def main ():
    
   # Get the number of tickets in each section
   
   aseats = float(input("enter the number of tickets sold for class A seating : "))
   
   bseats = float(input("enter the number of tickets sold for class B seating : "))
   
   cseats = float(input("enter the number of tickets sold for class C seating : ")) 
   
   # Calculate the income generated from ticket sales
   
   income_a = aseats * A_SEATS
   
   income_b = bseats * B_SEATS
   
   income_c = cseats * C_SEATS
   
   # Display information about sale 
   
   IncomeGenerated (income_a, income_b, income_c)
   
def IncomeGenerated (classa, classb, classc):
   
   print()   
   
   print("the income generated from class A tickets sold is ($): ", classa)
   
   print("the income generated from class B tickets sold is ($): ", classb)
   
   print("the income generated from class C tickets sold is ($): ", classc)
   
   #call main

main()    
