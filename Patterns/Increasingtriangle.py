#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - Increasing Triangle.
#DATE - JANUARY , 2022
#***********************************************************************

print("\nINCREASING TRIANGLE PATTERN \n")
n = int(input("Number of rows: "))
for i in range(n):
    for j in range(i+1):
        print('*',end='   ')
    print()