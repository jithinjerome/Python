#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - FACTORIAL.
#DATE - MARCH , 2022
#***********************************************************************
num = int(input("Enter the number to find the factorial:"))

factorial = 1
if num<0:
    print("Factorial does not exist:")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range (1,num+1):
        factorial = factorial * i
    print ("The factorial of ",num, " is ", factorial)