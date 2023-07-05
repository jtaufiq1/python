#!/usr/bin/python3

# Get name and a number
# If number is below 10, display name that number of times
# If number is larger than 10, display 'Too high' 3 times

print("Display name a number of times")
name = input("Enter a name: ")
num = int(input("number: "))

if num < 1:
    pass
elif num >= 1 and num <= 10:
    for i in range(1, num+1):
        print(" ", i, name.title())
else:
    print("Too high!")
    print("Too high!")
    print("Too high!")
