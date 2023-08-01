#!/usr/bin/python3

# Exercise 83 from Python By Examples: More on Strings

#msg = input("Enter a message in uppercase: ")
try_again = True
while try_again:
    msg = input("Enter a message in uppercase: ")
    if msg.isupper():
        print("Thank you")
        try_again = False
    else:
        print("Try again")
