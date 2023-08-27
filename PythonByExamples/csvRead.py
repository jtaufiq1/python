#!/usr/bin/python3

import csv
# READ: Comma Separated Values (csv)

csvFile = input("Select csv file: ")
file = open(csvFile, 'r')

for row in file:
    print(row,end='')
