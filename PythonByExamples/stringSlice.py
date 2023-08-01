#!/usr/bin/python3

# Get string from input
# Display string length
# String Slice:
#+ Display string section: Get section start & section end

line = input("Nursery Rhyme: ")
print("Line Length: ", len(line))

start = int(input("Start: "))
end  = int(input("End: "))

print(line[start:end])
