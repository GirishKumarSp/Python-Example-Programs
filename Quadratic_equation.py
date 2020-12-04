# Solve the quadratic equation ax**2 + bx + c = 0
# We have imported the cmath module to perform complex square root.
# First, we calculate the discriminant and then find the two solutions of the quadratic equation.
# import complex math module
import cmath
a = 2
b = 5
c = 6
#To take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))
d = (b**2) - (4*a*c) #calculate the discriminant
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a) #formula ((-b+-√b^2-4ac) / 2a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
