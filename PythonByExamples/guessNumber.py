#!/usr/bin/python3

# Set compNum to 50
# Get a number from the user
# While number is not equal to compNum
#+ Display 'The number is too low or too high'
#+ Display Guess another number, Get number from user
#+ If number is equal to compNum
#+  Display 'Well done, you took [count] attempts'

compNum = 50
count = 1

guessNumber = int(input("Guess a number: "))
while guessNumber != compNum:
    if guessNumber < compNum:
        print("The number is too low")
    elif guessNumber > compNum:
        print("The number is too high")
    count = count + 1

    guessNumber = int(input("Try again: "))

print("Well done, you took", count, "attempts")
