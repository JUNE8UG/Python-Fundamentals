# Programmer: Olmedo, Johnny

# Submission date: 09/09/2019

# This Program calculates the assessment value and property tax of a piece of property

# Global constants for percentage of properties actual value and property tax 
ASSESMENT_VALUE = 0.60
PROPERTY_TAX = 0.0064

def main ():
   # Get the actual value of a piece of property
   property = float(input("enter the value of a piece of property ($): "))
   # Calculate the assesment value
   assesvalue = property * ASSESMENT_VALUE
   # Calculate property tax 
   property_tax = assesvalue * PROPERTY_TAX
   # Display assesment value and property tax
   PropertyInfo ( assesvalue, property_tax)
   
def PropertyInfo ( value, tax): 
   print()
   print("the assesment value of the property is ($): ", value)
   print("the property tax of the property is ($): ", tax)
   
   #call main
main()      