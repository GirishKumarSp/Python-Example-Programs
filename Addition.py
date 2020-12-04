#Addition accepts the input from user
print("Performing Addition by accepts the values from user")
try:
    number1=float(input("enter the first number: ")) #try and except will ensure user enters values or returns value 0
except:
    number1=0 #if user enters anything other than numbers program will assume the number as 0
              #Here we can also use promt to inform that user has not entered valid number and let user enter the value
              #print("Please enter a valid number")
              #exit() #exit from the progarm and let the user enter the value
try:
    number2=float(input("enter the second number: ")) #input function will accept in mode of strings so we use "float" and add them
except:                                               #"float" will convert the obtained string by the user to float value in order to add
    number2=0

sum=number1+number2 #adds the obtained data

print("Obtained result of addition of {0} and {1} is {2} ".format(number1,number2,sum)) #displays the obtained results
 #(.format) is the new positional farmat /we can call it as placeholders (can be rearaged)

print("\n") #for maintaining space between both programs "\n"

#We can add numbers directly
print("Performing Addition of values directly by code")
num1=5
num2=5
sum1=num1+num2
print("sum of digits are {0} and {1} is {2}".format(num1,num2,sum1))
