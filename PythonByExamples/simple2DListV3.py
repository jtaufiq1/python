#!/usr/bin/python3

# Simple 2D List
# Ask row number from user
# Display ONLY that row
# Ask for new value
# Append to the end of the row

twoD = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

print(f"    0\t1\t2")
for s in range(0,17):
    print("-",end='')
print()
for i in range(0,len(twoD)):
    print(f'{i} |',end=' ')
    for x in twoD[i]:
        print(x,end='\t')
    print()

print()
row = int(input("Enter row number: "))
#column = int(input("Enter column number: "))
#pad_tab = ('\t' * column)
print(f"{row}| {twoD[row]}")

newValue = int(input("Add another number: "))
twoD[row].append(newValue)

print(f"{row}| {twoD[row]}")
