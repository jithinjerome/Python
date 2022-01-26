#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - SUM & AVERAGE.
#DATE - JANUARY , 2022
#***********************************************************************
n = int(input("How many numbers ,do you want to store?: "))
sum  = 0
for i in range(n):
    num = int(input("Enter the number: "))
    sum += num
avg = (sum/n)
print("Sum = ",sum)
print("Average = ",avg)