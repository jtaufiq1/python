#!/usr/bin/python3

import math

# Get integer over 500
# Calculate its square root
# Display it to two decimal places

num = int(input("Enter an integer above 500: "))

if num < 500:
    print("Error: Enter a number over 500")
else:
    sqrt = math.sqrt(num)
    print(round(sqrt, 2))
