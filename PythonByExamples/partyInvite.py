#!/usr/bin/python3

# Get number of users to invite
# If number is below 10:
#+ Get names
#+ After each name display '[name] has been invited'
# If number is 10 or higher
#+ display 'Too many people'

print("It's Party time".upper())

num = int(input("How many do you want to invite? "))
if num > 0 and num < 10:
    print("Please enter the names")
    for i in range(0, num):
        name = input("Name: ")
        print(f"\t{name.title()} has been invited")
elif num >= 10:
    print("Too many people")
