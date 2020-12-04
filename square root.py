#Program 1
#Finding square root directly through code
print("Finding square root directly through code")
# To take input from the user
#number = float(input('Enter a number: '))
number=5 #This program works for all positive real numbers
num_sqrt=number ** 0.5 #"**" Exponent - left operand raised to the power of right
print("the square root of the number {0} is {1}".format(number,num_sqrt))

print("\n")

#For negative or complex numbers,it can be done as follows.
#Program 2
#Finding square root through builtin library math
print("Finding square root through builtin library math")
#import "math" library to use bilt in function "sqrt"
import math
number1 = float(input('Enter a number: '))
# Return the square root of different numbers
sqrt=math.sqrt(number1)
print("the square root of the number {0} is {1}".format(number1,sqrt))
