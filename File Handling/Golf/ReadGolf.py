def main():
    # Create an empty list to store lines from the file
    fileLines = []

    # Open the file "golf.txt" in read mode ("r")
    with open("golf.txt", "r") as readFile:
        # Iterate through each line in the file
        for each in readFile:
            # Append each line to the fileLines list, removing leading and trailing whitespaces
            fileLines.append(each.strip())

    # Print the list of fileLines containing the contents of the file
    print(fileLines)

# Call the main function to execute the code
main()

