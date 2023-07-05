#!/usr/bin/python3

# Get a number between 10 and 20
# If number is less than 10
#+ Display 'The number is too low'
#+ Display 'Try again', Get number from user
#
# If number is greater than 20
#+ Display 'The number is too high'
#+ Display 'Try again', Get number from user
#
# Keep repeating until the number is between 10 and 20
#+ Display 'Thank you'

while True:
    guessNumber = int(input("Guess a number: "))
    if guessNumber < 10:
        print("The number is too low")
    elif guessNumber > 20:
        print("The number is too high")
    elif guessNumber >= 10 and guessNumber <= 20:
        break
    print("\tTry again!")
print("Thank you")
