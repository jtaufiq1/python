#!/usr/bin/python3

# LOOPS - For Loop

# Get name for user
# Get repeat times
# Display each character in name on each line

name = input("Enter your name: ")
count = int(input("Repeat times: "))

for i in range(0, count):
    for char in name:
        if char == ' ' or char == '\t' or char == '\n':
            continue
        else:
            print(char.upper())
    print("***", i, "***")

# length = len(name)
# for i in range(0,length):
#    print(name[i])
