#!/usr/bin/python3

# Create two arrays
# Array one: Contains 3 numbers from user entry
# Array two: Contains 5 random numbers
# Join array one and array two
# Sort the joint arrays
# Display each element on a line.

import random
from array import *

in_list = array('f',[])
print("Enter 3 numbers")
for i in range(1,4):
    num = float(input(f"Enter number {i}: "))
    in_list.append(num)

rand_list = array('f',[])
for x in range(0,5):
    rand_num = random.ranint(0,999)
    rand_list.append(rand_num)

in_list.extend(rand_list)
in_list = sorted(in_list)

for j in in_list:
    print(j)
