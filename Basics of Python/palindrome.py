#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - STRING PALINDROME.
#DATE - JANUARY , 2022
#***********************************************************************
s = input("Enter a string:")
revs = (s[::-1])   #Reversing a string.
if(s == revs):
    print("The string is a PALINDROME")
else:
    print("The string is not a PALINDROME")