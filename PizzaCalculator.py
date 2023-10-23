# Programmer: Olmedo, Johnny

# Submission date: 08/30/2019

# This Program calculates the number of slices that will be left over at a pizza party

def main ():
    # Get the number of full pizzas there will be
    pizza = float(input("enter the number of pizzas there will be : "))
    # Get the number of slices each pizza will contain
    slices = float(input("enter the number of slices each pizza contains : "))
    # Get the number of people attending the party
    people = float(input("enter the number people that will be attending the party : "))  
    # Calculate the number of slices each person will eat at the party
    slices_needed = people * 3
    # Calculate the number of slices that would be left over 
    left_over = pizza * slices - slices_needed 
    print() 
    print("Number of slices that will be left over : ", left_over)

#call main

main()     