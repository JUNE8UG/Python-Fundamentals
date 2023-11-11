# Critical Thinking Assignment #4 Option 1 
# Programmer: Olmedo, Johnny
# ITS-320
# Submission date: 12/12/2021
# This program can determine the total, average, max, min, and interest rate of multiple float values input by the user
# it also has input validation and exception handeling, please feel free to try and break the program 

def main():
    # describe what this program does
    print("\ncan determine the total, average, max, min, and interest rate of multiple float values input by the user, then prints it out\n")
    # ask the user if they wish to continue  
    answer = input("Do you wish to continue [Y/N]? : ")
    # while user input is "Y" or "y" 
    while (answer == "Y" or answer == "y"):
        # call the function that will get input and validate it from user
        getInput = inputFunc()
        # call the function that will get the total or sum of all the inputs
        total = totalFunc(getInput) # send the input from user
        # call the function that will get the average or mean of all the inputs
        average = averageFunc(total, getInput) # send the total and the og input
        # call the function that will get the largest number in the inputs
        max = maxFunc(getInput) # pass og the inputs
        # call the function that will get the smallesy number in the inputs
        min = minFunc(getInput) # pass the og inputs
        # call the interest function that calculates the 20 % interest on each inputed value
        interest = interestFunc(getInput) # pass og input 
        # call print function that prints og input, total, average, max, min, and interest of values
        printFunc(getInput, total, average, max, min, interest) # pass all info gathered to this point
        # ask user if they want o run program again
        answer = input("\n Do you wish to run the program again [Y/N]?: ")
       # End program gracefully
    print("\nThank you and goodbye!") 

# this function takes the 5 float inputs from user and returns only valid inputs
def inputFunc():
    # load up a list with 5 elements
    float_list = [1,2,3,4,5]

    # start going threw each element in the float_list
    for each in range(len(float_list)):
        # on the first loop
        if (float_list[each] == 1):
            # get input
            userIn = input("\nPlease enter the 1st of 5 floating point numbers: ")
            validIn = inputVal(userIn) # verify correct input
            # replce current int in the element spot with the one entered by user 
            float_list[each] = validIn

        # on the second loop
        if (float_list[each] == 2):
            # get input
            userIn = input("\nPlease enter the 2nd of 5 floating point numbers: ")
            validIn = inputVal(userIn) # verify 
            # replce current int in the element spot with the one entered by user 
            float_list[each] = validIn

        # on the third loop
        if (float_list[each] == 3):
            # get input
            userIn = input("\nPlease enter the 3rd of 5 floating point numbers: ")
            validIn = inputVal(userIn) # verify
            # replce current int in the element spot with the one entered by user
            float_list[each] = validIn

        # on the fourth loop
        if (float_list[each] == 4):
            # get input
            userIn = input("\nPlease enter the 4th of 5 floating point numbers: ")
            validIn = inputVal(userIn) # verify
            # replce current int in the element spot with the one entered by user
            float_list[each] = validIn

        # on the fifth loop
        if (float_list[each] == 5):
            userIn = input("\nPlease enter the 5th of 5 floating point numbers: ")
            validIn = inputVal(userIn) # verify
            # replce current int in the element spot with the one entered by user
            float_list[each] = validIn
        # each time print what the list looks like
        print(float_list)
    
    return float_list # list verified

# this function makes sure that the input given by the user is a float or int that can be made
# into a float, and if not wont let the user continue till verified
def inputVal(gotInput):  
    # first see if the the user immediatly entered the right input
    try:
        val = float(gotInput) # see if the input is a float
    # if it's not a float its okay, but stop the program from stopping due to error
    except ValueError:
        # while the input is not a numeric number
        while gotInput.isnumeric() == False:
            # remind the user to enter the right input
            print('\nit looks like you input a non float or int: ') 
            gotInput = input("\nPlease enter a valid float or int: ") # get another input
            # check again if this time they input a float or numeric number
            try: 
                val = float(gotInput)
            # if its not a float or numeric then just restart the loop and ask them for the right value again
            except ValueError:
                pass # pass
            # if the user does enter a float or numeric then return it
            else:
                # return the correct value
                return val 
        return float(gotInput) # if the input is already a float or int, we can return the float value with no issues
    # else the user entered a float or numeric so return the value 
    else:
        return val

# this function recieves the list that the user input and determines how many numbers 
# are in the list 
def totalFunc(list_receved):
    # use built in sum function to add up all the numbers in the list
    total = sum(list_receved)
    # return the total
    return total

# this function recieves the total and the original list so it can determine the average
def averageFunc(total_recieved, list_recieved):
    # assign sum as total that was given
    sum = total_recieved
    # use built in len function to deter,ine how many number are in the list
    length = len(list_recieved)
    # average = sum / all the numbers used to get some
    average = sum / length
    # return the average
    return average

# this function recives the list/input from user and locates the largest number    
def maxFunc(list_recieved):
    # use the built in max function
    max_num = max(list_recieved)
    # return the largest number 
    return max_num

# this function recives the list/input from user and locates the smallest number
def minFunc(list_recieved):
    # use the built in min function from python
    min_num = min(list_recieved)
    # return the smallest number
    return min_num

# this function will give back a 20% interest of all the values given
def interestFunc(list_recieved):
    # make a brand new list that will hold all values at an interest rate of 20%
    interest_list = []
    # for every value in the list input from user, we will go threw and convert using the equation given
    for each in range(len(list_recieved)):
        #Interest_Value = Original_value + Original_value*0.2
        interest_value = list_recieved[each] + (list_recieved[each] * 0.2)
        # add to the list
        interest_list.append(interest_value) 
        # return the new list
    return interest_list

# this function prints out all information determined 
def printFunc(ogInput, total_recieved, average_recieved, max_recieved, min_recieved, interest_recieved):
    # print out the orginal input
    print("\noriginally you entered these 5 numbers: ", ogInput)
    # print out the total / sum
    print("\nthe total from adding all those numbers you input is: ", total_recieved)
    # print out the average or mean
    print("\nthe average of all the numbers entered is: ", average_recieved)
    # print the largest number found
    print("\nthe largest number you input is: ", max_recieved)
    # print the smallest number found
    print("\nthe smallest number you input is: ", min_recieved)
    # print all inputed values as a 20% interest rate
    print("\nthe value of all the numbers you entered with a 20% interest is: ", interest_recieved)
main() #call main