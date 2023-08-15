#!/usr/bin/python3

grades = [
    [45,37,54],[62,58,59],
    [78,83,62],[49,47,60]
]

col_length = len(grades[0])
for x in range(0,col_length):
    if x == col_length-1:
        s = '\n'
    else:
        s = ''

    # Pad with spaces on the first column
    pad = ' '*3
    print(f"{pad}{x}",end=s)

row_num = len(grades)
for r in range(0,row_num):
    print(f"{r} {grades[r]}")
