# Python program to swap two variables
print("Python program to swap two variables")
a=2
b=3
# To take inputs from the user
#a = input("Enter value of x:")
#b = input("Enter value of y:")

# create a temporary variable and swap the values
temp=a #temp is the temporary variable to hold the value
a=b
b=temp

print("The value of x after swapping:",a)
print("The value of y after swapping:",b)
