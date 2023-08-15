#!/usr/bin/python3

# Simple 2D List

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

row = int(input("Enter row number: "))
column = int(input("Enter column number: "))
pad_tab = ('\t' * column)
print(f"{row}| {pad_tab}{twoD[row][column]}")
