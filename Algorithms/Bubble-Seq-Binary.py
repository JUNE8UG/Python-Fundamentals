# Programmer: Olmedo, Johnny
# Submission date: 10/29/2019 
# This program locates a value in a list of 20 integers using both the sequential search algorithm and 
# the binary search algorithm to locate the same value in an array and print out the number of comparissons made by each 
import random


def main():
    # Give user a chance to quit the program
    print(
        "This program locates a value in a list of 20 integers using both the sequential search algorithm and the binary search algorithm to locate the same value")
    print("in an array and print out the number of comparissons made by each ")
    answer = input("Do you wish to continue [Y/N]? ")
    # initialize the first array
    arrayA = []
    # for loop to itirate random number twenty times
    for num in range(20):
        # make a variable that will hold the random number generated
        randNumber = random.randint(1, 100)
        # append the array to hold all the values as the loop is producing them
        arrayA.append(randNumber)
    # make array B as a copy of array A
    arrayB = arrayA.copy()
    # call bubble sort to place elements in ascending order
    bubbleSortAlgorithm = bubbleSort(arrayA)
    while (answer.lower() == "y" or answer.lower() == "YES"):
        # have the user enter a number element for both search algorithms
        inputElement = int(input("\nEnter any obtainable value in the list: "))
        # call sequential search function to run a sequential search
        sequentialSearch = sequential(arrayB, inputElement)
        print("the sequential search algorithm made ", sequentialSearch,
              "comparisons")  # print out the number of comparisons made by the sequential search algorithm
        # call the binary search function to run a binary search
        binarySearchAlgorithm = binarySearch(arrayB, inputElement)
        print("the binary search algorithm made ", binarySearchAlgorithm,
              "comparisons")  # print out the number of comparisons made by the binary search algorithm
        # Give user a chance to quit the program
        answer = input("\nDo you wish to continue [Y/N]? ")
    # say goodbye
    print("\nGoodbye")


def bubbleSort(arrayA):
    # Set max_element to the length of the arr list, minus
    # one. This is necessary for the outer loop.
    maxElement = len(arrayA) - 1
    count = 0
    # The outer loop positions max_element at the last element
    # to compare during each pass through the list. Initially
    # max_element is the index of the last element in the array.
    # During each iteration, it is decreased by one.
    while maxElement >= 0:
        # Set index to 0, necessary for the inner loop.
        index = 0

        # The inner loop steps through the list, comparing
        # each element with its neighbor. All of the elements
        # from index 0 thrugh max_element are involved in the
        # comparison. If two elements are out of order, they
        # are swapped.
        while index <= maxElement - 1:
            # Compare an element with its neighbor.
            if arrayA[index] > arrayA[index + 1]:
                # Swap the two elements.
                temp = arrayA[index]
                arrayA[index] = arrayA[index + 1]
                arrayA[index + 1] = temp
                # add 1 to the count for each iteration
                count += 1
                # print("\nSwapped", arrayA[index], "with", arrayA[index + 1])

            # Increment index.
            index = index + 1

            # Decrement max_element.
        maxElement = maxElement - 1
    print("the bubble sorted version of array A is:")
    print(arrayA)


def sequential(arrayB, inputElement):
    # Get number
    count = 0
    # Reset foundName
    foundName = False
    # names = ["joe", "mary", "john"]
    # Validate name
    # index == specific name is name list
    print(arrayB)
    for index in range(len(arrayB)):
        count += 1
        if (inputElement == arrayB[index]):  # if userInput == name in names list
            foundName = True  # set foundName = true if statement was true
            foundElementLocation = index  # foudNameLocation saves the correct userInput
            break
    if foundName == True:  # if statemet to determine whether user input was true or false
        pass
        # print foundName along with that persons number
        # print(arrayB[foundElementLocation])
        # print that the uer input was not found
    else:
        print(inputElement, "is not found")
        # print number of comparissons made
    # print(count)
    return count


def binarySearch(searchList, value):
    # Initialize the first and last indices of the search range
    first = 0
    last = len(searchList) - 1

    # Initialize variables for position, found status, and a count of iterations
    position = -1
    foundBin = False
    count = 0

    # Perform binary search while the search range is valid and the target is not found
    while (not foundBin and (first <= last)):
        # Increment the iteration count
        count += 1

        # Calculate the middle index of the current search range
        middle = int((first + last) / 2)

        # Check if the middle element is the target value
        if (searchList[middle] == value):
            foundBin = True
            position = middle
        # If the target is smaller, adjust the search range to the left
        elif (searchList[middle] > value):
            last = middle - 1
        # If the target is larger, adjust the search range to the right
        else:
            first = middle + 1

    # Return the count of iterations
    return count


# call main
main()
