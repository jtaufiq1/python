#!/usr/bin/python3

# Create list 4 three-digit numbers
# Display the list of numbers one on each line
# Get 3 digit number from the user
# If the number matches any in the list
#+ Display the position of that number in the list
# Else Display "That's not in the list"

numbers = ('999','333','555','422')

print(numbers)
number = input("Enter a 3-Digit number: ")
if len(number) != 3:
    print("number must be 3 digit")
else:
    if number in numbers:
        print(f"{number} is at position {numbers.index(number)}")
    else:
        print("That's not in the list")
