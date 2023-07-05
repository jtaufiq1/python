#!/usr/bin/python3

# Get 2 numbers from user
# Add the two numbers
# Ask to add another number, If answer is yes
# Get another number and add it

total = 0
nCount = 1
while True:
    num = int(input("Enter a number: "))
    total = total + num

    if nCount >= 2:
        res = input("Add another number [y|n]: ")
        res = res.lower()

        if res != 'y':
            break

    nCount = nCount +1
print("Total =", total)
