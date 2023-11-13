# Programmer: Olmedo, Johnny
# Submission date: 10/01/2019 
# This program calculates generates 100 random numbers and keeps a count of how many of those are even and odd

import random


def main():
    num = random.randint(1, 1000)  # generaterandom integer
    oddresult = oddNum(num)  # container to hold value of evenodd(num)
    evencount = 100 - oddresult  # container to determine and hold the number of even numbers
    displayResult(oddresult, evencount)  # display count of even/odd numbers


def oddNum(num):
    oddcount = 0  # keeps track of odd numbers
    for num in range(100):  # Fix this to work with 100 values
        if num % 2 == 0:  # if the number modulo 2 equals to 0
            oddcount = oddcount + 1  # same as oddcount++
    return oddcount  # return the number of odd values


def displayResult(eveN, odD):
    print("the value of even numbers : ", eveN)  # display the number of even numbers generated
    print("the value of odd numbers : ", odD)  # display the number of odd numbes generatd


main()
