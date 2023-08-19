a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def large(a,b):
    if a<b:
        return b
    else:
        return a

print(large(a,b))



