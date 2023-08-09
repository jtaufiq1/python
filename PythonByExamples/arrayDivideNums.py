#!/usr/bin/python3

from array import *

# Create an array of five numbers between 10 and 100
# Ask the user for whole number between two and five.
# If number is out of the range
#+ Display an error message, ask them to
#+ try again until a valid number is entered.
# Divide each of the number in the list by the
#+ number entered and display the answer to two
#+ decimal places.

nums = array('i',[10,20,30,45,75,15])
divisor = int(input("Enter a number between 2 and 5: "))

while divisor < 2 or divisor > 5:
    print("Invalid value. Number must be between 2 and 5")
    divisor = int(input("Try again: "))

for div in nums:
    ans = round((div/divisor),2)
    print(f"{div}/{divisor} = {ans}")
