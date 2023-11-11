# Programmer: Olmedo, Johnny

# Submission date: 09/21/2019

# This Program calculates shipping charges

def main():
    # Constants for shipping rate
    rate1 = 1.10
    rate2 = 2.20
    rate3 = 3.70
    rate4 = 3.80
    # Get the weight of the package
    package_weight = float(input("enter the weight of your package in pounds : "))

    # Calculate the shippment rate
    if (package_weight >= 2 and package_weight <= 6):
        print("your shipping rate per pound will be ($): ", rate2)

    elif (package_weight >= 6 and package_weight <= 10):
        print("your shipping rate per pound will be ($): ", rate3)

    elif (package_weight > 10):
        print("your shipping rate per pound will be ($): ", rate4)

    else:
        print("your shipping rate per pound will be ($): ", rate1)

    # Display shiping cost
    showShipping(rate1, rate2, rate3, rate4, package_weight)


def showShipping(r1, r2, r3, r4, weight):
    # Constants for shipping cost
    cost1 = weight * r1
    cost2 = weight * r2
    cost3 = weight * r3
    cost4 = weight * r4
    # Calculate shipping cost
    if (weight > 2 and weight <= 6):
        print("your shipping cost will be ($): ", cost2)
    elif (weight > 6 and weight <= 10):
        print("your shipping rate wll be ($): ", cost3)
    elif (weight > 10):
        print("your shipping rate will be ($): ", cost4)
    else:
        print("your shipping rate will be ($): ", cost1)

        # Call main


main()
