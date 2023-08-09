#!/usr/bin/python3

from array import *

# Create an array of 5 numbers
#+ of which 2 numbers are repeated in it.
# Display the whole array list.
# Ask the user to enter one of the numbers
#+ from the list.
# Display the message saying how many times
#+ that number appears in the array list.
nums = array('i',[45,50,100,14,13,14])

print(nums)
getNum = int(input("Enter one number from the list: "))
if getNum in nums:
    print(f"{getNum} appears {nums.count(getNum)} time(s) in the list")
else:
    print(f"{getNum} is not in the list")
