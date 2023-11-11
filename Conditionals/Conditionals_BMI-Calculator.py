# Programmer: Olmedo, Johnny

# Submission date: 09/21/2019

# This Program calculates Body Mass Index

def main():
   # Get the height in feet of the user
   height = float(input("enter your height in inches : "))
   # Get the weight in pounds
   weight = float(input("enter your weight in pounds : "))
   # Calculate Body Mass Index
   body_mass = (weight * 703) / (height * height) 
   # Communicate this information
   bodyMass (height, weight, body_mass)

def bodyMass (inches, lbs, bmi):
   # Determine whether the user is underweight, optimal, or overweight 
   if (bmi >= 18.5 and bmi <= 25):
     print("your weight is considerd to be optimal.")
   elif (bmi > 25):
     print("your weight is considerd to be overweight.")
   else:
     print("your weight is considerd to be underweight.") 
   # Call main
main()     
       
   
     