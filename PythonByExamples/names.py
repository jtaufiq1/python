#!/usr/bin/python3

def border(chars):
    banner = '*'
    title = chars.upper()
    print(title)

# Input first name and last name
firstName = input("Firstname: ")
lastName = input("Lastname: ")
age = input("Age: ")
placeOfBirth = input("Place of Birth: ")
print()

border("personal info")
print("Full Name: ", firstName, lastName)
print("Age: ", age)
print("Place of Birth: ", placeOfBirth)
print()
