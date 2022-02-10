#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - MATRIX ADDITION.
#DATE - JANUARY , 2022
#***********************************************************************
print("MATRIX 1")
r = int(input("Enter the no of rows: "))
c = int(input("Enter the no of columns: "))
a = [] #matrix 1
for i in range(r):
    t = []
    for j in range(c):
        values = int(input(f"Enter a[{i}][{j}]: "))
        t.append(values)
    a.append(t)
print("\n")

print("MATRIX 2")
r1 = int(input("Enter the no of rows: "))
c1= int(input("Enter the no of columns: "))
b = [] #matrix 2
for i in range(r1):
    t = []
    for j in range(c1):
        values = int(input(f"Enter b[{i}][{j}]: "))
        t.append(values)
    b.append(t)

result = []  # result matrix
for i in range(r):
    t = []
    for j in range(c):
        values = a[i][j]+b[i][j]
        t.append(values)
    result.append(t)

print("MATRIX 1")
for i in range(r):
    for j in range(c):
        print(a[i][j],end=" ")
    print()

print("MATRIX 2")
for i in range(r1):
    for j in range(c1):
        print(b[i][j],end=" ")
    print()

print("RESULT MATRIX ")
for i in range(r):
    for j in range(c):
        print(result[i][j],end=" ")
    print()

