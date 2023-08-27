#!/usr/bin/python3
import csv

# Open 'stars.csv' file in read mode
fileName = 'stars.csv'
file = open(fileName,'r')

# Search in a csv file
search_term = input("Search data: ")

reader = csv.reader(file)
rows = tuple(reader)

for row in rows:
    if search_term in str(row):
        print(row)
