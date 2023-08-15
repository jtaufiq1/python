#!/usr/bin/python3

# Simple 2D List

twoD = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

print(f"    1\t2\t3")
for s in range(0,17):
    print("-",end='')
print()
for i in range(0,len(twoD)):
    print(f'{i} |',end=' ')
    for x in twoD[i]:
        print(x,end='\t')
    print()
