# Programmer: Olmedo, Johnny

# Submission date: 09/10/2019

# This Program calculates job estimates for a paint company using functions

# Global constants for estimate

LABOR_COST = 20.00

STANDARD = 115.00 

def main (): 
   
   # Get the amount of wall space in square feet
   
   wallSpace = float(input("enter the square feet of wall space to be painted : "))
   
   # Get the price of paint per gallon
   
   paintPrice = float(input("enter the price of paint per gallon : "))
   
   # Calculate the number of gallons of paint required
   
   paint_required = wallSpace / STANDARD
   
   
   # Calculate the amount of labor hours required 
   
   labor_required = 8 * ( wallSpace / STANDARD) 
   
   # Calculate the cost of the paint 
   
   paint_cost = paintPrice * paint_required
   
   # Calculate the labor charges 
   
   labor_charges = labor_required * LABOR_COST
   
   # Calculate the total cost of the paint job
   
   total_cost = labor_charges + paint_cost
   
   # Display information
   
   PaintEstimate (paint_required, labor_required, paint_cost, labor_charges, total_cost)
   
def PaintEstimate (paint, labor, pcost, lcost, tcost):

   print()
   
   print("The number of gallons of paint required : ", paint)
   
   print("The hours of labor required : ", labor)
   
   print("The cost of paint is ($) : ", pcost)
   
   print("The labor charges are ($) : ", lcost)
   
   print("The total cost of the paint job ($) : ", tcost)
   
   #call main
 
main()         
