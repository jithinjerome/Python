#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - SIMPLE USER DESIGNED COMPUTER QUIZ.
#DATE - JANUARY , 2022
#***********************************************************************
print("Welcome to my computer Quiz !!")

playing = input("Do you want to play?(Y/N):  ")

if playing.lower() != "y":
    quit()

print("Okay ! Let's Start the Game :) ")
score = 0
answer = input("What does CPU stand for ?  ")
if answer.lower() == "central processing unit":
    print("Correct!!")
    score += 1
else:
    print("Wrong Answer!")

answer = input("What does GPU stands for ?  ")
if answer.lower() == "graphics processing unit":
    print("Correct!!")
    score += 1
else:
    print("Wrong Answer!")

answer = input("What does RAM stands stands for ?  ")
if answer.lower() == "random access memory":
    print("Correct!!")
    score += 1
else:
    print("Wrong Answer!")

answer = input("What does PSU stands for ?  ")
if answer.lower() == "power supply":
    print("Correct!!")
    score += 1
else:
    print("Wrong Answer!")

print("You got "+str(score)+" questions correct!")
print("You got "+str((score/4)*100)+"%. ")
