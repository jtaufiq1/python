#!/usr/bin/python3

from array import *

# Display an array of five numbers
# Select one number from  the list
# Display the position of the item in the list
# If number is not in the list
#+ try again until an item in the list is selected.

num_lists = array('i',[15,30,45,10,20,25])
print(list(num_lists))

num = int(input("Select a number: "))
while num not in num_lists:
    num = int(input("Try again: "))

print(f"{num} is at position {num_lists.index(num)}")
