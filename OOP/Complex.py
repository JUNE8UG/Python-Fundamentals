# Critical Thinking Assignment #6 Option 1 
# Programmer: Olmedo, Johnny
# ITS-320
# Submission date: 01/2/2022
# This program does add,sub,mult,div,mod, etc and uses classes and object oriented code to accomplish it 

import math


# create class named complex
class Complex(object):  # pass object
    # initilizes real and imaginary
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # this function adds the two parameters given
    def __add__(self, no):
        # enter your code here
        real = self.real + no.real  # real numbers
        imaginary = self.imaginary + no.imaginary  # imaginary numbers
        # return the added real and imaginary numbers
        return Complex(real, imaginary)

    # this function subtracts the two parameters
    def __sub__(self, no):
        # enter your code here         
        real = self.real - no.real  # real numbers
        imaginary = self.imaginary - no.imaginary  # imaginary numbers
        # return two subtratced numbers
        return Complex(real, imaginary)

        # this function multiplies two parameters

    def __mul__(self, no):
        # set real
        # real = a*b - ai*bi
        real = self.real * no.real - self.imaginary * no.imaginary
        # imaginary = ai*b + a*bi
        imaginary = self.imaginary * no.real + self.real * no.imaginary
        # return real and imaginery 
        return Complex(real, imaginary)

    # this function divides two parameters
    def __truediv__(self, no):
        # m = (b * b)+ (bi* bi)
        m = no.real * no.real + no.imaginary * no.imaginary
        # real = (a*b) + (ai*bi) / m
        real = (self.real * no.real + self.imaginary * no.imaginary) / m
        # imaginary = (ai*b) - (a*bi) / m
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / m
        # reutn real and imaginary
        return Complex(real, imaginary)

    # this function does modulus operation on either x or y mod
    def mod(self):
        # real = math.sqrt((a*a) + (ai*ai))
        real = math.sqrt(self.real * self.real + self.imaginary * self.imaginary)
        # return real and 0
        return Complex(real, 0)

    # this function will return the correct executuions needed for the imaginery numbers
    def __str__(self):
        # creat real_str and imag_str variables
        real_str = ''
        imag_str = ''
        # if a does not equal 0
        if self.real != 0:
            # real_str = a with 2 decimal spot format
            real_str = "{:.2f}".format(self.real)
        else:
            # else we set it to just 0
            real_str = "0.00"

        # if ai does not equal 0  
        if self.imaginary != 0:
            # check if ai is less than 0
            if self.imaginary < 0:
                # if it's it then we make imag_str = ai with appropriate format
                imag_str = "{:.2f}".format(self.imaginary) + "i"
            # else we set imag_str = +(ai)i with proper formating
            else:
                imag_str = "+" + "{:.2f}".format(self.imaginary) + "i"

        # else ai = +0.00i
        else:
            imag_str = "+0.00i"
            # add real and imaginary
        result = real_str + imag_str
        return result  # return


def main():
    # Explain what we are doing. 
    print("\nThis program performs mathmatical operations for complex numbers\n")
    # ask the user if they wish to continue  
    answer = input("Do you wish to continue [Y/N]? : ")
    # while user input is "Y" or "y" 
    while (answer == "Y" or answer == "y"):
        print("enter the complex numbers: ")
        C = map(float, input().split())
        D = map(float, input().split())
        x = Complex(*C)  # "*" means theres multiple perameters
        y = Complex(*D)
        print('\n'.join(map(str, ["Addition: ", x + y, "Subtraction: ", x - y, "Multiplication: ", x * y, "Division: ",
                                  x / y, "X mod: ", x.mod(), "Y mod: ", y.mod()])))
        # ask if they want to run the program again
        answer = input("\n Do you wish to run the program again [Y/N]?: ")
    # End program gracefully
    print("\nThank you and goodbye!")


main()
