#!/usr/bin/python3

from array import *

# Get a number from the user
# If number is below 10 and 20
#+ Save it in the array
# Else if number is outside the range
#+ Display 'Outside the range'
# If numbers saved to array is 5
#+ Display 'Thank you'
#+ Display each item in the array on a separate line.

nums = array('i', [])
num_count = 0

isTrue = True
while isTrue:
    num = int(input("Enter a number: "))
    if num >= 10 and num <= 20:
        nums.append(num)
        num_count = num_count + 1

        if num_count == 5:
            print("Thank you")
            for x in nums:
                print(x)
            isTrue = False
    else:
        print("Outside the range")
