#!/usr/bin/python3

# Input and Output
user_input = input("Enter a text: ")

with open("test.txt", 'w') as file:
    file.write(f"{user_input}\n")
file.close()
