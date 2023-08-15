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

row = int(input("Enter row display: "))
if row >= 0 and row < len(twoD):
    print(f"{row}| {twoD[row]}")

    column = int(input("Display value in column: "))
    if column >= 0 and column < len(twoD[row]):
        pad_tab = ('\t' * column)
        print(f"{row}| {pad_tab}{twoD[row][column]}")

        answer = input("Do you want to change the value?[y|n] ")
        answer = answer.lower()

        if answer == 'y' or answer == 'yes':
            newValue = int(input("Enter new value: "))
            twoD[row][column] = newValue

        print(f"{row}| {twoD[row]}")
