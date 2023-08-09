#!/usr/bin/python3

# Get 5 numbers from the user
# Sort the numbers
# Display the numbers
# Ask the user to select one number
# Remove the number from the list
# Save it into new array list.

from array import *

nums = array('i',[])

for i in range(0,5):
    num = int(input(f"Enter a number {i}: "))
    nums.append(num)

nums = sorted(nums)
print(nums)

getRid = int(input("Enter number to remove: "))
if getRid in nums:
    index = nums.index(getRid)
    delNum = nums.pop(index)

    delNums = array('i',[delNum])
    #print(nums)
    #print(delNums)
else:
    print(f"{getRid} not in list")
