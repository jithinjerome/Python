#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - GIVEN NUMBER IS FIBONACCI OR NOT
#DATE - AUGUST , 2023
#***********************************************************************
#A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square

import math

n = int(input("Enter a number to check if it is fibonacci or not: "))
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonacci(n):
    return isPerfectSquare(5*n*n+4)or isPerfectSquare(5*n*n-4)

if isFibonacci(n)==True:
    print(n," is a fibonacci number")
else:
    print(n," is not a fibonacci number")
