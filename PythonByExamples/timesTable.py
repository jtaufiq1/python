#!/usr/bin/python3

# Get a number between 1 and 12
# Display the times table for that number

print("\t\tTimes Table".upper())
print("Enter a number between 1 & 12")
number = int(input("Enter: "))

if number < 1 or number > 12:
    print("Number must be between 1 and 12 inclusive")
    print("Try again...")
else:
    for i in range(1,13):
        print("\t", number, "x", i, "=", number * i)
