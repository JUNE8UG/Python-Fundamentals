# Programmer: Olmedo, Johnny

# Submission date: 09/22/2019

# This Program calculates minuets, hours, seconds 

# Global constants for time calculator

def main():
   # Ask the user to enter any number of seconds  
   number_seconds = float(input("enter any number of seconds : ")) 
   # Conversions for minutes, hours, days
   seconds = number_seconds
   minutes = number_seconds / 60 # seconds to minutes
   hours = number_seconds / 3600 # minutes to hours
   days = number_seconds / 86400 # hours to days


   # Determine whether the number of seconds can be shown in minuets, hours, or days
   # if the number of seconds is less than zero let the user know they entered the information incorrectly
   if (number_seconds < 0):
     print("the number you entered is invalid, please try again")
   # if the seconds enetered is between 60 and 3600

   elif (number_seconds >= 60 and number_seconds < 3600):
       # display the number of minutes
     print("the number of minutes is : ", minutes) # conversion to minutes

   # if the seconds enetered is between 3600 and 86400
   elif (number_seconds >= 3600 and number_seconds < 86400):
   # print the number of hours this is
     print("the number of hours is : ", hours) # conversion for hours

   # if the number of seconds is greater than
   elif (number_seconds >= 86400):
   # print the number of days this is
     print("the number of days is : ", days) # conversion for days

   else:
     print("the number of seconds is : ", seconds)  # conversion for seconds
    # call main        

main()