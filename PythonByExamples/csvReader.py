#!/usr/bin/python3
import csv

# Open 'stars.csv' file in read mode
fileName = input("CSV file: ")
file = open(fileName,'r')

reader = csv.reader(file)
rows = list(reader)

for i in range(0,len(rows)):
    print(rows[i])
