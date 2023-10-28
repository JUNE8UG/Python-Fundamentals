# Programmer: Olmedo, Johnny

# Submission date: 09/28/2019

# This program creates a multiplication table up to # 12.


def mulTable(maxNum):
   for row in range(1, maxNum +1):
      for col in range (1, maxNum+1):
         result = row * col
         print(f"\n{row} \t {col}")
         print(f"{row} * {col} = {result}")
         #print(format(row * col, '5d'), end=' ')
         print()
   #Call main

mulTable(12)   
            
