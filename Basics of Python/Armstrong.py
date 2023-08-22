n = int(input("Enter the number to check whether it is armstrong or not: "))
s = n
sum = 0
p = len(str(n))

while n!=0:
    r = n%10
    sum += (r**p)
    n = n//10


if s==sum:
    print("The give number is armstrong")
else:
    print("The given number is not armstrong")