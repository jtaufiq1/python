#!/usr/bin/python3

import random
# Set compNum to 50
# Get a number from the user
# While number is not equal to compNum
#+ Display 'The number is too low or too high'
#+ Display Guess another number, Get number from user
#+ If number is equal to compNum
#+  Display 'Well done, you took [count] attempts'

randNum = random.randint(1,5)

guessNumber = int(input("Pick a number: "))
if guessNumber == randNum:
    print("Well done")
elif guessNumber < randNum:
    print("Number too low")
elif guessNumber > randNum:
    print("Number too high")

if guessNumber != randNum:
    guessNumber = int(input("Pick a number again: "))
    if guessNumber == randNum:
        print("Correct")
    else:
        print("You lose")
