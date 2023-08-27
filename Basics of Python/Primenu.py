#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - PRIME NUMBER
#DATE - AUGUST , 2023
#***********************************************************************

num = int(input("Enter the number: "))

if num>1:
    for i in range(2,(num/2)+1):
        if(num%i)==0:
            print("Its not a prime number")
        else:
            print("Its a prime number")
else:
    print("Its not a prime number")