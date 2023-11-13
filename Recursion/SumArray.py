# Programmer: Olmedo, Johnny
# Submission date: 12/4/2019 
# This program return the sum of an array
def main():
    # Ask the user for an integer
    userInput = int(input("Enter a number to find the sum of: "))

    # Call the sumFunction to calculate the sum
    sum_result = sumFunction(userInput)

    # Call the display function to print the result
    display(sum_result, userInput)

    # Alternative approach using a loop to calculate the sum
    sum_alternative = 0
    for i in range(userInput):
        sum_alternative += i + 1
    print("Sum using an alternative approach:", sum_alternative)


def sumFunction(num):
    # Base case: if the number is 1, return 1
    if num == 1:
        return num
    else:
        # Recursive case: call sumFunction with num - 1 and add the current num
        return sumFunction(num - 1) + num


def display(dissum, uInput):
    print("The sum from 1 to", uInput, "is", dissum)


# Call the main function to execute the program
main()
