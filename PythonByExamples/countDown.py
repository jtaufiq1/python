#!/usr/bin/python3

# Get number from input
# Display number
# Count count down from 50 to the number

num = int(input("Enter a number below 50: "))

if num >= 50:
    print("Number must be less than 50")
else:
    print("Counting down from 50 to", num)
    for i in range(50, num-1, -1):
        print("\t", i)
