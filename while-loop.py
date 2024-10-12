import random

print("Welcome to Guess the Number!")
print("The Rules are Simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10) # guess random number from 1 to 10
isGuessRight = False # initializes var to false because user hasn't guessed yet
while isGuessRight != True: # enters loop that continues if the guess is false
    guess= input("Guess a number between 1 And 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You Win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try Again.".format(guess))