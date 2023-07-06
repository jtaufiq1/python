#!/usr/bin/python3

# Get firstname
# If length is under five chars, get surname and concatenate
# Display name in uppercase letter.
#
# If length of firstname is five or more chars
# Display firstname in lowercase chars.

firstname = input("Enter firstname: ")
flen = len(firstname)

if flen < 5:
    surname = input("Enter surname: ")
    fullName = f"{firstname} {surname}".upper()
    print(fullName)
elif flen >= 5:
    print(firstname.lower())
