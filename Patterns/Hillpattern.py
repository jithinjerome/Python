#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - HILL PATTERN.
#DATE - JANUARY , 2022
#***********************************************************************

print("\nHILL PATTERN \n")
n = int(input("Number of rows: "))
for i in range(n):
    for j in range(i,n):
        print(' ',end= '  ')
    for j in range(i):
        print('*',end= '  ')
    for j in range(i+1):
        print('*',end= '  ')
    print()