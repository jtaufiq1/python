#!/usr/bin/python3

# LOOPS: While Loop
#
# Set total to 0
# While the total is 50 or less
#+ Get a number from user
#+ Add the number to the total
#+ Display 'The total is ...[total]'
#+ Stop if total is over 50

total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total = total + num
    print("\tThe total is...", total)
