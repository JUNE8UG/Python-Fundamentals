import time
import sys

def main():
    # Explain what we are doing
    print('''
    The Ackermann function is known for growing rapidly, and its values can become very large 
    even for small inputs. It's often used to test the efficiency of algorithms and programming 
    languages due to its recursive nature. However, it's worth noting that for certain values of 
    m and n, the function may grow so quickly that it exceeds the recursion depth of many programming languages, 
    leading to stack overflow errors.
    ''')


    # Print the current recursion limit
    print("Current recursion limit:", sys.getrecursionlimit())

    # Set a higher recursion limit (e.g., 30000)
    sys.setrecursionlimit(30000)

    # Get user input for m and n
    minput = int(input("Enter an integer value for m: "))
    ninput = int(input("Enter an integer value for n: "))

    # Record the start time
    startTime = time.time()

    # Call the Ackermann's Function
    ackermanns = ackerFunction(minput, ninput)

    # Record the end time
    endTime = time.time()

    # Calculate the total time taken
    realTime = endTime - startTime

    # Print the result and the time taken
    print("Result of Ackermann's function:", ackermanns)
    print("The time the function took to run:", realTime)

def ackerFunction(m, n):
    if m == 0:  # Base case: if m == 0
        return n + 1  # Return 1 plus n
    elif n == 0:  # Base case: if n == 0
        return ackerFunction(m - 1, 1)
    else:  # Recursive case: otherwise
        return ackerFunction(m - 1, ackerFunction(m, n - 1))

# Call the main function to execute the program
main()
