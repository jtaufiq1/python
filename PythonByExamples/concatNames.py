#!/usr/bin/python3

# Get 2 names
# Concatenate the name with space in between

firstname = input("Firstname: ")
lastname = input("Lastname: ")

fullName = f"{firstname} {lastname}"
print()
print("Full Name: ", fullName.title())
print("Name Length: ", len(fullName))
