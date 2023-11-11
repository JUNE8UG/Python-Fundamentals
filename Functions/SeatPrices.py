# Programmer: Olmedo, Johnny
# Submission date: 10/05/2019
# This program determines the prime numbers from 1-1

# Constants for the maximum number of seats in each section
SECTION_A_SEATS = 300
SECTION_B_SEATS = 500
SECTION_C_SEATS = 200

# Constants for the price of seats in each section
SEATS_A = 20
SEATS_B = 15
SEATS_C = 10


def main():
    # Get input for the number of tickets in each section
    seatsA = getTicketsInput("A", SECTION_A_SEATS)
    seatsB = getTicketsInput("B", SECTION_B_SEATS)
    seatsC = getTicketsInput("C", SECTION_C_SEATS)

    # Calculate and display the revenue for each section
    showRevenue(seatsA, seatsB, seatsC)


def getTicketsInput(sectionName, sectionCapacity):
    # Prompt the user to enter the number of tickets for a given section
    question = "Enter the number of tickets for section " + sectionName + ':'
    numberOfTickets = int(input(question))

    # Validate the input to ensure it's within the valid range
    while (numberOfTickets < 0 or numberOfTickets > sectionCapacity):
        print("Invalid input, please try again.")
        numberOfTickets = int(input(question))

    return numberOfTickets


def showRevenue(forSeatsA, forSeatsB, forSeatsC):
    # Calculate the revenue for each section based on the number of seats and seat prices
    revenueA = forSeatsA * SEATS_A
    revenueB = forSeatsB * SEATS_B
    revenueC = forSeatsC * SEATS_C

    # Display the revenue for each section
    print("The revenue made for A section is ($): ", revenueA)
    print("The revenue made for B section is ($): ", revenueB)
    print("The revenue made for C section is ($): ", revenueC)


# Call the main function to start the program
main()
