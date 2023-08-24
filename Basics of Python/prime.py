#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - PRIME NUMBER BETWEETN A RANGE
#DATE - AUGUST , 2023
#***********************************************************************
def prime(x,y):
    prime_list = []
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

start = int(input("Enter the strating number: "))
end = int(input("Enter the ending numbe: "))
lst = prime(start,end)
if len(lst)==0:
    print("There is no prime number in this range")
else:
    print("the prime number in this range are ",lst)

