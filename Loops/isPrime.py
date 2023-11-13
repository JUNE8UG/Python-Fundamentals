# Programmer: Olmedo, Johnny
# Submission date: 10/05/2019 
# This program determines if a number is prime 


def main():  # main module
    num = int(input("enter a number : "))  # get a number from the user
    result = isPrime(num)  # container to hold the value of isPrime(number)
    if result == ("true"):
        print("the number is a prime number")
    else:
        print("the number is not prime")


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:  # determine if the number modulo i equals to 0
            return ("false")  # if number modulo i equals to 0 the number is not a prime number
        return ("true")  # if number modulo i equals to 0 the number is a prime number

    # call main


main()
