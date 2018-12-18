# I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too low.
# Take a guess.
# 15
# Your guess is too low.
# Take a guess.
# 17
# Your guess is too high.
# Take a guess.
# 16
# Good job! You guessed my number in 4 guesses!


# This is a guess the number game. 

import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20. You have 6 guesses.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber: 
        print('Your guess is too low. ' + str(guessesTaken) + " guesses taken!")
    elif guess > secretNumber:
        print('Your guess is too high.' + str(guessesTaken) + " guesses taken!")
    else:
        break   #this condition is the correct guess

if guess == secretNumber: 
    print('Good Job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else: 
    print('Nope. The number I was thinking of was ' + str(secretNumber))

