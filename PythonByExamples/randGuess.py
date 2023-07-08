#!/usr/bin/python3

import random
# Pick a random whole number between 1 and 10
# Get a number from the user until it matches
#+ the random number picked

randNumber = random.randint(1,10)
guessNumber = int(input("Guess a number: "))
while guessNumber != randNumber:
    guessNumber = int(input("\t"))
