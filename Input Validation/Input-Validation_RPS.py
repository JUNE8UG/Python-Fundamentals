# Programmer: Olmedo, Johnny

# Submission date: 10/06/2019

# This program lets you play rock paper scissors with the computer
import random 
def rockPaperScissorsGame():
    rock = 1
    paper = 2
    scissors = 3
 
    while(True):
        #Generate random number and store
        computerChoice = random.randint(1,3)
        # Ask user for input rock, paper, or scissors
        userInput = input("Choose between rock, paper, or scissors : \n")
        while(userInput != "rock" and userInput != "paper" and userInput != "scissors"):
           print("invalid answer")
           print("please enter enter either rock, paper, scissors")
           print("(lower case sensitive and correct spelling required)") 
           userInput = input("Choose between rock, paper, or scissors : \n")  
        if (userInput == "rock"):
         userChoice = rock  
        elif (userInput == "paper"):  
         userChoice = paper
        else:         
         userChoice = scissors 
        # Display computers choice
        if(computerChoice == rock):
            print("Computer's choice is rock\n")
        elif(computerChoice == paper):
            print("Computer's choice is paper\n")
        else:
            print("Computer's choice is scissors\n")
        #Compare/decide the winner and display
        if (userChoice == rock):
            if(computerChoice == rock):
                print("It's a tie, try again!!!\n")
                pass
            elif(computerChoice == paper):
                print("Computer wins!!!\n")
                break
            else: #computer chose scissors
                print("User wins!!!\n")
                break
        elif (userChoice == paper):
            if(computerChoice == rock):
                print("User wins!!!\n")
                break
            elif(computerChoice == paper):
                print("It's a tie, try again!!!\n")
                pass
            else: #computer chose scissors
                print("Computer wins!!!\n")
                break
        elif (userChoice == scissors):
            if(computerChoice == rock):
                print("Computer wins!!!\n")
                break
            elif(computerChoice == paper):
                print("User wins!!!\n")
                break
            else: #computer chose scissors
                print("It's a tie, try again!!!\n")
                break
 
def main():
   # Explain what we are doing. 
   print("This program plays rock paper sciccors with the user")
    
   answer = input("Do you wish to continue [Y/N]? ")
    
   while (answer == "Y" or answer == "y"):     

      rockPaperScissorsGame()
      answer = input("Do you wish to run the program again [Y/N]? ")
   # End program gracefully
   print("\nThank you and goodbye!")
    
main()


