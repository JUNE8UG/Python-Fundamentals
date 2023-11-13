# Program 10 exercise # 8
# Programmer: Olmedo, Johnny
# CSC119-141
# Submission date: 11/10/2019 
# This program prints a sales report  

def main():
   # Explain what we are doing. 
   print("This program prints out a sales reprt for Brewsters Used Cars Inc.")
   # ask the user if they wish to continue  
   answer = input("Do you wish to continue [Y/N]? : ")
   # while user input is "Y" or "y" 
   while (answer == "Y" or answer == "y"):
      #Declare variables: salesID, prevSalesID, salesAmount, salesTotal, coTotal
      #Initialize salesTotal and coTotal = 0
      saleID = -1
      prevSalesID = -1
      salesAmount = 0
      salesTotal = 0
      coTotal = 0
      # call displayHeader
      displayHeader()   
      # call openFile function to open and display brewesters file 
      openFile(saleID, prevSalesID, salesAmount, coTotal, salesTotal)
      # allow the user to run the program again if so desired without having to restart 
      answer = input("Do you wish to run the program again [Y/N]?: ")
   # End program gracefully
   print("\nThank you and goodbye!")             

def displayHeader():
   #Display header
   print('''Brewsters User Cars, Inc. 
   Sales Report''') 
   print("Salesperson ID         Sale Amount")
   print("=====================================")
   
def openFile(ID, prevID, Amount, cTotal, sTotal):  
   # open the golf file in read mode
   with open("brewesters.txt", "r") as brewestersFile:
   
      for eachLine in brewestersFile:
         lineSplit = eachLine.split(" ")
         Amount = float(lineSplit[1])
         ID = int(lineSplit[0]) 
         if prevID < 0 :
            prevID = ID
         # represents if switching to a new salesperson
         if ID != prevID:
            print("Total sales for sales person #", prevID, "is : ", cTotal, "\n")
            # are we switching to new sales rep?
            # yes we are, this case
            prevID = ID
            sTotal += cTotal   
            cTotal = 0 
         # keep adding the saleAmount to the coTotal
         cTotal += Amount
         # print the saleID and saleAmount in each line
         print("{:15}($){:15}".format(str(ID),Amount))         
      # adding last cototal
      sTotal += cTotal   
      #printing last cototal
      print("Total sales for sales person #", prevID, "is : ", cTotal)
      # print the total overall total
      print("\nthe total overall sales ($): ", sTotal)      
      # close file
      brewestersFile.close()
   
# call main
main()