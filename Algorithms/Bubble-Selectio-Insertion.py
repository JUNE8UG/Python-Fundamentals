# Programmer: Olmedo, Johnny
# Submission date: 10/29/2019 
# This program locates a value in a list of 20 integers using both the sequential search algorithm and 
# the binary search algorithm to locate the same value in an array and print out the number of comparissons made by each 
import random
import copy


def main():
    # Give user a chance to quit the program
    print("This program organizes 3 lists of random numbers using the insertion, selection, and bubble sort algorithms")
    answer = input("Do you wish to continue [Y/N]? ")
    while (answer.lower() == "y" or answer.lower() == "YES"):
        # call 1024 random integers function
        print("\nList of 1024 random integers")
        print()
        AIntegers = randomA(1024)
        print("\nList of 4096 random integers")
        print()
        # call the 4096 integers function
        BIntegers = randomA(4096)
        print("\nList of 16384 random integers")
        print()
        # call the 16384 integers function
        CIntegers = randomA(16384)
        # ask the user if they want to run the program
        answer = input("\nDo you wish to continue [Y/N]? ")
    # say goodbye
    print("\nGoodbye")


def randomA(iterations):
    listA = []
    # initilize for loop for list of 1024 integers
    for num in range(iterations):
        # mak a variable that will hold the random number generated
        randNumber = random.randint(1, 100)
        # append the array to hold all the values as the loop is producing them
        listA.append(randNumber)
    listB = listA.copy()
    listC = listA.copy()
    # call bubble sort
    bubbleSortAlgorithm = bubbleSort(listA)
    print("the bubble sort algorithm made ", bubbleSortAlgorithm, "swaps")
    #  call selection sort function
    selectionSortAlgorithm = selectionSort(listB)
    # report the number of swaps made
    print("the selection sort algorithm made ", selectionSortAlgorithm, "swaps")
    # call the insertion sort function
    insertionSortAlgorithm = insertion_sort(listC)
    # report the number of swaps made
    print("the insertion sort algorithm made ", insertionSortAlgorithm, "swaps")


def bubbleSort(listA):
    # Set max_element to the length of the arr list, minus
    # one. This is necessary for the outer loop.
    maxElement = len(listA) - 1
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
            if listA[index] > listA[index + 1]:
                # Swap the two elements.
                temp = listA[index]
                listA[index] = listA[index + 1]
                listA[index + 1] = temp
                count += 1
                # Increment index.
            index = index + 1
            # Decrement max_element.
        maxElement = maxElement - 1
    # print out bubble sorted list
    print("the bubble sorted version of listA is :")
    print(listA)
    # return the count
    return count


def selectionSort(listB):
    # Set startScan to 0. This is necessary for
    # the outer loop. It is the starting position
    # of the scan.
    startScan = 0
    count = 0

    # The outer loop iterates once for each element in the
    # list. The startScan variable marks the position where
    # the scan should begin.
    while startScan < len(listB) - 1:
        # Assume the first element in the scannable area
        # is the smallest value.
        minIndex = startScan
        minValue = listB[startScan]

        # Initialize index for the inner loop.
        index = startScan + 1

        # Scan the list, starting at the 2nd element in
        # the scannable area. We are looking for the smallest
        # value in the scannable area.
        while index < len(listB):
            if listB[index] < minValue:
                minValue = listB[index]
                minIndex = index
            # Increment index.
            index = index + 1
        # Swap the element with the smallest value
        # with the first element in the scannable area.
        listB[minIndex] = listB[startScan]
        listB[startScan] = minValue
        count += 1
        # Increment startScan.
        startScan = startScan + 1
    # print selection sorted list
    print("the selection sorted version of listB is:")
    print(listB)
    # return count
    return count


def insertion_sort(listC):
    # Set index to 1 for the outer loop.
    index = 1
    count = 0
    # The outer loop steps the index variable through
    # each subscript in the list, starting at 1. This
    # is because element 0 is considered already sorted.
    while index < len(listC):
        # The first element outside the sorted subset is
        # arr[index]. Assign the value of this element
        # to unsorted_value.
        unsorted_value = listC[index]
        # Start the scan variable at the subscript of the
        # first element outside the sorted subset.
        scan = index

        # Move the first element outside the sorted subset
        # into its proper position within the sorted subset.
        while scan > 0 and listC[scan - 1] > unsorted_value:
            count += 1  # add 1 to counter every time the loop iterates
            listC[scan] = listC[scan - 1]
            scan = scan - 1
        # Insert the unsorted value in its proper position
        # within the sorted subset.
        listC[scan] = unsorted_value
        # Increment index.
        index = index + 1
    # print the insertion sorted list
    print("the insertion sorted version of listC is:")
    print(listC)
    # return count
    return count


main()
