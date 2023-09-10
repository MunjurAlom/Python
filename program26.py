from random import randint

#print("----Guessing Game-----")
for x in range(1,11):
    guessNumber = int(input("Enter your guess number between 1 to 10: "))
    randomNumber = randint(1,10)

    if guessNumber == randomNumber:
        print("You've Won")
    else:
        print("You've lost")
        print("randomNumber was: ",randomNumber)


