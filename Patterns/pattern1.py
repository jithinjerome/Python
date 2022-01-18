#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - Square Pattern.
#DATE - JANUARY , 2022
#***********************************************************************

print("\nSQUARE PATTERN \n")
n = int(input("Number of rows: "))
for i in range(n):
    for j in range(n):
        print('*',end='   ')
    print()