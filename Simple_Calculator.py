# Program make a simple calculator
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4): ")

# Check if choice is one of the four options
if choice in ("1","2","3","4"):

    num1= float(input("enter first number: "))
    num2= float(input("enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == '2':
        print(num1, "-", num2, "=",  num1 - num2)

    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == '4':
        print(num1, "/", num2, "=", num1 / num2)
else:
    print("invalid input")
