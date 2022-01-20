import random
randomNumber=random.randint(1,100)
userGuess=None
guesses=0

while(userGuess != randomNumber):
    userGuess=int(input("Please Enter your guess: "))
    guesses +=1
    if(userGuess==randomNumber):
        print("You guess it right")
    else:
        if(userGuess>randomNumber):
            print("You guessed it wrong. please enter smaller number")
        else:
            print("You guessed it wrong. Please enter a larger number")

print(f"You guessed the number in {guesses} guesses")


with open("hiscore.txt",'r') as f:
    hiscore=int(f.read())

if (guesses<hiscore):
    print("You have just broken the record")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))

        