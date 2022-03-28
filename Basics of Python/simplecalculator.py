#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - MATRIX ADDITION.
#DATE - MARCH , 2022
#***********************************************************************
print("------CALCULATOR------")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Select an Operation to Perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")

operation = input()

if operation == "1":
    print("Sum = "+str(num1+num2))
elif operation == "2":
    print("Difference = " + str(num1 - num2))
elif operation == "3":
    print("Product = " + str(num1 * num2))
elif operation == "4":
    print("Division = " + str(num1 / num2))
else:
    print("Invalid Choice!!")

