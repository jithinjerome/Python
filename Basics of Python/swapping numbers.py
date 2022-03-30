#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - SWAPPING TWO NUMBERS.
#DATE - MARCH , 2022
#***********************************************************************
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Values before swapping")
print("First Number = "+str(num1))
print("First Number = "+str(num2))

#temp = num1
#num1 = num2
#num2 = temp

num1,num2 = num2,num1

print("Values after swapping")
print("First Number = "+str(num1))
print("First Number = "+str(num2))