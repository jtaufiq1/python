#!/usr/bin/python3

# Get a list of five integers
# Store in an array
# Sort the list
# Display in reverse order

from array import *

intList = array('i',[])
print("\tEnter 5 integers")
for i in range(1,6):
    newValue = int(input(f"Enter an integer {i}: "))
    if newValue < 0 or newValue >= 0:
        intList.append(newValue)
    else:
        print("Invalid integer")
        i = i - 1

intList = sorted(intList)
intList.reverse()
print(f"\t==> {intList} <==")
