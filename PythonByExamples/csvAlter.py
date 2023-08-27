#!/usr/bin/python3

import csv

fileName = "stars.csv"
file = list(csv.reader(open(fileName)))

tmp = []
for row in file:
    tmp.append(row)

# Temporal file handle
tempFile = "new_stars.csv"
file = open(tempFile,'w')

x = 0
for row in tmp:
    row_id = x
    name = tmp[x][0] = 'mohammad taufiq'
    age = tmp[x][1] = 29
    month = tmp[x][2] = 'december'
    newRec = f"{row_id},{name},{age},{month}\n"
    file.write(str(newRec))
    x = x + 1
file.close()
