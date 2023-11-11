# Programmer: Olmedo, Johnny
# Submission date: 12/19/2021
# This program takes 3 strings for manipulation, the first two get concantondated together
# the third is reversed, the program uses functions and a modular format

def main():   
    # Explain what we are doing. 
    print("\nThis program performs string manipulation\n")
    # ask the user if they wish to continue  
    answer = input("Do you wish to continue [Y/N]? : ")
    # while user input is "Y" or "y" 
    while (answer == "Y" or answer == "y"): 
        # get the firsts string
        string1= string1_func()
        # get the second string
        string2= string2_func()
        # get the third string
        string3= string3_func()
        # call the function that will combine the two strings together
        string_concant = concant_func(string1, string2) # pass the first two strings
        # call the function that will reverse the 3rd string 
        reverse = reverse_string(string3) #pass the string 3
        # print the results
        print_func(string_concant, reverse) #pass the combined string and reversed string
        # ask if they want to run the program again
        answer = input("\n Do you wish to run the program again [Y/N]?: ")
   # End program gracefully
    print("\nThank you and goodbye!") 

# this function gets input for 1st string then returns it
def string1_func():
    # get input
    string1 = input("please input the first string: ")
    # return it
    return string1

# this function gets input for 2nd string then returns it
def string2_func():
    # get input
    string2 = input("please input the second string: ")
    # return it
    return string2

# this function gets input for 3rd string then returns it
def string3_func():
    # get input
    string3 = input("please input the third string: ")
    # return it
    return string3

# this function takes the first two strinsg and combines them into one string
def concant_func(first_str, second_str): # recieve the two strings
    # combine the two strings
    concant = first_str + second_str
    # return it
    return concant

# this function recieves the 3rd string and does a couple operations:
# 1. loads it into a string to demonstrate that it could be reversed more than one way
# 2. uses the copied string to do split and join operations
# 3. does the normal reversal and returns it
def reverse_string(third_str): # recieve the 3rd pass
    # make an empty string copy
    string_copy= []
    # go threw each character in the string
    for char in third_str:
        # append the characters to the string
        string_copy.append(char)

    # for fun show you read the chapters and gained some new knowledge
    # print what the string curretly looks like
    print("\nat this point the string looks like: ", end = '')
    print(string_copy)
    print("now we can reverse the list : ", string_copy[::-1]) # reverse reverse

    # show what hapends when you join the list with no space inbetween
    join_string = ''.join(string_copy)
    reversed_join_string = ''.join(string_copy[::-1]) # reverse it
    print("after joing the list togther with no space it now looks like: ", end = '')
    print(join_string, "and", reversed_join_string)

    # now lets join the list with a '.' beteen the charecters
    join_string = '.'.join(string_copy)
    print("now lets join the list with a '.' beteen the charecters, it looks like :", end ='')
    print(join_string, "and", join_string[::-1])

    # now go back threw the string a seperate it into a list of chars, take out the '.'
    new_chars = join_string.split('.')
    print("the same string above ^ got the '.' taken away and now it looks like", end = '')
    print(new_chars, "and", new_chars[::-1])
    # enough playing around return to the assignment, reverse the orginal string passed
    reversed = third_str[::-1]
    # return it 
    return reversed

# now print the concantinated string and reversed string
def print_func(concant, reversed): # recieve the correct strings
    print("\nconcantanted: ", concant) 
    print("reversed: ", reversed)

main() # call main
    