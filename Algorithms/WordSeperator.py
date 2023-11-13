# Programmer: Olmedo, Johnny
# This program is a word seperator
def main():
    # Call the displayMenu function to show the menu options
    displayMenu()

    # Ask the user to choose an option from the menu
    choice = input("Choose an option on the menu please: ")

    # While the user chooses not to exit
    while choice != "2":
        # Ask the user for a sentence
        sentInput = input("Enter a sentence with no spaces and caps at the beginning of each word: ")

        # Call the function that converts the sentence
        sent = sentFunc(sentInput)

        # Display the converted sentence
        print("The converted sentence:")
        print(sent)

        # Call the displayMenu function again
        displayMenu()

        # Ask the user the menu question again
        choice = input("Choose an option on the menu: ")

    # End the program gracefully
    print("\nThank you and goodbye!")


def displayMenu():
    # Display menu options
    print("\n1. Separate a sentence")  # Option 1
    print("2. Exit")  # Option 2


def sentFunc(sentence):
    empStr = ""  # Initialize an empty string

    # For loop to go through each index in the sentence
    for i in range(len(sentence)):
        if sentence[i].isupper():  # If the character is uppercase
            empStr += sentence[i]  # Add the uppercase letter to the string

            # For each character collected after the uppercase letter (i)
            for e in sentence[i + 1:]:
                if e.isupper():  # If it's uppercase
                    empStr += " "  # Add a space between each new line
                    break  # Break out of the loop
                empStr += e  # Add each character after the uppercase letter to the string

    return empStr  # Return empStr

# Call the main function to execute the program
main()

