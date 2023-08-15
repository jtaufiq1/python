#!/usr/bin/python3

# Open 'names.txt' file
# Display the list of names
# Ask the user for a name in the list
# Save all the other names in 'names2.txt' except
#+ the name entered.
fileName = 'names.txt'
fileName2 = 'names2.txt'
#print(open(fileName,'r').read(),end='')

n = input("Enter a name: ")
chosenName = f"{n}\n".title()

file = open(fileName,'r')
file2 = open(fileName2,'a')

for name in file:
    if chosenName != name:
        file2.write(name)
        #print(f"{name.strip()} appended to {fileName2}")
file.close()
file2.close()
