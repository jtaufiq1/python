#!/usr/bin/python3

# Get input of favorite color
# If color is red or Red or RED
#   Output "I liked red too"
# Else
#   Output "I don't like [color], I prefer red"

favColor = input("Enter favorite color: ")
favColor = favColor.lower()

if favColor == 'red':
    msg = "I liked red too"
else:
    msg = "I don't like " + favColor + ", I prefer red"

print(msg)
