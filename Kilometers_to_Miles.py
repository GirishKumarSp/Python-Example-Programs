#Python Program to Convert Kilometers to Miles
# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print("{} kilometers is equal to {} miles".format(kilometers,miles))
"""
to convert miles to kilometers using the following formula
kilometers = miles / conv_fac
"""