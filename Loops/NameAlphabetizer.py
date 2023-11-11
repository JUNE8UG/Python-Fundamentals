# Submission Date: September 25, 2019
# This program determines the first and last names alphabetically from an entered list of names.
# The user will enter a list of names.

def main():
 
    # Explain what we are doing. 
    print("This program determines the first and last names alphabetically from an entered list of names. ")
    
    answer = input("Do you wish to continue [Y/N]?")
    
    while (answer == "Y" or answer == "y"):
    
        # make the first entry
        firstName = str(input("Enter the first name (Enter STOP to stop the program):  "))
        print("You entered ", firstName)
        # if the user enters STOP, stop the program
        if firstName != "STOP":
            alphabetize(firstName)
        else:
            print("You stopped the program.")
        
        # allow the user to run the program again if so desired without having to restart    
        answer = input("Do you wish to run the program again [Y/N]?")
        
    # End program gracefully
    print("\nThank you and goodbye!")
    
def alphabetize(value1):

    # initialize both variables to the first value entered
    first = value1
    last = value1
    # intialize the condition
    condition = True
    while condition:
        new = str(input("Enter theTerry next name (Enter STOP to stop the program):  "))
        print("You entered ", new)
        # if the user enters STOP, stop the program
        if new == "STOP":
            condition = False
        # determine if the newly entered name is lower or higher alphabetically than previously entered names
        elif new < first:
            first = new
        elif new > last:
            last = new
        else:
            ("You entered an invalid entry.")
     
    print("The alphabetical first name entered was ", first) 
    print("The alphabetical last name entered was ", last)   

# Call main()    
main()    



