#!/usr/bin/python3

import random
# Pick a random whole number between 1 and 10
# Get a number from the user until it matches
#+ the random number picked

randNumber = random.randint(1,10)
guess = True
while guess:
    guessNumber = int(input("Guess a number: "))
    if guessNumber < randNumber:
        print("Too low")
    elif guessNumber > randNumber:
        print("Too high")
    elif guessNumber == randNumber:
        guess = False
