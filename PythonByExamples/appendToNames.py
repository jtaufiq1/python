#!/usr/bin/python3

# Create a new file 'names.txt'
# Write to five names to the text file
# Each name on a separate line

fileName = 'names.txt'
file = open(fileName,'a')

name = input("Add another name: ")
name = f'{name}\n'
file.write(name)
file.close()

print(open(fileName,'r').read(),end='')
