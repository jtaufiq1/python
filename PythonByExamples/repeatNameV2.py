#!/usr/bin/python3

# LOOPS - For Loop
# Get name from user
# Get repeat count
# Output name N times

name = input("Enter your name: ")
count = int(input("Repeat times: "))

for i in range(1,count+1):
    print(i, name.title())
