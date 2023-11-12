# Program # 2 exercise 9 

# Programmer: Olmedo, Johnny 

# CSC119-141 

# Submission date: 08/29/2019

# This Program calculates a persons weight on a reduced calorie intake for a period of 6 months

def main():
    # Constants for weight loss rate
    WEIGHT_LOSS = 4.00
    # Get the start weight 
    weight = float(input("enter your weight in pounds : "))
    # Calculate weight lost in the first month
    month_one = weight - WEIGHT_LOSS * 1
    # Calculate weight lost in the second month
    month_two = weight - WEIGHT_LOSS * 2        
    # Calculate weight lost in third month
    month_three = weight - WEIGHT_LOSS * 3
    # Calculate weight lost in fourth month
    month_four = weight - WEIGHT_LOSS * 4  
    # Calculate weight lost in fifth month 
    month_five = weight - WEIGHT_LOSS * 5
    # Calculate weight lost in sixth month
    month_six = weight - WEIGHT_LOSS * 6
    print()        
    print("You will weigh", month_one,
          " pounds in one month.")
    print("You will weigh", month_two,
          " pounds in two months.") 
    print("you will weigh", month_three, 
          " pounds in three months.")         
    print("you will weigh", month_four, 
          " pounds in four months.")   
    print("you will weigh", month_five,       
          " pounds in five months.")
    print("you will weigh", month_six, 
          " pounds in six months.")            
      
# Call main
main()    
    
