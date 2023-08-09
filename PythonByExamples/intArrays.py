#!/usr/bin/python3

from array import *

nums = array('i',[45,324,654,45,264])
print(f"type:{type(nums)}, id:{id(nums)}")
for x in nums:
    print(x)

newValue = int(input("Enter a number: "))
nums.append(newValue)

nums.reverse()
print(f"Reversed: {nums}")
nums = sorted(nums)
print(f"Sorted: {nums}")
print(f"Removed: {nums.pop()}")
