#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - INVERTED RIGHT SIDE TRIANGLE PATTERN
#DATE - JANUARY , 2022
#***********************************************************************

print("\nINVERTED RIGHT SIDE TRIANGLE PATTERN \n")
n = int(input("Number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(' ',end = '  ')
    for j in range(i,n):
        print('*',end ='  ')
    print()