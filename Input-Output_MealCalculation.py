# Programmer: Olmedo, Johnny

# Submission date: 08/28/2019

# This Program calculates the total amount of a meal purchased at a restaurant

def main():
    # Constants for the sales tax and tip rate
    SALE_TAX_RATE = 0.07
    TIP_RATE = 0.150
    # Get the amount of the purchase
    purchase = float(input("enter the amount of the purchase ($): "))
    # Calculate sale tax
    sales_tax = purchase * SALE_TAX_RATE
    # Calculate total tip
    total_tip = purchase * TIP_RATE
    # Calculate total sale
    total_sale = purchase + sales_tax + total_tip 
    # Display information about sale
    print()
    print("Purchase Amount : $", purchase)
    print("Total Tax: ", sales_tax)
    print("Total Tip: ", total_tip)
    print("Sale Total: ", total_sale)
# Call main

main()  
    
