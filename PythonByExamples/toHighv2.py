#!/usr/bin/python3

# Get a number
# If number is below 10
#   Output 'Too low'
# If number is between 10 and 20
#  Output 'Correct'
# Else
#  Output 'Too high'

num = int(input("Enter a number: "))

if num < 10:
    message = "Too low"
elif num >= 10 and num <= 20:
    message = "Correct"
else:
    message = "Too high"

print(message)
