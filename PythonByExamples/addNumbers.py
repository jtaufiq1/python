#!/usr/bin/python3

# Simple Script to add numbers
# Get list of numbers
# Sum the total
# Print out total sum

def help():
    print("Press S to sum numbers")

def getNumbers():
    numberList = list()

    while(1):
        i = input()
        if i is str("s") or i is "s".upper():
            return numberList
        else:
            number = float(i)
            numberList.append(number)

help()
total = sum(getNumbers())
print("Total is", total)
