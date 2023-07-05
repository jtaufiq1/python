#!/usr/bin/python3

# Rainy Day
# Ask if it's raining. Prompt for answer [yes|no]
# If yes
#   Ask if it's windy. Prompt for answer [yes|no]
#   If yes
#     Output 'It's too windy for an umbrella'
#   Else
#     Output 'Take an umbrella'
# Else
#   Output 'Enjoy your day'

answer = input("Is it raining? [yes|no]: ")

answer = answer.lower()
if answer == "yes":
    answer = input("Is it windy? [yes|no]: ")

    answer = answer.lower()
    if answer == "yes":
        message = "It's too windy to take an umbrella"
    else:
        message = "Take an umbrella"
else:
    message = "Enjoy your day"

print()
print(message)
print()
