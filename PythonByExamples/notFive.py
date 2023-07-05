#!/usr/bin/python3

# Get from user
# While number is not 5 or more, continue
# If the number is 5 and over
#+ Display 'The last number you entered was [number]'
#+ Exit

# number = int(input("Enter a number: "))
while True:
    number = int(input("Enter a number: "))
    if number >= 5:
        print("The last number you entered was", number)
        break
