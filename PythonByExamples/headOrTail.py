#!/usr/bin/python3

# Random choose Head or Tail ('h' or 't')
# Ask the user for their choice
# If user choice is the same as random choice
#+ Display 'You win'
# Otherwise display 'Bad luck'
# Display Random choice

import random

#def choice(c):
#    if c == 'h':
#        return 'heads'
#    elif c == 't':
#        return 'tails'
#    else:
#        pass

sel = ""
while sel != 'q':
    randChoice = random.choice(['h','t'])
    sel = input("Enter (h)eads or (t)ails: ")
    sel = sel.lower()
    sel = sel.strip()

    if sel == 'q':
        print("Exiting...")
        continue
    elif sel == randChoice:
        print("\nYou win")
    else:
        print("Bad luck...Try again")

    choice = ""
    if randChoice == 'h':
        choice = "Heads"
    elif randChoice == 't':
        choice = "Tails"

    print(f"\tRandom Choice is {choice}")
