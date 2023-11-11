# Programmer: Olmedo, Johnny

# Submission date: 09/16/2019

# This Program calculates software sales 

# Global constants package price 

PACKAGE = 99.00


def main():
    # Get the number of packages purchased
    packages_purchased = float(input("enter the number of packages purchased : "))

    # Calculate price of packages
    package_price = packages_purchased * PACKAGE

    # Calculate the discount
    discount0 = package_price * 0.00
    discount1 = package_price * 0.20
    discount2 = package_price * 0.30
    discount3 = package_price * 0.40
    discount4 = package_price * 0.50

    # Detrmine the discount
    if (packages_purchased >= 10 and packages_purchased <= 19):
        print("the discount is ($) : ", discount1)
    elif (packages_purchased >= 20 and packages_purchased <= 49):
        print("the discount is ($) : ", discount2)
    elif (packages_purchased >= 50 and packages_purchased <= 99):
        print("the discount is ($) : ", discount3)
    elif (packages_purchased >= 100):
        print("the discount is ($) : ", discount4)
    elif (packages_purchased < 0):
        print("invalid purchase number... try again")
    else:
        print("the discount is ($) : ", discount0)

    # Display information
    if (packages_purchased >= 0):
        saleAmount(packages_purchased, package_price, discount0, discount1, discount2, discount3, discount4)


def saleAmount(purchased, price, discount_0, discount_1, discount_2, discount_3, discount_4):
    # Calculate total price
    total0 = price - discount_0
    total1 = price - discount_1
    total2 = price - discount_2
    total3 = price - discount_3
    total4 = price - discount_4

    # Calculate the total amount
    if (purchased >= 10 and purchased <= 19):
        print("your total purchase is ($): ", total1)
    elif (purchased >= 20 and purchased <= 49):
        print("your total purchase is ($): ", total2)
    elif (purchased >= 50 and purchased <= 99):
        print("your total purchase is ($): ", total3)
    elif (purchased >= 99):
        print("your total purchase is ($): ", total4)
    else:
        print("your total purchase is ($): ", total0)

    # Call main


main()
