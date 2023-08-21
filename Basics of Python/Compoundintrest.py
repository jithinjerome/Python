#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - SIMPLE INTREST
#DATE - AUGUST , 2023
#***********************************************************************

def c_intrest(p,t,r):
    amount = p*(1+r/100)**t
    ci = amount - p
    print("Compound intrest is ",ci)

p = int(input("Enter the principle amount in rupees: "))
t = int(input("Enter the time: "))
r = float(input("Enter rate of interest: "))

c_intrest(p,t,r)