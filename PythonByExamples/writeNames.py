#!/usr/bin/python3

# Create a new file 'names.txt'
# Write to five names to the text file
# Each name on a separate line

fileName = 'names.txt'
file = open(fileName,'w')

for i in range(0,5):
    name = input("Enter a name: ")
    name = f'{name}\n'
    file.write(name)
file.close()
