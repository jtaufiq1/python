#!/usr/bin/python3

import csv
# READ: Comma Separated Values (csv)

csvFile = 'books.csv'
file = open(csvFile)

for row in file:
    print(row,end='')
