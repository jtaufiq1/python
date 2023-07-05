#!/usr/bin/python3

# LOOPS - For Loop

# Get name for user
# Display each character in name on each line

name = input("Enter your name: ")

for char in name:
    if char == ' ' or char == '\t' or char == '\n':
        continue
    else:
        print(char.upper())

# length = len(name)
# for i in range(0,length):
#    print(name[i])
