def main():
    # Initialize an array
    array1 = [700, 105, 900, 33, 550, 140]

    # Call the larElement function to find the largest element
    element = larElement(array1)

    # Call the display function to print the result
    display(element)


# Recursive function to find the largest element in the array
def larElement(array1):
    # Base case: if the array has only one element, return that element
    if len(array1) == 1:
        return array1[0]

    # Recursive case: compare the first element with the largest element in the rest of the array
    if array1[0] > larElement(array1[1:]):
        return array1[0]

    # If the first element is not the largest, continue the recursion with the rest of the array
    return larElement(array1[1:])


# Function to display the result
def display(larNumber):
    print("The largest number in the array is:", larNumber)


# Call the main function to execute the program
main()
