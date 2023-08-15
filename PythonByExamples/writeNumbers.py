#!/usr/bin/python3

# Write to a new text file 'numbers.txt'
# Add five numbers to the file
# All numbers must be on the same line separated by a comma

fileName = 'numbers.txt'
file = open(fileName,'w')

count = 0
for i in range(20,120,20):
    file.write(str(i))
    count = count + 1
    if count <= 4:
        file.write(",")
    else:
        file.write("\n")
file.close()
