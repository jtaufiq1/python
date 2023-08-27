#!/usr/bin/python3

# Open a file
# Convert to lowercase
# Save to a file

filename = input("File name: ")
file = open(filename)

text = ''
#tmp = open(filename,w)
for line in file:
    if line.isupper():
        print(line.isupper())
        #text = line.lower()
    else:
        pass
        #text = line
    #tmp.write(str(text)+'\n')
file.close()
