# Programmer: Olmedo, Johnny

# Submission date: 09/21/2019

# This Program is a change counting game 

# Global constants for game 

PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25


def main():
    # Get the number of coins
    pennies = float(input("enter the number of pennies : "))
    nickels = float(input("enter the number of nickels : "))
    dimes = float(input("enter the number of dimes : "))
    quarters = float(input("enter the number of quarters : "))
    # Calculate change price
    penny_price = pennies * PENNY
    nickel_price = nickels * NICKEL
    dime_price = dimes * DIME
    quarter_price = quarters * QUARTER
    # Display information about the game
    winLoss(penny_price, nickel_price, dime_price, quarter_price)


def winLoss(pen, nic, dim, quart):
    # determine if they won or lost the game
    if (pen + nic + dim + quart == 1.00):
        print("CONGRATULATIONS YOU WON THE GAME!")
    elif (pen + nic + dim + quart > 1.00):
        print("Unfortunately the amount you entered is more than a dollar")
    else:
        print("Unfortunately the amount you entered was less that a dollar")

    # Call main


main()
