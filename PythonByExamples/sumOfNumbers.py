#!/usr/bin/python3

# Set variable 'total = 0'
# Get 5 numbers; after each input
#+ Ask if that number is to be included
#+ If yes, add to the total
#+ If no, do not add to the total
#
# Display the total after the 5 input

total = 0

print("Enter 5 numbers:")
for i in range(1,6):
    print("number ", i, sep='', end='')
    num = int(input(": "))

    ans = input("Do you want to add to the total?[yes|no] ")

    if ans.lower() == "yes":
        total = total + num

print("Total =", total)
