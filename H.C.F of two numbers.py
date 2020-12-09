# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))

"""
Output

The H.C.F. is 6
"""
"""
Source Code: Using the Euclidean Algorithm
# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)
print("The HCF is", hcf)

For example, if we want to find the H.C.F. of 54 and 24, we divide 54 by 24. The remainder is 6. Now,
 we divide 24 by 6 and the remainder is 0. Hence, 6 is the required H.C.F.
"""
