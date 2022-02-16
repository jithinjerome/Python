#***********************************************************************
#CREATOR : JITHIN JEROME
#TITLE - NUMBER GUESSING.
#DATE - JANUARY , 2022
#***********************************************************************
import random
top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range =int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0!")
        quit()
else:
    print("Enter a valid number")
    quit()
random_number = random.randrange(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    guess_number = input("Guess a number: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Enter a valid number")
        continue
    if random_number == guess_number:
        print("You got the correct answer!!")
        break
    elif  guess_number > random_number :
            print("You were above the number!")
    else:
            print("You were below the number!!")

print ("You got it in", guesses, "guesses")