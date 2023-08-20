#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - SIMPLE INTREST
#DATE - AUGUST , 2023
#***********************************************************************

def simpleINtrest(p,t,r):
    print("Principle amount = ",p)
    print("Time period = ",t)
    print("Rate of interest = ",r)

    si = (p*t*r)/100
    print("Simple intrest for ",p,"rupees for time period of ",t,"at the rate of ",r,"is ",si)

p = int(input("Enter the principle amount in rupees: "))
t = int(input("Enter the time: "))
r = int(input("Enter rate of interest: "))

simpleINtrest(p,t,r)