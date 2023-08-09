#!/usr/bin/python3

from array import *

nums = array('i',[45,324,654,45,264])
newArray = array('i',[])
print(f"type:{type(nums)}, id:{id(nums)}")
print(f"type:{type(newArray)}, id:{id(newArray)}")

more = int(input("How many items: "))
for x in range(0,more):
    newValue = int(input("Enter a number: "))
    newArray.append(newValue)

nums.extend(newArray)
print(nums)
print(f"{nums.count(45)}")

getRid = int(input("Enter item index: "))
nums.pop(getRid)
print(nums)
