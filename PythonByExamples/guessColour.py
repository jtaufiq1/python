#!/usr/bin/python3

import random
# Display five colours
# Ask the user to a colour
# If the user's pick is the same as the program's pick
#+ Display 'Well done'
# Otherwise Display '[Witty message]'
# Ask them to guess again:
# If answer is wrong Display '[Witty message]' again until guess is correct

COLOURS = ['red','blue','green','yellow','white']
randColour = random.choice(COLOURS)
randColourIndex = str(COLOURS.index(randColour))
colourIndex = ""

for colour in COLOURS:
    print(f"{COLOURS.index(colour)}) {colour}")

colourIndex = input("Choose a colour: ")
while colourIndex != randColourIndex:
    if randColour == 'red':
        print(f"You are probably feeling {randColour.upper()}")
    elif randColour == 'blue':
        print(f"Your are probably feeling {randColour.upper()} right now")
    elif randColour == 'green':
        print(f"I bet you are {randColour.upper()} with envy")
    elif randColour == 'yellow':
        print(f"It's fun to have {randColour.upper()} mangoes around")
    elif randColour == 'white':
        print(f"Hello, {randColour.upper()} Ape!")
    colourIndex = input("Guess again: ")

print("Well done")
