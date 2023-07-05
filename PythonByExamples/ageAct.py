#!/usr/bin/python3


# Get user age
# If age is 18 or more
#   Output 'You can vote'
# Else if age is 17
#   Output 'You can learn to drive'
# Else if age is 16
#   Output 'You can buy a lottery-ticket'
# Else
#   Output 'You can go Trickor-Treating'

age = int(input("What is your age? "))

if age >= 18:
    message = "You can vote"
elif age == 17:
    message = "You can learn to drive"
elif age == 16:
    message = "You can buy a lottery ticket"
elif age < 16 and age > 1:
    message = "You can go Trickor-Treating"

print()
print(message)
