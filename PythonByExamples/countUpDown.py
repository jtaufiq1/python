#!/usr/bin/python3

# Get direction to count towards (up/down)
#+ If direction is 'up'
#+  Get top number to count
#+  Count from 1 to top number
#+ If direction is 'down'
#+  Get number below 20
#+  Count down from 20 to the number
#+ Else
#+  Display "I don't understand"

print("\tCount number Up/Down".upper())
direction = input("Counting direction [up/down]: ")
direction = direction.lower()

if direction == 'up':
    num = int(input("Top Number: "))

    print("Counting from 1 to ", num)
    for i in range(1, num+1):
        print("\t", i)

elif direction == 'down':
    num = int(input("Enter a number below 20: "))

    if num >= 20:
        print("Number must be less than 20")
    else:
        print("Counting down from 20 to", num)
        for i in range(20, num-1, -1):
            print("\t", i)
else:
    print("[Error]: I don't understand")
